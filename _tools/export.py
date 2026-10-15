#!/usr/bin/env python3
"""Export the vault to one stable data file for the map and other tools.

    python3 _tools/export.py                  write _export/kaelesmuth.json
    python3 _tools/export.py --out FILE       somewhere else
    python3 _tools/export.py --force          export even when the checker finds errors

Tools read this file, never the notes, so the notes can change shape without
breaking them. The format is described in the "Tools" note at the vault root;
format_version only goes up when a change could break a reader (adding a
field doesn't count).

The export refuses to run while check_vault.py reports errors, so a tool
never receives data the vault's own rules reject. It prints which ids
appeared or disappeared since the previous export: a disappeared id usually
means a renamed note, which a map marker may still point to.
"""

import argparse
import datetime
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from vault import Vault  # noqa: E402
from world_at import World, PERSON_TYPES, body_text  # noqa: E402
import check_vault  # noqa: E402

FORMAT = "kaelesmuth-export"
FORMAT_VERSION = 1
DEFAULT_OUT = os.path.join("_export", "kaelesmuth.json")
GROUPS = {"character": "characters", "god": "characters", "event": "events", "place": "places",
          "organization": "organizations", "timeline": "timelines", "relationship": "relationships"}


def slug(text):
    t = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") or "note"


class Exporter:
    def __init__(self, vault):
        self.v = vault
        self.w = World(vault)
        self.ids = {}
        used = set()
        for n in sorted(vault.notes, key=lambda n: n.rel):
            if n.type == "meta":
                continue
            base = "%s/%s" % (slug(n.folder or "root"), slug(n.name))
            i, k = base, 2
            while i in used:
                i, k = "%s-%d" % (base, k), k + 1
            used.add(i)
            self.ids[n.rel] = i

    def id(self, note):
        return self.ids.get(note.rel)

    def refs(self, note, key):
        return [self.id(n) for n in self.w.links(note, key) if self.id(n)]

    def ref(self, note, key):
        r = self.refs(note, key)
        return r[0] if r else None

    def time(self, note):
        """The one shape every dated thing has in the export."""
        ts = self.v.type_schema(note.type)
        span = ts["span"] if ts else None
        if not span:
            return None
        s, e = self.v.span(note)
        cal = note.get("calendar") if (s is not None or e is not None) else None
        is_event = note.type == "event"
        if s is None and e is None:
            kind = "unknown"
        elif is_event and e == s:
            kind = "point"
        else:
            kind = "span"
        t = {
            "kind": kind, "calendar": cal, "start": s,
            "end": None if (is_event and e == s) else e,
            "start_date": note.get("date" if is_event else span["start"] + "_date"),
            "end_date": note.get("end_date" if is_event else span["end"] + "_date"),
            "approximate": note.get("approximate") is True,
            "in": {},
        }
        for c in self.w.cals.names:
            if cal is None or not self.w.cals.can_convert(cal, c):
                t["in"][c] = None
                continue
            lo = self.w.cals.convert(s, cal, c) if s is not None else None
            hi = self.w.cals.convert(e + 1, cal, c) if e is not None else None
            t["in"][c] = {"from": lo, "until": hi}
        if is_event:
            t["after"] = self.refs(note, "after")
            t["before"] = self.refs(note, "before")
        return t

    def place(self, note):
        """Where an event happened, in one of four shapes."""
        locs = self.w.links(note, "location")
        planets = self.w.note_planets(note)
        planet_ids = [self.id(self.v.resolve(p)) for p in planets if self.v.resolve(p)]
        if locs:
            if all(l in self.w.planets for l in locs):
                kind = "planet_only"
            elif not any(self.w.place_planets(l) for l in locs):
                kind = "off_planet"
            else:
                kind = "located"
        else:
            kind = "planet_only" if planet_ids else "unknown"
        return {"kind": kind, "locations": [self.id(l) for l in locs if self.id(l)], "planets": planet_ids}

    def base(self, n):
        return {"id": self.id(n), "name": n.name, "type": n.type, "file": n.rel,
                "aliases": [a for a in (n.get("aliases") or []) if isinstance(a, str)],
                "status": n.get("status"), "planets": [self.id(self.v.resolve(p)) for p in self.w.note_planets(n)
                                                       if self.v.resolve(p)],
                "wa_id": n.get("wa_id")}

    def run(self):
        out = {
            "format": FORMAT, "format_version": FORMAT_VERSION,
            "generated": datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
            "schema_version": self.v.schema.get("version"),
            "calendars": {c: {"planet": self.id(self.v.resolve(d["planet"])) if self.v.resolve(d["planet"]) else None}
                          for c, d in self.v.schema["calendars"].items()},
            "conversion": {"ready": self.w.cals.ready, "missing": self.w.cals.missing() or None},
            "places": [], "events": [], "characters": [], "organizations": [], "timelines": [],
            "relationships": [], "other": [],
        }
        for n in sorted(self.v.notes, key=lambda n: n.rel):
            if n.type == "meta" or n.parse_error:
                continue
            d = self.base(n)
            t = n.type
            if t == "place":
                d.update(place_type=n.get("place_type"), parent=self.ref(n, "parent"), owner=self.ref(n, "owner"),
                         time=self.time(n), is_planet=n in self.w.planets)
            elif t == "event":
                d.update(time=self.time(n), place=self.place(n), event_type=n.get("event_type"), era=n.get("era"),
                         participants=self.refs(n, "participants"), species=self.refs(n, "species"),
                         related=self.refs(n, "related"), timelines=self.refs(n, "timelines"),
                         text=body_text(n))
            elif t in PERSON_TYPES:
                d.update(time=self.time(n), importance=n.get("importance"), species=self.ref(n, "species"),
                         birthplace=self.ref(n, "birthplace"), residence=self.ref(n, "residence"),
                         realm=self.ref(n, "realm"), affiliations=self.refs(n, "affiliations"),
                         parents=self.refs(n, "parents"), partners=self.refs(n, "partners"),
                         conditions=self.refs(n, "conditions"), titles=n.get("titles") or [])
            elif t == "organization":
                d.update(time=self.time(n), org_type=n.get("org_type"), headquarters=self.ref(n, "headquarters"),
                         leaders=self.refs(n, "leaders"), founders=self.refs(n, "founders"),
                         parent_org=self.ref(n, "parent_org"), deities=self.refs(n, "deities"))
            elif t == "timeline":
                d.update(calendar=n.get("calendar"))
            elif t == "relationship":
                d.update(first=self.ref(n, "first"), second=self.ref(n, "second"),
                         **{k: n.get(k) for k in ("first_role", "first_attitude", "second_role", "second_attitude")})
            out[GROUPS.get(t, "other")].append(d)
        return out


