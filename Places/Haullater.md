---
type: place
aliases: []
planet:
  - "[[Zephyrion]]"
place_type: City
parent: "[[Zephyrion]]"
owner: 
from: 
until: 
calendar: zephyrion
status: draft
tags: []
---

## Summary

A big city, the second of its country for trade and the fourth for population (as of 1750).

## Geography

Straight west of the northern mountain chain of the [[Kingdom of Istors]].

## History



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
