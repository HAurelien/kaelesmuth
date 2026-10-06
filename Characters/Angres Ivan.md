---
type: "character"
aliases: []
planet:
  - "[[Aethernam]]"
importance: "main"
calendar: "aethernam"
partners:
  - "[[Angres Adelaïde]]"
status: "canon"
tags: []
wa_id: "56386d31-deb6-4f83-9217-1e94cf0e95ec"
---

## Relationships
- [[Angres Ivan]] (Father (Vital)) ⇄ [[Angres Rimas]] (Child (Vital))
    - Angres Ivan → level -5 / -5, Subversive
    - Angres Rimas → level -5 / -5, Subversive
- [[Angres Ivan]] (Husband (Vital)) ⇄ [[Angres Adelaïde]] (Wife (Vital))
    - Angres Ivan → level 4 / 4, Honest
    - Angres Adelaïde → level 4 / 4, Honest
- [[Angres Emilie]] (Daughter (Vital)) ⇄ [[Angres Ivan]] (Father (Vital))
    - Angres Emilie → level 0 / 0
    - Angres Ivan → level 0 / 0

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
