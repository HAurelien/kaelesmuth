#!/usr/bin/env python3
"""The state of the world at a given year.

    python3 _tools/world_at.py 2758                         whole world, in the first calendar
    python3 _tools/world_at.py 2758 --calendar zephyrion    year given in another calendar
    python3 _tools/world_at.py 2758 --focus "Angres Rimas"  plus a close-up of a note
    python3 _tools/world_at.py 2758 --planet Aethernam      one planet only
    python3 _tools/world_at.py 2758 --window 20             "recent" and "upcoming" = 20 years
    python3 _tools/world_at.py 2758 --json                  for other tools

Who is alive and how old, where they are, which organizations and places
exist, and which events are ongoing, recent or coming up, per planet. This is
the shared query behind the Write and Compile skills: import World from here
rather than re-reading the notes another way.

Rules it follows (see Schema.md):
- A year y covers [y, y + 1). Notes in another calendar are converted when
  _tools/calendars.py has the data, and are listed as "not comparable" when not.
- Someone is where their latest dated event with a location put them, else at
  their residence (or a god's realm), else at their birthplace.
- Someone with no birth year is "not yet recorded" before their first dated
  event, so an unknown birth never makes a person appear too early.
"""

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vault import Vault, link_target, norm, parse_date  # noqa: E402
from calendars import Calendars  # noqa: E402

PERSON_TYPES = ("character", "god")
OFF_PLANET = "Off-planet"
BASE_BLOCK_RE = re.compile(r"```base\n.*?```\n?", re.S)
EPS = 1e-9


def is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def fmt_year(y):
    """2758 -> '2758', -120 -> '120 PME', 2758.4 -> '≈2758'."""
    if y is None:
        return "?"
    n = int(round(y))
    s = "%d PME" % -n if n < 0 else str(n)
    return ("≈" + s) if abs(y - n) > EPS else s


def body_text(note, demote=0):
    """The note's text for dossiers and close-ups: Bases blocks and the
    headings they leave empty removed, headings pushed `demote` levels down."""
    lines = BASE_BLOCK_RE.sub("", note.body).strip().split("\n")

    def level(line):
        m = re.match(r"^(#{1,6}) ", line)
        return len(m.group(1)) if m else 0

    keep = []
    for i, line in enumerate(lines):
        lv = level(line)
        if lv:
            rest = [l for l in lines[i + 1:] if l.strip()]
            nxt = rest[0] if rest else None
            if nxt is None or (level(nxt) and level(nxt) <= lv):
                continue
            line = "#" * min(6, lv + demote) + line[lv:]
        keep.append(line)
    return re.sub(r"\n{3,}", "\n\n", "\n".join(keep)).strip()


