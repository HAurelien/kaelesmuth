---
type: place
aliases: []
planet:
  - "[[Aethernam]]"
place_type: Archipelago
parent: "[[Aethernam]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

An archipelago with no clear central leader, largely influenced or controlled by priests from [[Calindor]].

## Geography

East of the [[Aethernam main continent]].

## History

### In 1243

It has no significant mineral resources; its economy lives on enslaving and selling its own population, with strict quotas so that the manpower is spread around the world.

Lately, rumours of slavery being abolished in a foreign nation (the [[Stalaras Confederation]]) have set many islands alight with freedom movements, some actively looking for sea routes to the neighbouring confederations in hope of a better future. A few of its islands trade in secret with [[Cliphetoristu]]'s southern region.

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
