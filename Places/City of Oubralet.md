---
type: place
aliases: 
  - "Cité d'Oubralet"
planet:
  - "[[Zephyrion]]"
place_type: City
parent: "[[Oubralet]]"
owner: 
from: 
until: 
calendar: zephyrion
status: draft
tags: []
---

## Summary

The city guarded by the Deans of [[Oubralet]].

## Geography



## History

The gods judge the opening of its gates responsible for the catastrophes when magic appeared, and for the Century of Silence. See [[Opening of the gates of Oubralet]].

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