class World:
    """The vault seen through time, with every year in one calendar."""

    def __init__(self, vault=None, calendar=None):
        self.vault = vault or Vault()
        self.cals = Calendars(self.vault.schema)
        self.calendar = calendar or self.cals.names[0]
        if self.calendar not in self.cals.names:
            raise ValueError("unknown calendar %r (known: %s)" % (calendar, ", ".join(self.cals.names)))
        self.planets = [p for p in self.vault.of_type("place")
                        if str(p.get("place_type") or "").strip().lower() == "planet"]
        self.events = self.vault.of_type("event")
        self.people = self.vault.of_type(*PERSON_TYPES)
        self._planet_cache = {}
        self._events_of = {}
        for ev in self.events:
            for key in ("participants", "location", "related", "species"):
                for n in self.links(ev, key):
                    lst = self._events_of.setdefault(n.rel, [])
                    if ev not in lst:
                        lst.append(ev)

    # ------------------------------------------------------------ links

    def links(self, note, key):
        """Notes a link or list-of-links property points to (broken links skipped)."""
        v = note.get(key)
        out = []
        for x in (v if isinstance(v, list) else [v]):
            n = self.vault.resolve_link(x)
            if n is not None and n not in out:
                out.append(n)
        return out

    def links_to(self, note, key, types=None):
        """Notes whose `key` property links to `note` (the reverse of links())."""
        return [n for n in self.vault.notes
                if (types is None or n.type in types) and note in self.links(n, key)]

    def events_of(self, note, keys=("participants",)):
        """Events linking `note` in one of `keys`, in date order."""
        evs = [ev for ev in self._events_of.get(note.rel, []) if any(note in self.links(ev, k) for k in keys)]
        return self.sort_events(evs)

    def events_at(self, place):
        """Events located at `place` or anywhere inside it, in date order."""
        inside = {p.rel for p in self.places_inside(place)} | {place.rel}
        return self.sort_events([ev for ev in self.events
                                 if any(l.rel in inside for l in self.links(ev, "location"))])

    def places_inside(self, place):
        out, todo = [], [place]
        while todo:
            cur = todo.pop()
            for p in self.vault.of_type("place"):
                if p not in out and p is not place and cur in self.links(p, "parent"):
                    out.append(p)
                    todo.append(p)
        return out

    # ------------------------------------------------------------ planets

    def place_planets(self, place, _seen=None):
        """Planet names a place is on: itself if a planet, else its `planet`, else its parent's."""
        if place is None or place.type != "place":
            return []
        if place.rel in self._planet_cache:
            return self._planet_cache[place.rel]
        seen = (_seen or set()) | {place.rel}
        if place in self.planets:
            res = [place.name]
        else:
            res = [n.name for n in self.links(place, "planet")]
            if not res:
                for par in self.links(place, "parent"):
                    if par.rel not in seen:
                        res = self.place_planets(par, seen)
        self._planet_cache[place.rel] = res
        return res

    def note_planets(self, note):
        """Planet names a note belongs to, from its `planet`, else its location."""
        res = [n.name for n in self.links(note, "planet")]
        if not res:
            for loc in self.links(note, "location"):
                res += [p for p in self.place_planets(loc) if p not in res]
        return res

    # ------------------------------------------------------------ time

    def source_calendar(self, note):
        return note.get("calendar") or self.calendar

    def comparable(self, note):
        return self.cals.can_convert(self.source_calendar(note), self.calendar)

    def to_here(self, year, note):
        """A year written on `note`, in this world's calendar (None if unknown or not convertible)."""
        if year is None:
            return None
        return self.cals.convert(year, self.source_calendar(note), self.calendar)

    def interval(self, note):
        """[lo, hi) the note exists over, in this calendar. None for an unknown side."""
        s, e = self.vault.span(note)
        lo = self.to_here(s, note) if s is not None else None
        hi = self.to_here(e + 1, note) if e is not None else None
        return lo, hi

    def label(self, note):
        """Readable date of a note's span: '2758', '2740–2745', 'zephyrion 1712 (≈2758 aethernam)'."""
        s, e = self.vault.span(note)
        if s is None and e is None:
            return "undated"
        if note.type == "event" and e == s:
            e = None
        txt = fmt_year(s) if e is None else "%s–%s" % (fmt_year(s), fmt_year(e))
        if note.type == "event" and isinstance(note.get("date"), str) and note.get("date") != str(s):
            txt = note.get("date") + (" – " + note.get("end_date") if note.get("end_date") else "")
        src = self.source_calendar(note)
        if src != self.calendar:
            lo = self.to_here(s, note) if s is not None else None
            here = (" (%s %s)" % (fmt_year(lo), self.calendar)) if lo is not None else " (not convertible yet)"
            txt = "%s %s%s" % (src, txt, here)
        if note.get("approximate") is True:
            txt += " (approx.)"
        return txt

    def sort_key(self, ev):
        lo, _ = self.interval(ev) if self.comparable(ev) else (None, None)
        d = parse_date(ev.get("date")) if self.source_calendar(ev) == self.calendar else None
        fine = tuple(x or 0 for x in (d[1:] if d else (0, 0, 0, 0)))
        return (lo is None, lo if lo is not None else 0, fine, ev.name.casefold())

    def sort_events(self, evs):
        return sorted(evs, key=self.sort_key)

    # ------------------------------------------------------------ people

    def first_seen(self, person):
        los = [self.interval(ev)[0] for ev in self.events_of(person) if self.comparable(ev)]
        los = [x for x in los if x is not None]
        return min(los) if los else None

    def life(self, person, year):
        """{'status', 'age', 'age_calendar', 'note'} for a person at `year`.

        status: alive, born this year, dies this year, unborn, dead,
        not yet recorded (no birth year, first dated event is later),
        undated (nothing dated at all), unknown (other calendar)."""
        if not self.comparable(person):
            return {"status": "unknown", "age": None, "age_calendar": None,
                    "note": "dated in the %s calendar, not convertible yet" % self.source_calendar(person)}
        lo, hi = self.interval(person)
        y0, y1 = year, year + 1
        born, died = self.vault.span(person)
        res = {"status": "alive", "age": None, "age_calendar": self.source_calendar(person), "note": ""}
        if lo is not None and lo >= y1 - EPS:
            res["status"] = "unborn"
            res["note"] = "born in %s" % fmt_year(lo)
            return res
        if hi is not None and hi <= y0 + EPS:
            res["status"] = "dead"
            res["note"] = "died in %s" % fmt_year(hi - 1)
            return res
        if born is not None:
            here_in_src = self.cals.convert(year, self.calendar, self.source_calendar(person))
            res["age"] = int(here_in_src - born + EPS) if here_in_src is not None else None
            if lo is not None and lo > y0 - EPS:
                res["status"] = "born this year"
        else:
            seen = self.first_seen(person)
            if seen is None and hi is None:
                res["status"] = "undated"
                res["note"] = "no birth, death or dated event"
                return res
            if seen is not None and seen >= y1 - EPS:
                res["status"] = "not yet recorded"
                res["note"] = "first recorded in %s" % fmt_year(seen)
                return res
            res["note"] = "birth year unknown"
        if hi is not None and hi < y1 + EPS:
            res["status"] = "dies this year"
        return res

    def whereabouts(self, person, year):
        """Where a person is at `year`, and how we know.

        {'places': [names], 'planets': [names], 'source': event|residence|realm|birthplace|planet|None,
         'event': name or None, 'since': year or None, 'ongoing': bool}"""
        best = None
        for ev in self.events_of(person):
            if not self.comparable(ev):
                continue
            lo, hi = self.interval(ev)
            locs = self.links(ev, "location")
            if lo is None or lo >= year + 1 - EPS or not locs:
                continue
            if best is None or self.sort_key(ev) >= self.sort_key(best[0]):
                best = (ev, lo, hi, locs)
        if best:
            ev, lo, hi, locs = best
            planets = []
            for l in locs:
                planets += [p for p in self.place_planets(l) if p not in planets]
            if not planets and not any(self.place_planets(l) for l in locs):
                planets = [OFF_PLANET] if locs else []
            return {"places": [l.name for l in locs], "planets": planets, "source": "event",
                    "event": ev.name, "since": lo, "ongoing": hi is not None and hi > year + EPS}
        for key in ("residence", "realm", "birthplace"):
            places = [p for p in self.links(person, key) if p.type == "place" or key == "residence"]
            if places:
                planets = []
                for p in places:
                    planets += [x for x in self.place_planets(p) if x not in planets]
                return {"places": [p.name for p in places], "planets": planets or self.note_planets(person),
                        "source": key, "event": None, "since": None, "ongoing": False}
        return {"places": [], "planets": self.note_planets(person), "source": "planet" if self.note_planets(person) else None,
                "event": None, "since": None, "ongoing": False}

    def family(self, person):
        parents = self.links(person, "parents")
        partners = self.links(person, "partners")
        children = self.links_to(person, "parents", PERSON_TYPES)
        siblings = []
        for par in parents:
            for c in self.links_to(par, "parents", PERSON_TYPES):
                if c is not person and c not in siblings:
                    siblings.append(c)
        return {"parents": parents, "partners": partners, "children": children, "siblings": siblings}

    def relationships(self, person):
        out = []
        for rel in self.vault.of_type("relationship"):
            first, second = (self.links(rel, "first") or [None])[0], (self.links(rel, "second") or [None])[0]
            if person in (first, second):
                me, other = ("first", "second") if first is person else ("second", "first")
                out.append({"note": rel, "other": (second if me == "first" else first),
                            "my_role": rel.get(me + "_role"), "their_role": rel.get(other + "_role"),
                            "my_attitude": rel.get(me + "_attitude"), "their_attitude": rel.get(other + "_attitude")})
        return out

    def exists(self, note, year):
        """True/False whether a place or organization exists at `year`, None if not comparable."""
        if not self.comparable(note):
            return None
        lo, hi = self.interval(note)
        return (lo is None or lo < year + 1 - EPS) and (hi is None or hi > year + EPS)

    # ------------------------------------------------------------ events around a year

    def classify(self, ev, year, window):
        """'now', 'recent', 'upcoming', None (outside the window), 'undated' or 'other calendar'."""
        if not self.comparable(ev):
            return "other calendar"
        lo, hi = self.interval(ev)
        if lo is None:
            return "undated"
        if hi is None:
            hi = lo + 1
        if lo < year + 1 - EPS and hi > year + EPS:
            return "now"
        if hi <= year + EPS and hi > year - window + EPS:
            return "recent"
        if lo >= year + 1 - EPS and lo < year + 1 + window - EPS:
            return "upcoming"
        return None

    # ------------------------------------------------------------ the query

    def person_entry(self, p, year):
        life = self.life(p, year)
        where = self.whereabouts(p, year)
        return {
            "name": p.name, "type": p.type, "status": life["status"], "age": life["age"],
            "age_calendar": life["age_calendar"], "life_note": life["note"],
            "where": where["places"], "where_source": where["source"], "where_event": where["event"],
            "where_since": where["since"], "where_ongoing": where["ongoing"],
            "planets": where["planets"] or self.note_planets(p),
            "affiliations": [o.name for o in self.links(p, "affiliations")],
            "conditions": [c.name for c in self.links(p, "conditions")],
            "importance": p.get("importance"),
        }

    def event_entry(self, ev):
        return {"name": ev.name, "when": self.label(ev), "planets": self.note_planets(ev),
                "location": [l.name for l in self.links(ev, "location")],
                "participants": [n.name for n in self.links(ev, "participants")],
                "event_type": ev.get("event_type"), "status": ev.get("status"),
                "after": [n.name for n in self.links(ev, "after")],
                "before": [n.name for n in self.links(ev, "before")]}

    def state_at(self, year, window=10, planet=None, focus=()):
        planet_names = [p.name for p in self.planets] + [OFF_PLANET]
        if planet:
            hit = [n for n in planet_names if norm(n) == norm(planet)]
            if not hit:
                raise ValueError("unknown planet %r (known: %s)" % (planet, ", ".join(planet_names)))
            planet_names = hit
        groups = {n: {"people": [], "events": {"now": [], "recent": [], "upcoming": []}} for n in planet_names}
        state = {
            "year": year, "calendar": self.calendar, "window": window,
            "conversion": {"ready": self.cals.ready, "missing": self.cals.missing()},
            "planets": groups, "gods": [], "organizations": [], "places_changing": [],
            "dead": [], "unborn": [], "not_yet_recorded": [], "undated_people": [], "not_comparable": [],
            "undated_events": [], "focus": [],
        }
        for p in sorted(self.people, key=lambda n: n.name.casefold()):
            e = self.person_entry(p, year)
            if e["status"] == "unknown":
                state["not_comparable"].append(p.name)
                continue
            if e["status"] in ("dead", "unborn", "not yet recorded", "undated"):
                key = {"dead": "dead", "unborn": "unborn", "not yet recorded": "not_yet_recorded",
                       "undated": "undated_people"}[e["status"]]
                if not planet or any(norm(x) == norm(planet) for x in e["planets"]):
                    state[key].append({"name": p.name, "note": e["life_note"], "planets": e["planets"]})
                continue
            if p.type == "god":
                state["gods"].append(e)
                continue
            for pl in (e["planets"] or [OFF_PLANET]):
                if pl in groups:
                    groups[pl]["people"].append(e)
        for ev in self.sort_events(self.events):
            c = self.classify(ev, year, window)
            if c == "other calendar":
                state["not_comparable"].append(ev.name)
                continue
            if c is None:
                continue
            entry = self.event_entry(ev)
            if c == "undated":
                state["undated_events"].append(entry)
                continue
            for pl in (entry["planets"] or [OFF_PLANET]):
                if pl in groups:
                    groups[pl]["events"][c].append(entry)
        for org in sorted(self.vault.of_type("organization"), key=lambda n: n.name.casefold()):
            ex = self.exists(org, year)
            if ex is None:
                state["not_comparable"].append(org.name)
            elif ex:
                state["organizations"].append({"name": org.name, "since": self.label(org),
                                               "planets": self.note_planets(org)})
        for pl in self.vault.of_type("place"):
            lo, hi = self.interval(pl) if self.comparable(pl) else (None, None)
            if lo is None and hi is None:
                continue
            ex = self.exists(pl, year)
            state["places_changing"].append({"name": pl.name, "exists": ex, "span": self.label(pl)})
        for name in focus:
            state["focus"].append(self.focus_entry(name, year, window))
        return state

    def focus_entry(self, name, year, window):
        note = self.vault.resolve(name)
        if note is None:
            return {"name": name, "error": "no note called %r" % name}
        out = {"name": note.name, "type": note.type, "file": note.rel}
        if note.type in PERSON_TYPES:
            out.update(self.person_entry(note, year))
            fam = self.family(note)
            out["family"] = {k: [{"name": n.name, **self.life(n, year)} for n in v] for k, v in fam.items()}
            out["relationships"] = [{"with": r["other"].name if r["other"] else None, "note": r["note"].name,
                                     "role": r["my_role"], "their_role": r["their_role"],
                                     "attitude": r["my_attitude"], "their_attitude": r["their_attitude"]}
                                    for r in self.relationships(note)]
            out["affiliations"] = [{"name": o.name, "exists": self.exists(o, year)} for o in self.links(note, "affiliations")]
            evs = self.events_of(note)
        elif note.type == "place":
            out["exists"] = self.exists(note, year)
            out["planets"] = self.place_planets(note)
            inside = {note.rel} | {p.rel for p in self.places_inside(note)}
            out["people_here"] = [p.name for p in self.people
                                  if self.life(p, year)["status"] in ("alive", "born this year", "dies this year")
                                  and any((self.vault.resolve(x) or note).rel in inside
                                          for x in self.whereabouts(p, year)["places"])]
            evs = self.events_at(note)
        elif note.type == "organization":
            out["exists"] = self.exists(note, year)
            members = self.links_to(note, "affiliations", PERSON_TYPES)
            out["members"] = [{"name": m.name, **self.life(m, year)} for m in members]
            out["leaders"] = [n.name for n in self.links(note, "leaders")]
            evs = self.events_of(note)
        else:
            evs = self.events_of(note, keys=("participants", "location", "related", "species"))
        before, now, after, undated = [], [], [], []
        for ev in evs:
            c = self.classify(ev, year, 10 ** 9)
            (before if c == "recent" else now if c == "now" else after if c == "upcoming" else undated).append(ev)
        out["events_before"] = [self.event_entry(e) for e in before[-5:]]
        out["events_now"] = [self.event_entry(e) for e in now]
        out["events_after"] = [self.event_entry(e) for e in after[:5]]
        out["events_undated"] = [self.event_entry(e) for e in undated]
        return out


