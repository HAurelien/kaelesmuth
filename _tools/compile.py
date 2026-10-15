#!/usr/bin/env python3
"""Compile a dossier on a character, place, organization, event, timeline or period.

    python3 _tools/compile.py "Angres Rimas"                      a whole life
    python3 _tools/compile.py "Angres Rimas" --from 2740 --to 2760
    python3 _tools/compile.py Aethernam                           a place and everything inside it
    python3 _tools/compile.py "Lone Protectors"                   an organization and its members
    python3 _tools/compile.py "The Great Cataclysm"               an event and the people in it
    python3 _tools/compile.py "Rimas timeline"                    a timeline
    python3 _tools/compile.py --from 2740 --to 2760               a period of the whole world
    python3 _tools/compile.py --from 2740 --to 2760 --planet Aethernam
    ... --calendar zephyrion        years given in another calendar
    ... --out "_export/dossiers/Angres Rimas.md"

Everything is in date order, with the full text of every event, and shows
how the subject changes across the span (age, whereabouts, who is alive,
which organizations exist). It is built on world_at.World, so it follows
the same rules as the "world at year X" query. A dossier is generated:
regenerate it after the notes change instead of editing it.
"""

import argparse
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vault import Vault  # noqa: E402
from world_at import World, PERSON_TYPES, OFF_PLANET, EPS, fmt_year, body_text, parse_year  # noqa: E402

ALIVE = ("alive", "born this year", "dies this year")


