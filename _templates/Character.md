---
type: character
aliases: []
planet: []
importance: 
species: 
sex: 
born: 
died: 
calendar: aethernam
birthplace: 
affiliations: []
parents: []
partners: []
titles: []
status: draft
tags: []
---

## Summary

## Appearance

## Personality

## History

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
