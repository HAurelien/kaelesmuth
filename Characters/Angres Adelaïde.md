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
