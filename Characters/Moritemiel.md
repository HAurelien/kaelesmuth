---
type: "character"
aliases:
  - "Moritemiel Rianthurin"
  - "Mori"
planet: []
importance: "secondary"
calendar: "aethernam"
affiliations:
  - "[[Lone Protectors]]"
status: "draft"
tags: []
wa_id: "7069a561-bae6-4136-b49b-3925d8002d0a"
---

**Moritemiel Rianthurin (a.k.a. Mori)**

One of the latest member of the [[Lone Protectors]]
Current owner of the "Book of the traveller"

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
