---
type: place
aliases: 
  - "Main continent"
  - "Eastern continent"
planet:
  - "[[Aethernam]]"
place_type: Continent
parent: "[[Aethernam]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

The main continent of [[Aethernam]]: one of its two huge continents, east of the [[Western continent]], and the most developed. Home to [[Ithoria]], [[Jovinia]] and [[Calindor]]. Its real name isn't recorded yet.

It is also where the age of war took place, in the dark age before Absalom the First (the future [[God of Humankind]]) took power: [[StormHold]] and [[Sovnar]] are in its east.

## Geography

Snowy in the north and along its west coast. [[Ithoria]] covers most of it, with [[Jovinia]] on the north coast and [[Calindor]] in the south-east.

## History



## Notable places

- [[Ithoria]]
- [[Jovinia]]
- [[Calindor]]
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
