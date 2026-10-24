---
type: place
aliases: 
  - "Free Confederation of Isrïl"
  - "Confédération libre d'Isrïl"
  - "Isril"
planet:
  - "[[Zephyrion]]"
place_type: Country
parent: "[[Zephyrion]]"
owner: 
from: 
until: 
calendar: zephyrion
status: draft
tags: []
---

## Summary

The free confederation of the two main native clans, Astaril in the north and Outragonout in the south. Fairly well organised, and quickly gaining ground on [[Grueca]] these last years.

## Geography

Not very fertile land.

## History

### In 1750

Rumours speak of an alliance with [[Tutsana]] that lets it keep its population fed despite its poor land. The people strongly support the freedom the two leaders decided to take, and the leaders are said to often be on the battlefield themselves.

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
