---
type: place
aliases: 
  - "Kingdom of Tostep"
planet:
  - "[[Aethernam]]"
place_type: Country
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

One of the richest countries in the world, known above all for its merchant power as an exporter of precious stones. A monarchy whose workforce is mostly slaves.

## Geography

Its lands in the west hold high-quality wood.

## History

### In the time of Alexendre X

Its ruler, Alexendre X, has lately been much talked about, mostly badly. Some say he is slowly losing his mind, but the monarchy still seems to be doing well.

The slave revolts at the start of the century were crushed, giving a second economic wind to the region's nobles and bourgeoisie. Its western wood has lately let it build transport ships said to rival those of [[Jovinia]].

It allied with [[Cliphetoristu]] against [[Thoear]], and now extends its influence over Thoear's lordships. See [[Fall of Thoear]].

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
