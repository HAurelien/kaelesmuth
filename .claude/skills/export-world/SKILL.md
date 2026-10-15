---
name: export-world
description: Export the Kaelesmuth vault to the stable data file that the map viewer and other tools read (_export/kaelesmuth.json), and check that changes to the notes don't break those tools. Use when the user wants to refresh the map data, plug in a new tool, or asks whether a change broke the export.
---

# Export the world

Tools never read the notes. They read `_export/kaelesmuth.json`, which `_tools/export.py` builds. Its format is described in the `Tools` note at the vault root, under "Export format".

## Refresh the export

1. Run `python3 _tools/check_vault.py`. The export refuses to run while there are errors, so fix them first (with the user when a fix changes lore). Warnings don't block.
2. Run `python3 _tools/export.py`.
3. Report the counts it prints. If it lists **ids gone since the last export**, find which notes were renamed or deleted (`git log --stat -M` helps) and tell the user which tool references need updating, for example a map marker attached to a renamed place.
4. `_export/` is not committed; it is regenerated whenever needed.

`--force` exports despite checker errors. Use it only when the user asks.

## Plug in a new tool

- The tool reads the JSON only. Point it at `format_version`, and have it refuse versions it doesn't know.
- Every dated thing has the same `time` object, and every event the same `place` object, with a `kind` that covers the edge cases (unknown, approximate, span, planet only, off-planet). The tool must handle each kind, not just the common one.
- Ids look like `events/the-great-cataclysm`. They follow the note's folder and name, so renaming a note changes its id; step 3 above catches that.
- When the calendar conversion is filled in, `time.in` gives every dated thing in every calendar, which is what a map with a year slider should use.

## Change the format

Add a field in `_tools/export.py` and document it in the `Tools` note. Adding fields keeps `FORMAT_VERSION`. Renaming, removing or changing the meaning of a field is a breaking change: bump `FORMAT_VERSION`, document what changed, and tell the user which tools need updating. Run the export afterwards and commit the code and the note together; remind the user to `git push`.