# ---------------------------------------------------------------- text output

def _person_line(e):
    bits = [e["name"]]
    if e["age"] is not None:
        bits.append("age %d" % e["age"] + ("" if e["age_calendar"] is None else ""))
    if e["status"] not in ("alive",):
        bits.append(e["status"])
    if e["life_note"]:
        bits.append(e["life_note"])
    if e["where"]:
        how = {"event": "since [[%s]]" % e["where_event"], "residence": "lives there", "realm": "realm",
               "birthplace": "birthplace, nothing later known"}.get(e["where_source"], "")
        if e["where_source"] == "event" and e["where_ongoing"]:
            how = "during [[%s]]" % e["where_event"]
        bits.append("at " + ", ".join("[[%s]]" % w for w in e["where"]) + (" (%s)" % how if how else ""))
    else:
        bits.append("place unknown")
    return "- " + "; ".join(bits)


def _event_line(e):
    s = "- [[%s]] (%s)" % (e["name"], e["when"])
    if e["location"]:
        s += " at " + ", ".join("[[%s]]" % x for x in e["location"])
    if e["participants"]:
        s += ". With " + ", ".join("[[%s]]" % x for x in e["participants"])
    return s


def render(state):
    y, cal, w = state["year"], state["calendar"], state["window"]
    out = ["# The world in %s (%s calendar)" % (fmt_year(y), cal), ""]
    if not state["conversion"]["ready"]:
        out.append("_Only notes in the %s calendar are placed in time: %s._" % (cal, state["conversion"]["missing"]))
        out.append("")
    for f in state["focus"]:
        out += render_focus(f, state)
    for pl, g in state["planets"].items():
        if not g["people"] and not any(g["events"].values()):
            continue
        out += ["## %s" % pl, ""]
        if g["people"]:
            out += ["**People**", ""] + [_person_line(e) for e in g["people"]] + [""]
        for key, title in (("now", "Happening this year"), ("recent", "Last %d years" % w), ("upcoming", "Next %d years" % w)):
            if g["events"][key]:
                out += ["**%s**" % title, ""] + [_event_line(e) for e in g["events"][key]] + [""]
    if state["gods"]:
        out += ["## Gods", ""] + [_person_line(e) for e in state["gods"]] + [""]
    if state["organizations"]:
        out += ["## Organizations that exist", ""]
        out += ["- [[%s]] (%s)" % (o["name"], o["since"] if o["since"] != "undated" else "founding unknown") for o in state["organizations"]]
        out.append("")
    if state["places_changing"]:
        out += ["## Places with a start or end", ""]
        out += ["- [[%s]] %s: %s" % (p["name"], p["span"], "exists" if p["exists"] else "does not exist") for p in state["places_changing"]]
        out.append("")
    for key, title in (("dead", "Already dead"), ("unborn", "Not born yet"), ("not_yet_recorded", "Not recorded yet"),
                       ("undated_people", "No dates at all (could be alive)")):
        if state[key]:
            out += ["## %s" % title, ""] + ["- [[%s]] (%s)" % (
                d["name"], d["note"] if key != "undated_people" else (", ".join(d["planets"]) or OFF_PLANET))
                for d in state[key]] + [""]
    if state["undated_events"]:
        out += ["## Undated events (can't be placed)", ""] + [_event_line(e) for e in state["undated_events"]] + [""]
    if state["not_comparable"]:
        out += ["## In another calendar, not placed", "", ", ".join("[[%s]]" % n for n in state["not_comparable"]), ""]
    return "\n".join(out).rstrip() + "\n"


