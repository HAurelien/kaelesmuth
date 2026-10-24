---
type: place
aliases: []
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

One of the two huge continents of [[Aethernam]], west of the [[Aethernam main continent|main continent]]. Less developed than the main continent.

## Geography

The western of the two huge continents on the map ![[Aethernam countries 1243.png]]

Desert in the west ([[Cliphetoristu]]), [[Ichtar]] in the north-east, [[Thoear]] in the south, and the mountainous peninsula of [[Tostep]] to the north-east.

## History



## Notable places

- [[Tostep]]
- [[Ichtar]]
- [[Kyrith]]
- [[Cliphetoristu]]
- [[Thoear]]

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
