---
type: "character"
aliases: []
planet: []
importance: "secondary"
species: "[[Human]]"
sex: "Female"
gender: "Woman"
calendar: "aethernam"
affiliations:
  - "[[Lone Protectors]]"
parents:
  - "[[Angres Adelaïde]]"
  - "[[Angres Ivan]]"
status: "canon"
tags: []
wa_id: "d0f17564-55c0-48bd-91c0-4b2783cef3fd"
---

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
