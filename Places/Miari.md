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

A city massacred by the administration of [[Eastern Tutsana]] during Western Tutsana's attempt to take power.

## Geography



## History

See [[Tutsana slave revolt]].

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
