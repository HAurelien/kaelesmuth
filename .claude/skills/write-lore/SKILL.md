---
name: write-lore
description: Add new lore to the Kaelesmuth vault, such as an event, a character, a place, an organization, a relationship, or new details on an existing note. Use whenever the user wants to write down something that happens or exists in their world.
---

# Write lore

The user describes something in their world; you turn it into notes that follow the vault's rules, after checking it against what the world looks like at that date.

Read `Schema.md` and `Vault conventions.md` once per session before writing. They are the rules; this skill is the workflow.

## 1. Pin down what is being added

From the user's words, work out:

- **What kind of note(s)**: an event, a new character, place, organization, a relationship between two characters, or details on an existing note. One story often means one event plus small edits elsewhere (a death year, a new residence).
- **When**: year and calendar (`aethernam` or `zephyrion`). Years before 0 are negative (120 PME is `-120`). A guess is fine (`approximate: true`). If nobody knows the year, it stays empty, and you ask whether it comes before or after an existing event so you can fill `after` / `before`.
- **Where**: the most precise place, its planet, or the Ether.
- **Who**: participants, and which of them already have notes.

Look the names up before creating anything: `python3 -c "import sys; sys.path.insert(0,'_tools'); from vault import Vault; v=Vault(); print(v.resolve('NAME'))"`. A name or alias that already exists means you extend that note, never create a second one.

If the date or place is missing and matters, ask once, briefly. Don't block on details the user doesn't know: empty is a valid answer.

## 2. Show the world at that date

Before writing, run the shared query with every participant and the place in focus:

```
python3 _tools/world_at.py YEAR --calendar CAL --focus "Character" --focus "Place"
```

Add `--window 20` (or more) when the surroundings matter over a longer stretch. Then read the text of the events just before and after for each participant, and their relationship notes, since mood and motives live in the text, not in the properties.

Give the user a short picture of that moment: who is alive and how old, where each participant was last seen, what just happened to them, what comes next, and how they feel about each other. Flag every conflict plainly, for example:

- a participant who is dead, not born yet, or "not recorded yet" at that date;
- a participant who is somewhere else at that time according to another event;
- a later event whose text contradicts the new one;
- an organization that doesn't exist yet or anymore.

Let the user decide how to resolve each conflict. Don't change existing lore on your own.

If calendars differ and the query says conversion isn't available yet, say that the two calendars can't be compared yet, so cross-planet timing is unchecked.

### Older dates across the two planets

Everything written before 2026-10-23 (the WorldAnvil import, the user's older notes, chats they paste) was built as if a Zephyrion year and an Aethernam year had the same length. They don't: one Zephyrion year is about 2.15 Aethernam years (see `Tools.md`). So older material can hide mismatches:

- durations on Zephyrion ("a century", "90 years later") may have been thought of in Aethernam-length years, and so be about twice too long once read in Zephyrion years;
- events that were meant to happen "at the same time" or "shortly after" on the two planets may no longer line up once converted;
- a Zephyrion date copied from older material may sit before or after an Aethernam event it was supposed to follow or precede.

Whenever new lore uses an older Zephyrion date or span, or links events on both planets, convert both ways (`world_at.py` prints the ≈ other-calendar year), check the order and gaps against the linked events on the other planet, and flag each mismatch to the user with the years in both calendars and a suggested fix (usually moving the less established date). Never rescale old dates on your own: the user decides. Example: on 2026-10-24 The Silence became 1669 to about 1745 in Zephyrion years, and Rimas's departure from Aethernam moved from 2849 to 2913, for this reason.

## 3. Write the notes

- Start from the template in `_templates/` (Character for gods too, with `type: god`). Keep every property the template has, even empty.
- Follow `Schema.md` exactly: years are numbers, precise dates are quoted text that agrees with the year, `calendar` is set whenever a year is, links in properties are quoted (`"[[Name]]"`).
- An event is written once, in `Events/`. Don't add it to timelines or to character notes by hand: its `timelines`, `participants` and `location` properties make it show up there.
- Family goes only in `parents` (on the child) and `partners` (on both). Membership only in `affiliations` on the character. Relationships are notes in `Relationships/` named "A and B". Never write `children`, `siblings`, `members` or `subsidiaries`.
- A property link must point to a note that exists. If the user mentions a new place or person, create a short note for it (status `idea`) or leave the property empty and link it in the text.
- `status` is `draft` unless the user says it's settled (`canon`).
- Write in the user's words and stay close to what they said. When you fill a gap (a motive, a consequence), say so in your answer and let them accept it rather than slipping it in as fact.
- The vault is private and writer-only: no spoiler markup. Never put the user's real name in a note.

## 4. Check

Run `python3 _tools/check_vault.py`. Fix every error before going on. For warnings, report those on the notes you touched (a participant after their death, a location on another planet...) and ask whether they're intended.

Then re-run `world_at.py` at the same date with the same focus and confirm the new event reads right in context.

## 5. Save

Show the user what you created or changed (file names and a line each). When they're happy, commit the changes with a message that says what was added (`git add` the notes, then `git commit`; the pre-commit hook runs the checker again). The commit can't be pushed from here, so remind the user to run `git push`.

If `_export/kaelesmuth.json` exists and you changed events, places or dates, offer to refresh it with the export-world skill.