class Dossier:
    def __init__(self, world, subject=None, start=None, end=None, planet=None):
        self.w = world
        self.subject = subject
        self.planet = planet
        self.items = []          # dated: {"lo", "hi", "title", "kind", "note", "line"}
        self.undated = []        # events that can't be placed
        self.other_cal = []      # events in a calendar that can't be converted
        self.sources = set()
        self.start, self.end = start, end
        self.build()

    # ---------------------------------------------------------------- collect

    def add_event(self, ev):
        self.sources.add(ev.name)
        if not self.w.comparable(ev):
            self.other_cal.append(ev)
            return
        lo, hi = self.w.interval(ev)
        if lo is None:
            self.undated.append(ev)
            return
        self.items.append({"lo": lo, "hi": hi or lo + 1, "title": ev.name, "kind": "event", "note": ev,
                           "key": self.w.sort_key(ev)})

    def add_mark(self, note, which, title):
        """A birth, death, founding... taken from a note's span."""
        if not self.w.comparable(note):
            return
        lo, hi = self.w.interval(note)
        y = lo if which == "start" else (hi - 1 if hi is not None else None)
        if y is None:
            return
        self.sources.add(note.name)
        self.items.append({"lo": y, "hi": y + 1, "title": title, "kind": "mark", "note": note,
                           "key": (False, y, (0, 0, 0, 0), title.casefold())})

    def build(self):
        w, s = self.w, self.subject
        if s is None:
            self.kind = "period"
            for ev in w.events:
                if self.planet and not self.on_planet(w.note_planets(ev)):
                    continue
                self.add_event(ev)
            for p in w.people:
                if self.planet and not self.on_planet(w.note_planets(p)):
                    continue
                self.add_mark(p, "start", "Birth of %s" % p.name)
                self.add_mark(p, "end", "Death of %s" % p.name)
            for o in w.vault.of_type("organization"):
                self.add_mark(o, "start", "Founding of %s" % o.name)
                self.add_mark(o, "end", "End of %s" % o.name)
            for pl in w.vault.of_type("place"):
                self.add_mark(pl, "start", "%s comes to exist" % pl.name)
                self.add_mark(pl, "end", "%s stops existing" % pl.name)
        elif s.type in PERSON_TYPES:
            self.kind = "person"
            for ev in w.events_of(s, keys=("participants", "related")):
                self.add_event(ev)
            fam = w.family(s)
            self.add_mark(s, "start", "Birth of %s" % s.name)
            self.add_mark(s, "end", "Death of %s" % s.name)
            for role, people in fam.items():
                for p in people:
                    self.add_mark(p, "start", "Birth of %s (%s)" % (p.name, role[:-1] if role != "children" else "child"))
                    self.add_mark(p, "end", "Death of %s (%s)" % (p.name, role[:-1] if role != "children" else "child"))
            for o in w.links(s, "affiliations"):
                self.add_mark(o, "start", "Founding of %s" % o.name)
                self.add_mark(o, "end", "End of %s" % o.name)
        elif s.type == "place":
            self.kind = "place"
            for ev in w.events_at(s):
                self.add_event(ev)
            at = w.events_at(s)
            for ev in w.events_of(s, keys=("related",)) + [e for e in w.events if s.name in w.note_planets(e)]:
                if ev not in at:
                    at.append(ev)
                    self.add_event(ev)
            self.add_mark(s, "start", "%s comes to exist" % s.name)
            self.add_mark(s, "end", "%s stops existing" % s.name)
            for p in w.places_inside(s):
                self.add_mark(p, "start", "%s comes to exist" % p.name)
                self.add_mark(p, "end", "%s stops existing" % p.name)
        elif s.type == "organization":
            self.kind = "organization"
            for ev in w.events_of(s, keys=("participants", "related")):
                self.add_event(ev)
            self.add_mark(s, "start", "Founding of %s" % s.name)
            self.add_mark(s, "end", "End of %s" % s.name)
            for m in w.links_to(s, "affiliations", PERSON_TYPES):
                self.add_mark(m, "start", "Birth of %s (member)" % m.name)
                self.add_mark(m, "end", "Death of %s (member)" % m.name)
        elif s.type == "timeline":
            self.kind = "timeline"
            for ev in w.links_to(s, "timelines", ("event",)):
                self.add_event(ev)
        elif s.type == "event":
            self.kind = "event"
            lo, hi = w.interval(s) if w.comparable(s) else (None, None)
            self.add_event(s)
            people = w.links(s, "participants")
            for p in people:
                for ev in w.events_of(p, keys=("participants",)):
                    if ev is not s and ev not in [i["note"] for i in self.items] + self.undated + self.other_cal:
                        self.add_event(ev)
            if self.start is None and lo is not None:
                self.start = lo - 10
            if self.end is None and hi is not None:
                self.end = hi + 10 - 1
        else:
            self.kind = s.type or "note"
            for ev in w.events_of(s, keys=("participants", "location", "related", "species")):
                self.add_event(ev)
        # default span: the subject's own, else what the items cover
        if s is not None and s.type != "event" and w.comparable(s):
            lo, hi = w.interval(s)
            if self.start is None and lo is not None:
                self.start = int(lo // 1)
            if self.end is None and hi is not None:
                self.end = int(-(-hi // 1)) - 1
        if self.start is not None or self.end is not None:
            a = self.start if self.start is not None else float("-inf")
            b = (self.end + 1) if self.end is not None else float("inf")
            self.items = [i for i in self.items if i["lo"] < b - EPS and i["hi"] > a + EPS]
        titles = {i["title"].casefold() for i in self.items if i["kind"] == "event"}
        self.items = [i for i in self.items if i["kind"] == "event" or i["title"].split(" (")[0].casefold() not in titles]
        self.items.sort(key=lambda i: i["key"])
        if self.items:
            if self.start is None:
                self.start = int(self.items[0]["lo"] // 1)
            if self.end is None:
                self.end = int(max(i["hi"] for i in self.items) - EPS)

    def on_planet(self, planets):
        from vault import norm
        if not planets:
            return norm(self.planet) == norm(OFF_PLANET)
        return any(norm(p) == norm(self.planet) for p in planets)

    # ---------------------------------------------------------------- render

    def title(self):
        span = "%s to %s" % (fmt_year(self.start), fmt_year(self.end)) if self.start is not None else "no dates"
        if self.subject is None:
            where = self.planet or "Kaelesmuth"
            return "%s, %s (%s calendar)" % (where, span, self.w.calendar)
        return "%s, %s (%s calendar)" % (self.subject.name, span, self.w.calendar)

    def person_state(self, p, year):
        life = self.w.life(p, year)
        where = self.w.whereabouts(p, year)
        place = ", ".join("[[%s]]" % x for x in where["places"]) or "unknown"
        age = str(life["age"]) if life["age"] is not None else "?"
        return life["status"], age, place

    def render(self):
        w, s = self.w, self.subject
        out = ["# Dossier: %s" % self.title(), "",
               "_Compiled from the vault on %s with `_tools/compile.py`. Regenerate it after the notes change rather than editing it._" % datetime.date.today().isoformat(), ""]
        if not w.cals.ready:
            out += ["_Years from other calendars can't be placed yet: %s._" % w.cals.missing(), ""]
        if s is not None:
            out += self.render_subject()
        out += self.render_changes()
        out += ["## Chronology", ""]
        if not self.items:
            out += ["Nothing dated in this span.", ""]
        for it in self.items:
            out += self.render_item(it)
        if self.undated:
            out += ["## Undated", "", "Linked to the subject but without a year. `after` / `before` hints are shown when the note has them.", ""]
            for ev in w.sort_events(self.undated):
                out += self.render_event(ev, "###")
        if self.other_cal:
            out += ["## In another calendar", "", "Dated in a calendar that can't be converted yet, so not placed in the chronology.", ""]
            for ev in self.other_cal:
                out += self.render_event(ev, "###")
        out += ["## Sources", "", ", ".join("[[%s]]" % n for n in sorted(self.sources | ({s.name} if s else set()), key=str.casefold)), ""]
        return "\n".join(out).rstrip() + "\n"

    def render_subject(self):
        w, s = self.w, self.subject
        out = ["## %s" % s.name, ""]
        facts = []
        skip = {"type", "aliases", "tags", "wa_id", "wa_merged_ids", "status"}
        for k, v in s.props.items():
            if k in skip or v in (None, "", []):
                continue
            facts.append("- **%s**: %s" % (k, ", ".join(map(str, v)) if isinstance(v, list) else v))
        facts.append("- **type / status**: %s / %s" % (s.type, s.get("status")))
        out += facts + [""]
        text = body_text(s, demote=2)
        if text:
            out += ["### The note", "", text, ""]
        if s.type in PERSON_TYPES:
            fam = w.family(s)
            if any(fam.values()):
                out += ["### Family", ""]
                for k, v in fam.items():
                    if v:
                        out.append("- %s: %s" % (k.capitalize(), ", ".join("[[%s]] (%s)" % (p.name, w.label(p)) for p in v)))
                out.append("")
            rels = w.relationships(s)
            if rels:
                out += ["### Relationships", ""]
                for r in rels:
                    self.sources.add(r["note"].name)
                    out.append("#### [[%s]]" % r["note"].name)
                    out.append("")
                    out.append("%s is %s to %s (attitude %s); %s is %s (attitude %s)." % (
                        s.name, r["my_role"] or "?", r["other"].name if r["other"] else "?", r["my_attitude"] or "?",
                        r["other"].name if r["other"] else "?", r["their_role"] or "?", r["their_attitude"] or "?"))
                    t = body_text(r["note"], demote=3)
                    if t:
                        out += ["", t]
                    out.append("")
        if s.type == "organization":
            members = w.links_to(s, "affiliations", PERSON_TYPES)
            if members:
                out += ["### Members", ""] + ["- [[%s]] (%s)" % (m.name, w.label(m)) for m in members] + [""]
            subs = w.links_to(s, "parent_org", ("organization",))
            if subs:
                out += ["### Sub-organizations", ""] + ["- [[%s]]" % o.name for o in subs] + [""]
        if s.type == "place":
            inside = w.places_inside(s)
            if inside:
                out += ["### Places inside", ""] + ["- [[%s]]" % p.name for p in inside] + [""]
            residents = [p for p in w.people if s in w.links(p, "residence") or s in w.links(p, "birthplace")]
            if residents:
                out += ["### People born or living here", ""] + ["- [[%s]]" % p.name for p in residents] + [""]
        return out

    def checkpoints(self):
        years = []
        if self.start is not None:
            years.append(self.start)
        for it in self.items:
            y = int(it["lo"] // 1)
            if y not in years:
                years.append(y)
        if self.end is not None and self.end not in years:
            years.append(self.end)
        return sorted(y for y in years if (self.start is None or y >= self.start) and (self.end is None or y <= self.end))

    def render_changes(self):
        """How the subject changes across the span."""
        w, s = self.w, self.subject
        if self.start is None or self.end is None:
            return []
        out = ["## Across the span", ""]
        if s is not None and s.type in PERSON_TYPES:
            out += ["| Year | Status | Age | Where |", "|---|---|---|---|"]
            for y in self.checkpoints():
                st, age, place = self.person_state(s, y)
                out.append("| %s | %s | %s | %s |" % (fmt_year(y), st, age, place))
            out.append("")
            fam = [p for v in w.family(s).values() for p in v]
            if fam:
                out += ["Family at the start and at the end:", ""]
                for p in fam:
                    a, b = w.life(p, self.start)["status"], w.life(p, self.end)["status"]
                    out.append("- [[%s]]: %s → %s" % (p.name, a, b) if a != b else "- [[%s]]: %s" % (p.name, a))
                out.append("")
            orgs = w.links(s, "affiliations")
            changed = [(o, w.exists(o, self.start), w.exists(o, self.end)) for o in orgs]
            changed = [c for c in changed if c[1] != c[2]]
            if changed:
                out += ["Organizations that appear or disappear:", ""]
                out += ["- [[%s]]: %s → %s" % (o.name, "exists" if a else "doesn't exist", "exists" if b else "doesn't exist") for o, a, b in changed]
                out.append("")
            return out
        if s is not None and s.type == "organization":
            members = w.links_to(s, "affiliations", PERSON_TYPES)
            out += ["| Member | At %s | At %s |" % (fmt_year(self.start), fmt_year(self.end)), "|---|---|---|"]
            for m in members:
                out.append("| [[%s]] | %s | %s |" % (m.name, w.life(m, self.start)["status"], w.life(m, self.end)["status"]))
            return out + [""]
        if s is not None and s.type == "event":
            people = [p for p in w.links(s, "participants") if p.type in PERSON_TYPES]
            if people:
                lo, _ = w.interval(s) if w.comparable(s) else (None, None)
                if lo is not None:
                    y = int(lo // 1)
                    out += ["Participants when it happens (%s):" % fmt_year(y), "",
                            "| Who | Status | Age | Where they were before |", "|---|---|---|---|"]
                    for p in people:
                        st, age, place = self.person_state(p, y - 1)
                        st_now = w.life(p, y)["status"]
                        age_now = w.life(p, y)["age"]
                        out.append("| [[%s]] | %s | %s | %s |" % (p.name, st_now, age_now if age_now is not None else "?", place))
                    out.append("")
            return out
        # place, timeline, period: who is alive and which organizations exist, start vs end
        a = w.state_at(self.start, 0, self.planet)
        b = w.state_at(self.end, 0, self.planet)

        def alive(st):
            names = set()
            for g in st["planets"].values():
                names |= {e["name"] for e in g["people"]}
            return names | {e["name"] for e in st["gods"]}

        def orgs(st):
            return {o["name"] for o in st["organizations"]}

        pa, pb, oa, ob = alive(a), alive(b), orgs(a), orgs(b)
        out.append("From %s to %s:" % (fmt_year(self.start), fmt_year(self.end)))
        out.append("")
        for title, names in (("Alive at both ends", pa & pb), ("Gone by the end", pa - pb), ("Alive or first recorded by the end", pb - pa),
                             ("Organizations at both ends", oa & ob), ("Organizations gone", oa - ob),
                             ("Organizations new", ob - oa)):
            if names:
                out.append("- %s: %s" % (title, ", ".join("[[%s]]" % n for n in sorted(names, key=str.casefold))))
        return out + [""]

    def render_item(self, it):
        if it["kind"] == "event":
            return self.render_event(it["note"], "###")
        return ["### %s, %s" % (fmt_year(it["lo"]), it["title"]), ""]

    def render_event(self, ev, h):
        w, s = self.w, self.subject
        out = ["%s %s" % (h, ev.name), ""]
        meta = ["**When**: %s" % w.label(ev)]
        locs = w.links(ev, "location")
        planets = w.note_planets(ev)
        meta.append("**Where**: %s" % (", ".join("[[%s]]" % l.name for l in locs) or "unknown")
                    + (" (%s)" % ", ".join(planets) if planets else ""))
        parts = w.links(ev, "participants")
        if parts:
            meta.append("**Who**: %s" % ", ".join("[[%s]]" % p.name for p in parts))
        for key in ("after", "before"):
            if w.links(ev, key):
                meta.append("**%s**: %s" % (key.capitalize(), ", ".join("[[%s]]" % n.name for n in w.links(ev, key))))
        if ev.get("status") != "canon":
            meta.append("**Status**: %s" % ev.get("status"))
        out += [" · ".join(meta), ""]
        if s is not None and s.type in PERSON_TYPES and w.comparable(ev) and w.interval(ev)[0] is not None:
            y = int(w.interval(ev)[0] // 1)
            st, age, place = self.person_state(s, y - 1)
            life = w.life(s, y)
            out += ["_%s at the time: %s%s, coming from %s._" % (
                s.name, life["status"], (", age %d" % life["age"]) if life["age"] is not None else "", place), ""]
        text = body_text(ev, demote=len(h))
        if text:
            out += [text, ""]
        return out

    def to_json(self):
        return {
            "subject": self.subject.name if self.subject else None, "kind": self.kind,
            "calendar": self.w.calendar, "start": self.start, "end": self.end, "planet": self.planet,
            "chronology": [{"year": i["lo"], "title": i["title"], "kind": i["kind"], "note": i["note"].name,
                            "text": body_text(i["note"]) if i["kind"] == "event" else ""} for i in self.items],
            "undated": [e.name for e in self.undated], "other_calendar": [e.name for e in self.other_cal],
            "sources": sorted(self.sources),
        }


def main(argv=None):
    ap = argparse.ArgumentParser(description="Compile a dossier from the Kaelesmuth vault.")
    ap.add_argument("subject", nargs="?", help="note name (character, place, organization, event, timeline); omit for a period")
    ap.add_argument("--from", dest="start", default=None, help="first year (e.g. 2740 or '120 PME')")
    ap.add_argument("--to", dest="end", default=None, help="last year")
    ap.add_argument("--calendar", default=None, help="calendar of the years (default: the subject's, else the first)")
    ap.add_argument("--planet", default=None, help="period only: limit to one planet (or Off-planet)")
    ap.add_argument("--out", default=None, help="write to this file instead of printing")
    ap.add_argument("--json", action="store_true", help="JSON instead of Markdown")
    ap.add_argument("--vault", default=None)
    args = ap.parse_args(argv)
    vault = Vault(args.vault) if args.vault else Vault()
    subject = None
    if args.subject:
        subject = vault.resolve(args.subject)
        if subject is None:
            print("No note called %r." % args.subject, file=sys.stderr)
            return 2
    elif args.start is None and args.end is None:
        print("Give a note name, or --from / --to for a period.", file=sys.stderr)
        return 2
    cal = args.calendar or (subject.get("calendar") if subject is not None else None)
    world = World(vault, cal)
    start = parse_year(args.start) if args.start else None
    end = parse_year(args.end) if args.end else None
    d = Dossier(world, subject, start, end, args.planet)
    text = json.dumps(d.to_json(), ensure_ascii=False, indent=2) + "\n" if args.json else d.render()
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text)
        print("Wrote %s" % args.out)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
