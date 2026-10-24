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

The main continent of [[Aethernam]]. Lore set here so far comes from two periods: the age of war in the dark age, before Absalom the First (the future [[God of Humankind]]) took power, and the kingdoms of around 1100, in the breakthrough era.

## Geography

The western of the two large landmasses on the map ![[Aethernam countries 1243.png]]

Desert in the west ([[Cliphetoristu]]), [[Ichtar]] in the north-east, [[Thoear]] in the south, and the mountainous peninsula of [[Tostep]] to the north-east.

## History



## Notable places

- [[Tostep]]
- [[Ichtar]]
- [[Kyrith]]
- [[Cliphetoristu]]
- [[Thoear]]
- [[StormHold]]
- [[Naridor]]
- [[Sovnar]]
- [[Valmar]]
- [[Frostjárnafjöll]]
- [[Calindor wood]]
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