def render_focus(f, state):
    out = ["## Close-up: %s" % f["name"], ""]
    if "error" in f:
        return out + [f["error"], ""]
    if f["type"] in PERSON_TYPES:
        out.append(_person_line(f))
        for k in ("parents", "partners", "children", "siblings"):
            if f["family"][k]:
                out.append("- %s: %s" % (k.capitalize(), ", ".join(
                    "[[%s]] (%s%s)" % (m["name"], m["status"], (", age %d" % m["age"]) if m["age"] is not None else "")
                    for m in f["family"][k])))
        if f["affiliations"]:
            out.append("- Affiliations: " + ", ".join(
                "[[%s]]%s" % (a["name"], "" if a["exists"] in (True, None) else " (does not exist at this date)")
                for a in f["affiliations"]))
        if f["conditions"]:
            out.append("- Conditions: " + ", ".join("[[%s]]" % c for c in f["conditions"]))
        for r in f["relationships"]:
            out.append("- [[%s]]: %s to [[%s]] (attitude %s); they are %s (attitude %s)" % (
                r["note"], r["role"] or "?", r["with"], r["attitude"] or "?", r["their_role"] or "?", r["their_attitude"] or "?"))
    elif f["type"] == "place":
        out.append("- Exists: %s; planet: %s" % ({True: "yes", False: "no", None: "unknown"}[f["exists"]], ", ".join(f["planets"]) or OFF_PLANET))
        if f["people_here"]:
            out.append("- People here: " + ", ".join("[[%s]]" % p for p in f["people_here"]))
    elif f["type"] == "organization":
        out.append("- Exists: %s" % {True: "yes", False: "no", None: "unknown"}[f["exists"]])
        if f["members"]:
            out.append("- Members: " + ", ".join("[[%s]] (%s)" % (m["name"], m["status"]) for m in f["members"]))
        if f["leaders"]:
            out.append("- Leaders: " + ", ".join("[[%s]]" % m for m in f["leaders"]))
    out.append("")
    for key, title in (("events_before", "Before (latest 5)"), ("events_now", "This year"),
                       ("events_after", "After (next 5)"), ("events_undated", "Undated")):
        if f.get(key):
            out += ["**%s**" % title, ""] + [_event_line(e) for e in f[key]] + [""]
    return out


