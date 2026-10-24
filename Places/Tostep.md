---
type: place
aliases: 
  - "Kingdom of Tostep"
planet:
  - "[[Aethernam]]"
place_type: Country
parent: "[[Western continent]]"
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

A mountainous peninsula surrounded by water, north-east of [[Ichtar]]. Its lands in the west hold high-quality wood.

## History

### In 1243

Like most countries in this world, the kingdom is led by a king, Alexender VII. Allied with [[Ichtar]], it is known as one of the richest in the world, with a blossoming economy yet almost no army: its mountains surrounded by water and the powerful navy of Ichtar make it a natural fortress.

It is also where the reported death rate of slaves is highest: the mines are extremely profitable for their owners but dangerous to work in. [[Ithoria]] covets its rich mountains, and [[Jovinia]]'s navy acts as a buffer between them; slaves from [[Calindor]] reach Tostep through Ithoria.

### Around 1300 (time of Alexendre X)

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
