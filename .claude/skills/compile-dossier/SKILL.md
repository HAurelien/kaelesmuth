---
name: compile-dossier
description: Compile everything the Kaelesmuth vault knows about a character, place, organization, event, timeline or period, in date order, showing how things change across the span. Use when the user wants material for a book, a game, a scene or a summary of a stretch of their world's history.
---

# Compile a dossier

`_tools/compile.py` gathers the facts; your job is to pick the right subject and span, run it, then turn the result into what the user needs.

## 1. Subject and span

- A **note**: a character (a life or part of it), a place (with everything inside it, and on a planet everything on that planet), an organization (with its members), an event (with its participants and ten years around it), or a timeline.
- A **period**: a range of years, for the whole world or one planet.

Years are in a calendar; by default the subject's own. Years before 0 are negative or written like `120 PME`.

## 2. Run it

```
python3 _tools/compile.py "Angres Rimas" --out "_export/dossiers/Angres Rimas.md"
python3 _tools/compile.py "Angres Rimas" --from 2740 --to 2760 --out "_export/dossiers/Angres Rimas 2740-2760.md"
python3 _tools/compile.py --from 2740 --to 2760 --planet Aethernam --out "_export/dossiers/Aethernam 2740-2760.md"
```

Options: `--calendar zephyrion`, `--json` for a machine-readable version. `_export/` is generated and not committed, so a dossier is regenerated rather than edited. The user can open it in Obsidian.

The dossier contains: the subject's properties and text, family and relationships, an "Across the span" section (age and whereabouts at every step for a person, who appears or disappears for a place or period, member status for an organization), the chronology with the full text of every event, then the undated events and the ones in a calendar that can't be converted yet.

For a single moment rather than a span, `python3 _tools/world_at.py YEAR --focus "Name"` is the lighter tool.

## 3. Turn it into what the user asked for

Read the dossier, then give the user, depending on their goal:

- **For a book**: the arc across the span (what changes for the character, in order), the turning points, the people around them at each stage, and the open questions.
- **For a game or a scene**: the situation at the starting date (who is where, what just happened, what's at stake), the factions that exist, and the constraints the lore sets.
- **In every case**, the gaps: events without a date or place, people with no dates, contradictions between texts, places of other calendars that can't be placed. Offer to fill them with the write-lore skill.

Stick to what the notes say. When you infer something (a motive, a likely date), label it as an inference. Link the dossier file in your answer.
