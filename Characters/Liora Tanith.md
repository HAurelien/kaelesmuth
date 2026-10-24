---
type: character
aliases: []
planet:
  - "[[Aethernam]]"
importance: secondary
species: "[[Human]]"
sex: 
born: 
died: 
calendar: aethernam
birthplace: 
residence: 
affiliations: []
parents: []
partners: []
titles: 
  - "Leader of the southern region of Cliphetoristu"
status: draft
tags: []
---

## Summary

The leader of the southern region of [[Cliphetoristu]] since 1237, chosen by the population.

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
