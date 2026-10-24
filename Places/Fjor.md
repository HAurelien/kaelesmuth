---
type: place
aliases: 
  - "Fish-shaped island"
planet:
  - "[[Aethernam]]"
place_type: Island
parent: "[[Aethernam]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

The fish-shaped island. Little is known about it, because of its sparse population and limited resources; only a few boats visit it each year.

## Geography

A small island in the south-east of the map.

## History

### In 1243

King Albert III, liked by the population, has ruled for a long time, from a line loved for generations, which suggests a stable lineage. Though seen as poor, the island is known for its peaceful way of life and is a tranquil place to live.

## Notable places



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
