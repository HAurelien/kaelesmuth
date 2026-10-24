---
type: place
aliases: []
planet:
  - "[[Aethernam]]"
place_type: Mountain range
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: idea
tags: []
---

## Summary

A mountain chain north of [[Valmar]].

## Geography

South-east of the chain lies a very favourable microclimate with fairly stable crops, which the [[Amtras clan]] benefits from.

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
