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

The eastern part of the old [[Tutsana]], across the desert from the west. It holds the mines of the east and south, guarded on the [[Ugrya]] side by imposing mountains. [[Haullater]] lies here, west of the mountain chain.


## History

The whole government of Tutsana sat here, including the capital and King Istors (later remembered as Istors I, last king of Tutsana). Before the Silence it was better armed and richer than the west, which it ruled through intendants. Its administration was responsible for the massacre of [[Miari]] during Western Tutsana's attempt to take power. Under pressure from [[Grueca]] it was split from Western Tutsana and merged by marriage with [[Ugrya]], forming the [[Kingdom of Istors]].

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
