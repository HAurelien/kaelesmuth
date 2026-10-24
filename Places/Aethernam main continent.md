---
type: place
aliases: 
  - "Main continent"
planet:
  - "[[Aethernam]]"
place_type: Continent
parent: "[[Aethernam]]"
owner: 
from: 
until: 
calendar: aethernam
status: idea
tags: []
---

## Summary

The main continent of [[Aethernam]]. Lore set here so far comes from the dark age, long before year 0.

## Geography

Has a south-eastern peninsula ([[Thoear]]).

## History



## Notable places

- [[Tostep]]
- [[Cliphetoristu]]
- [[Thoear]]
- [[Jovinia]]
- [[Starala]]
- [[StormHold]]
- [[Naridor]]
- [[Sovnar]]
- [[Valmar]]
- [[Frostjárnafjöll]]
- [[Calindor]]
- [[Iverald]]

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
