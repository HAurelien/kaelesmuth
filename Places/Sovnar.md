---
type: place
aliases: []
planet:
  - "[[Aethernam]]"
place_type: Village
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

A small village north of [[StormHold]], in the east of the continent, prey to frequent fighting between two clans, the [[Vallebord clan]] and the [[Amtras clan]].

## Geography



## History

### In the age of war (before Absalom the First)

The Amtras clan wants it to open a trade route to [[StormHold]]; the Vallebord clan disputes it.

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
