---
type: "character"
aliases:
  - "Rimas"
planet:
  - "[[Aethernam]]"
  - "[[Zephyrion]]"
importance: "main"
born: 2701
born_date: "2701-07-09"
calendar: "aethernam"
birthplace: "[[Aethernam]]"
affiliations:
  - "[[Lone Protectors]]"
parents:
  - "[[Angres Adelaïde]]"
  - "[[Angres Ivan]]"
titles:
  - "Duke of Aethernal."
conditions:
  - "[[Aura]]"
circumstances_of_birth: "[[Experiment 6012]]"
status: "canon"
tags: []
wa_id: "af21da05-4bc7-4e74-814b-86e085ce018e"
---

![[76cc8556178ab2df850b41836a78142e.png]]

**Rimas**

Rimas is one of the most important characters in Kaelesmuth.
He has a timeline related to him : Rimas
He is one of the [[Lone Protectors]]
He is actually dead since his very young age, even tho no one understoods it except [[Arrack]] as only his parents really knew what their experiment was.

## Mental characteristics

### Personal history

A long, long story, not fully in this website yet.

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

## Timeline
- [[Rimas timeline]]

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
