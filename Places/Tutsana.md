---
type: place
aliases: 
  - "Tutsana Ouest"
  - "Western Tutsana"
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

A country in the north-west where life is now fairly good. It is governed by an assembly elected every ten years. Poorer than Istors, but free, and it has the food: large farmlands, which is no accident, since that is where all the slaves were.

## Geography

In the north-west. Large agricultural lands.

## History

Before magic appeared, this region of the world was mostly made of slaves, ruled from [[Eastern Tutsana]] by the Istors dynasty. Their rebellion was helped by the gods during the Century of Silence (see [[Tutsana slave revolt]]). There were few survivors, which is why its population is still small compared to the rest of the world.

Under pressure from [[Grueca]], Tutsana was split: the west became today's Tutsana, and the east joined [[Ugrya]] as the [[Kingdom of Istors]].

### In 1770

Its large farmlands recently let it negotiate a peace with Grueca that it hopes will last. Apparently there are no more slaves in Tutsana. Rumours say it is allied with [[Isrïl]], helping the confederation feed its people.

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
