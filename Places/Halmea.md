---
type: place
aliases: []
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

A land in chronic instability. For the past two decades no government has kept control for long, leaving widespread anarchy in which many small clans fight for power.

## Geography

An island south of the [[Eastern continent]], with permafrost in its western regions and no mineral resources, which makes it unattractive to invaders.

## History

### In 1243

It trades with [[Thoear]].

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
