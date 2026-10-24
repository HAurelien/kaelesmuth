---
type: place
aliases: 
  - "Forest of Iverald"
planet:
  - "[[Aethernam]]"
place_type: Forest
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: idea
tags: []
---

## Summary

A small forest north of [[StormHold]].

## Geography



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
