"""Convert years between the planet calendars of Kaelesmuth.

Aethernam and Zephyrion orbit the same star and each counts years by its own
orbit, so one planet's year is a fixed number of the other's. The numbers
live in _tools/schema.json under "calendar_conversion":

    "calendar_conversion": {
      "year_length":  {"aethernam": 365.25, "zephyrion": 512.0},
      "orbit_radius": {"aethernam": null,   "zephyrion": null},
      "anchor":       {"aethernam": 2758,   "zephyrion": 1712}
    }

- year_length: each planet's year, in one shared unit (for example Aethernam
  days). Used when every calendar has one.
- orbit_radius: otherwise, each planet's distance to the star, in one shared
  unit. Kepler's third law gives the year lengths (a year grows as r^1.5
  around the same star).
- anchor: one moment written in every calendar (the start of a year that is
  known on both planets). It fixes where the counts line up.

Until an anchor and one of the two ratios are filled in, convert() returns
None between different calendars and tools only compare years within one
calendar. A year y covers [y, y + 1), so converted years are fractional.
"""


def _num(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


class Calendars:
    def __init__(self, schema):
        self.names = list(schema.get("calendars", {}))
        conv = schema.get("calendar_conversion") or {}
        self.anchor = {c: float(v) for c, v in (conv.get("anchor") or {}).items() if _num(v)}
        lengths = conv.get("year_length") or {}
        radii = conv.get("orbit_radius") or {}
        self.length = {}
        if self.names and all(_num(lengths.get(c)) and lengths[c] > 0 for c in self.names):
            self.length = {c: float(lengths[c]) for c in self.names}
            self.source = "year_length"
        elif self.names and all(_num(radii.get(c)) and radii[c] > 0 for c in self.names):
            self.length = {c: float(radii[c]) ** 1.5 for c in self.names}
            self.source = "orbit_radius"
        else:
            self.source = None

    @property
    def ready(self):
        """True when every pair of calendars can be converted."""
        return bool(self.length) and all(c in self.anchor for c in self.names)

    def missing(self):
        """What's needed before conversion works, in plain words ('' when ready)."""
        if self.ready:
            return ""
        parts = []
        if not self.length:
            parts.append("each planet's year length (or orbit radius)")
        if not all(c in self.anchor for c in self.names):
            parts.append("one moment dated in both calendars")
        return "calendar conversion needs " + " and ".join(parts) + " in _tools/schema.json (calendar_conversion)"

    def can_convert(self, src, dst):
        if src == dst:
            return True
        return all(c in self.length and c in self.anchor for c in (src, dst))

    def convert(self, year, src, dst):
        """A year (int or fractional) in calendar src, expressed in calendar dst."""
        if year is None:
            return None
        if src == dst:
            return year
        if not self.can_convert(src, dst):
            return None
        return self.anchor[dst] + (year - self.anchor[src]) * self.length[src] / self.length[dst]
