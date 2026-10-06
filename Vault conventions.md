---
type: meta
tags: []
---

# Vault conventions

## World

Kaelesmuth is the world; [[Aethernam]] and [[Zephyrion]] are planets in it, and the [[Ether]] is a plane of it.

## Folders

One folder per kind of note: Characters, Gods, Places, Organizations, Species, Conditions, Items, Languages, Events, Relationships, Timelines. Which planet a note belongs to is the `planet` property, not the folder. Importance (main, secondary, key) is the `importance` property.

## Templates

Templates live in `_templates`: Character, Place, Organization, Event, Relationship. Gods use the Character template with `type: god`. Every note has a `type`, which is what the lists on [[Kaelesmuth World]] are built from.

## Dates

- Years are plain numbers: `born: 2701`, `year: 2758`. Years before 0 (PME) are negative: 1 PME is `-1`.
- A more precise date goes next to it as text: `born_date: "2701-07-09"`, `date: "2758-01-01 01:00"`.
- Every dated note says which calendar it uses: `calendar: aethernam` or `calendar: zephyrion`. The two are not converted yet (see [[Backlog]]).
- Leave a field empty when it's unknown.
- [[Schema]] has the exact rules for every kind of note, including spans, approximate and unknown dates, and how an event's place is written. `_tools/check_vault.py` checks them before every commit.

## Events

Each event is its own note in `Events`. It lists its `participants`, `location`, `species`, `related` notes and the `timelines` it belongs to. Timelines and the "Events" section of every note are lists that fill themselves from those links, so an event is only ever written once.

## Links

Links in properties are written in quotes: `species: "[[Human]]"`, `affiliations: ["[[Lone Protectors]]"]`.

**Family links** go only on the child: `parents: ["[[Angres Ivan]]", "[[Angres Adelaïde]]"]`, plus `partners` on both partners. Children and siblings are worked out from `parents`, so they are never typed by hand and can't drift out of sync. A family tree is drawn from these properties.

**Relationships** between two characters (friendship, rivalry, how family members feel about each other) are one note each in `Relationships`, named "A and B". The note holds each side's role, importance, attitude and honesty, plus the shared history. Both characters' "Relationships" sections list it automatically, so it is never written on the characters themselves. Family structure still lives in `parents` and `partners`.

**Membership** is written once, on the character (`affiliations`), never as a member list on the organization. The organization's member list is a query over `affiliations`.

**Organization hierarchy** is written only on the sub-organization (`parent_org`), never as a `subsidiaries` list on the parent. **Worship** is written only on the organization (`deities`), not on the god.

## Status

`status` is `idea`, `draft` or `canon`.
