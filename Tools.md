---
type: meta
tags: []
---

# Tools

Scripts and Claude skills built on the vault. They all read the notes through `_tools/vault.py` and follow [[Schema]], so they agree with each other and with the checker.

## Skills

Open Claude Code in this folder and ask in plain words; the skills live in `.claude/skills`.

- **write-lore**: add an event, a character, a place... It first shows the world at that date (who is alive, ages, where everyone is, what just happened), flags contradictions, writes the notes from the templates, runs the checker and commits.
- **compile-dossier**: everything about a character, place, organization, event, timeline or period, in date order, with how things change across the span. For books, games and scenes.
- **export-world**: refreshes the data file the map and other tools read.

## Scripts

Run from the vault folder.

| Command | What it does |
|---|---|
| `python3 _tools/check_vault.py` | Checks the vault against the schema. Runs before every commit. |
| `python3 _tools/world_at.py 2758 --focus "Angres Rimas"` | The world at a year: who is alive and how old, where they are, events now, recent and upcoming, per planet. `--calendar`, `--planet`, `--window`, `--json`. |
| `python3 _tools/compile.py "Angres Rimas" --from 2740 --to 2760` | A dossier. Without a name, `--from`/`--to` give a period. `--out` writes it to a file. |
| `python3 _tools/export.py` | Writes `_export/kaelesmuth.json`. Refuses while the checker reports errors. |

`_export/` holds generated files (the export, dossiers). It isn't committed: regenerate instead of editing.

## Calendars

Both planets orbit a Sun-like star inside its habitable zone, and each counts years by its own orbit. The numbers are in `_tools/schema.json` under `calendar_conversion`, and every tool converts with them.

| Planet | Size | Distance to the star | Year | In Earth days |
|---|---|---|---|---|
| [[Aethernam]] | 0.8 Earth | 0.9 AU (inner) | 0.854 Earth years | about 312 |
| [[Zephyrion]] | 1.1 Earth | 1.5 AU (outer) | 1.837 Earth years | about 671 |

So one Zephyrion year is about 2.15 Aethernam years. At their closest the planets are 0.6 AU apart, farther than Mars ever comes to Earth, and the inner planet only ever turns its night side toward the outer one when it sits close to the star in the sky. Neither can make out the other's cities with early telescopes; radio is the first real sign, from the mid 1900s on.

The two counts are lined up by one anchor: Zephyrion 1712 starts at Aethernam 2850, when Rimas reaches Zephyrion just after leaving Aethernam in 2849. Change the anchor in `schema.json` if the story places that moment differently.

## Export format

`_export/kaelesmuth.json`, version 1. Tools read this file, never the notes. `format_version` changes only when a change could break a reader; new fields can appear at any time.

Top level: `format` ("kaelesmuth-export"), `format_version`, `generated`, `schema_version`, `calendars` (calendar → its planet's id), `conversion` (`ready`, `missing`), and one list per kind: `places`, `events`, `characters` (gods included, `type` tells them apart), `organizations`, `timelines`, `relationships`, `other` (species, conditions, items, languages).

Every entry has `id`, `name`, `type`, `file`, `aliases`, `status`, `planets` (ids) and `wa_id`. Links to other notes are ids. An id is the folder and the name in lowercase with dashes (`events/the-great-cataclysm`), so renaming a note changes its id; the export lists ids that disappeared since the previous run.

**`time`** (events, characters, organizations, places):

| Field | Meaning |
|---|---|
| `kind` | `point` (an event within one year), `span` (has a start and/or an end), `unknown` (no year at all) |
| `calendar` | calendar of `start` and `end`, null when unknown |
| `start`, `end` | years as written in the note (end included). Either can be null: an open start or end. A point has `end` null. |
| `start_date`, `end_date` | the precise dates when known (`"2758-01-01 01:00"`) |
| `approximate` | true when the years are a best guess |
| `in` | for each calendar, `{"from", "until"}`: the same span in that calendar's years, as numbers where a year y covers y to y + 1 (`until` excluded). Null when it can't be converted yet. This is what a year slider should use. |
| `after`, `before` | events only: ids of events this one comes after or before, to order undated events |

**`place`** (events only):

| `kind` | Meaning |
|---|---|
| `located` | `locations` lists the precise places |
| `planet_only` | only the planet is known: `locations` is the planet, or empty with `planets` set |
| `off_planet` | in the Ether or another place on no planet |
| `unknown` | no place at all |

`planets` lists the event's planet ids in every case.

Other fields by kind: places have `place_type`, `parent`, `owner`, `is_planet`; events have `event_type`, `era`, `participants`, `species`, `related`, `timelines`, `text`; characters have `importance`, `species`, `birthplace`, `residence`, `realm`, `affiliations`, `parents`, `partners`, `conditions`, `titles`; organizations have `org_type`, `headquarters`, `leaders`, `founders`, `parent_org`, `deities`; relationships have `first`, `second` and their roles and attitudes.

Places don't have map coordinates yet; those will be added when the map is built.
