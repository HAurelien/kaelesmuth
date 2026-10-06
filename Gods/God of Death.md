---
type: "god"
aliases: []
planet:
  - "[[Aethernam]]"
  - "[[Zephyrion]]"
species: "[[Ether mirror]]"
calendar: "aethernam"
affiliations:
  - "[[Lower gods]]"
realm: "[[Ether]]"
status: "canon"
tags: []
wa_id: "b99047c8-69d9-4a23-ae37-511c695fbfa6"
---

The God of Death is actually the first non-person God. He is one of the main supports of the [[Lone Protectors]] against [[Arrack]], as he came from the strong believe the survivors of the cataclysm had for the foretold hero that would one day free them from their fate, [[Angres Rimas]]

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