def parse_year(s):
    """'2758', '-120' or '120 PME' -> int."""
    s = s.strip()
    m = re.fullmatch(r"(\d+)\s*PME", s, re.I)
    if m:
        return -int(m.group(1))
    return int(s)


def main(argv=None):
    ap = argparse.ArgumentParser(description="State of the Kaelesmuth world at a year.")
    ap.add_argument("year", help="year, e.g. 2758, -120 or '120 PME'")
    ap.add_argument("--calendar", default=None, help="calendar of the year (default: the first in schema.json)")
    ap.add_argument("--planet", default=None, help="only this planet (or Off-planet)")
    ap.add_argument("--window", type=int, default=10, help="years counted as recent / upcoming (default 10)")
    ap.add_argument("--focus", action="append", default=[], help="note to look at closely (repeatable)")
    ap.add_argument("--json", action="store_true", help="print JSON instead of text")
    ap.add_argument("--vault", default=None, help="vault folder (default: the one holding _tools)")
    args = ap.parse_args(argv)
    world = World(Vault(args.vault) if args.vault else Vault(), args.calendar)
    state = world.state_at(parse_year(args.year), args.window, args.planet, args.focus)
    if args.json:
        print(json.dumps(state, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(render(state))
    return 0


if __name__ == "__main__":
    sys.exit(main())