def all_ids(data):
    return {x["id"]: x["name"] for k, v in data.items() if isinstance(v, list) for x in v if isinstance(x, dict) and "id" in x}


def main(argv=None):
    ap = argparse.ArgumentParser(description="Export the vault for the map and other tools.")
    ap.add_argument("--out", default=None, help="output file (default: _export/kaelesmuth.json in the vault)")
    ap.add_argument("--force", action="store_true", help="export even if the checker reports errors")
    ap.add_argument("--vault", default=None)
    args = ap.parse_args(argv)
    vault = Vault(args.vault) if args.vault else Vault()
    report = check_vault.run(vault)
    errors = [i for i in report.items if i["severity"] == "error"]
    if errors and not args.force:
        print("Not exported: the checker reports %d error(s). Run python3 _tools/check_vault.py to see them." % len(errors),
              file=sys.stderr)
        return 1
    data = Exporter(vault).run()
    out = args.out or os.path.join(vault.root, DEFAULT_OUT)
    before = {}
    if os.path.exists(out):
        try:
            with open(out, encoding="utf-8") as f:
                before = all_ids(json.load(f))
        except (ValueError, OSError):
            before = {}
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    tmp = out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, out)
    after = all_ids(data)
    counts = ", ".join("%d %s" % (len(v), k) for k, v in data.items() if isinstance(v, list))
    print("Exported %s: %s." % (os.path.relpath(out, vault.root), counts))
    if before:
        gone = sorted(set(before) - set(after))
        new = sorted(set(after) - set(before))
        if new:
            print("New ids: " + ", ".join(new))
        if gone:
            print("Ids gone since the last export (renamed or deleted notes; tools pointing at them need updating): "
                  + ", ".join(gone))
    if errors:
        print("Exported despite %d checker error(s) (--force)." % len(errors))
    return 0


if __name__ == "__main__":
    sys.exit(main())
