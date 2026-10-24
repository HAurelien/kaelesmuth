---
type: place
aliases: []
planet:
  - "[[Aethernam]]"
place_type: City
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: idea
tags: []
---

## Summary

A city that [[Valmar]] is a foothold to attack. In the age of war it attacked Valmar several times over a decade, without success.

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
