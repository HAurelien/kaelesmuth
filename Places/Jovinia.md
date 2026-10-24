---
type: place
aliases: []
planet:
  - "[[Aethernam]]"
place_type: Country
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: idea
tags: []
---

## Summary

A country known for its transport ships, which [[Tostep]]'s new ships now rival.

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
