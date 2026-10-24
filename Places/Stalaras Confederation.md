---
type: place
aliases: 
  - "Confederation of Starala"
  - "Starala"
  - "Stalaras"
  - "Staralas"
planet:
  - "[[Aethernam]]"
place_type: Island
parent: "[[Aethernam]]"
owner: 
from: 
until: 
calendar: aethernam
status: idea
tags: []
---

## Summary

A relatively weak and unassuming confederation, stranded on a vast island in the south-west.

Around 1300 (time of Alexendre X of [[Tostep]]) only remnants of it are left, and they influence the lordships of [[Thoear]].

## Geography

A vast island, south-west of [[Thoear]].


## History

### In 1243

Its sparse population lives mainly from fishing and trades mostly with [[Thoear]]; [[Cliphetoristu]]'s southern region also trades with it in secret.

It is governed by a council of 20 members, elected every decade by a majority of the population. It recently drew the whole world's attention with a controversial law: the complete abolition of slavery across the island, called an "inhuman crime". Most of the world considers this regressive, and international opinion has united against it. See [[Abolition of slavery in the Stalaras Confederation]].


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
