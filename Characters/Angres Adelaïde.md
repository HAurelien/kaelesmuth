---
type: "character"
aliases:
  - "Angres"
planet:
  - "[[Aethernam]]"
importance: "main"
species: "[[Human]]"
sex: "Female"
gender: "Woman"
died: 2757
died_date: "2757-07"
calendar: "aethernam"
partners:
  - "[[Angres Ivan]]"
status: "canon"
tags: []
wa_id: "5c66bed6-0c3b-41e8-98c9-272896b6a481"
---

**Angres**

## Relationships
- [[Angres Adelaïde]] (Mother (Vital)) ⇄ [[Angres Rimas]] (Child (Vital))
    - Angres Adelaïde → level -4 / -4, Subversive
    - Angres Rimas → level -5 / -5, Subversive
- [[Angres Ivan]] (Husband (Vital)) ⇄ [[Angres Adelaïde]] (Wife (Vital))
    - Angres Ivan → level 4 / 4, Honest
    - Angres Adelaïde → level 4 / 4, Honest
- [[Angres Emilie]] (Daughter (Vital)) ⇄ [[Angres Adelaïde]] (Mother (Vital))
    - Angres Emilie → level 0 / 0
    - Angres Adelaïde → level 0 / 0

## Events

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "event"
    - file.hasLink(this.file)
views:
  - type: table
    name: Events
    order:
      - file.name
      - year
      - event_type
      - timelines
    sort:
      - property: year
        direction: ASC
```
