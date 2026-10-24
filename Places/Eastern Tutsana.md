---
type: place
aliases: 
  - "Tutsana Est"
  - "East Tutsana"
planet:
  - "[[Zephyrion]]"
place_type: Region
parent: "[[Kingdom of Istors]]"
owner: 
from: 
until: 
calendar: zephyrion
status: draft
tags: []
---

## Summary

The richest region of the old [[Tutsana]], now part of the [[Kingdom of Istors]].

## Geography



## History

The whole government of Tutsana sat here, including the capital. Its administration was responsible for the massacre of [[Miari]] during Western Tutsana's attempt to take power. Under pressure from [[Grueca]] it was split from Western Tutsana and merged by marriage with [[Ugrya]], forming the [[Kingdom of Istors]].

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
