---
type: place
aliases: []
planet:
  - "[[Zephyrion]]"
place_type: City
parent: "[[Kingdom of Istors]]"
owner: 
from: 
until: 
calendar: zephyrion
status: draft
tags: []
---

## Summary

A big city, the second largest of the [[Kingdom of Istors]] (as of 1770). An older note ranks it second for trade and fourth for population in the country.

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
