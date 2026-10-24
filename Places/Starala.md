---
type: place
aliases: 
  - "Confederation of Starala"
planet:
  - "[[Aethernam]]"
place_type: Confederation
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: idea
tags: []
---

## Summary

A confederation of which only remnants are left around 1100, in the time of Alexendre X of [[Tostep]]. Those remnants influence the lordships of [[Thoear]].

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
