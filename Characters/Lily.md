---
type: "character"
aliases:
  - "Littl'"
planet:
  - "[[Zephyrion]]"
importance: "secondary"
species: "[[Elementary]]"
calendar: "aethernam"
affiliations:
  - "[[Lone Protectors]]"
alignment: "Lawfull Neutral"
conditions:
  - "[[Bound]]"
residence: "[[Book of the traveler]]"
status: "draft"
tags: []
wa_id: "cd399892-46e9-4eab-a778-c714111a8356"
---

**Lily (a.k.a. Littl')**

Lily is an entity attached to the [[Book of the traveler]]. She is it's keeper since [[Dave Buns]] invoked her to protect the book's usage after finding it.

## Relationships

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "relationship"
    - file.hasLink(this.file)
views:
  - type: table
    name: Relationships
    order:
      - file.name
      - first
      - first_role
      - second
      - second_role
```

## Circumstances of Death

When [[Arrack]] retrieved the book, as Lily tried to prevent her from using it, she got annihilated.
