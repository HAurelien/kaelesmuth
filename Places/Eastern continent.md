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

The large continent east of the [[Aethernam main continent|main continent]] on the map, home to [[Ithoria]], [[Jovinia]] and [[Calindor]]. Its real name isn't recorded yet.

## Geography

Snowy in the north and along its west coast. [[Ithoria]] covers most of it, with [[Jovinia]] on the north coast and [[Calindor]] in the south-east.

## History



## Notable places

- [[Ithoria]]
- [[Jovinia]]
- [[Calindor]]

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
