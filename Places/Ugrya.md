---
type: place
aliases: 
  - "Old Ugrya"
  - "Kingdom of Ugrya"
planet:
  - "[[Zephyrion]]"
place_type: Region
parent: "[[Kingdom of Istors]]"
owner: 
from: 
until: 
calendar: zephyrion
status: draft
tags: []
---

## Summary

A former kingdom, now part of the [[Kingdom of Istors]].

## Geography

Its border stopped at the mountain chain, east of [[Tutsana]]'s mines.

## History

Before the Silence it coveted the mines on its western border, in Tutsana, but the mountains discouraged open war. It secretly stirred the insurrections in western Tutsana instead, which everyone blamed on the west.

Held responsible for the Century of Silence, which the gods say is directly linked to the opening of the gates of the [[City of Oubralet]]. After the Silence, the failed rebuilding of Ugrya and [[Grueca]] gave rise to [[Oubralet]]. It later absorbed [[Eastern Tutsana]] by marriage, which made it the [[Kingdom of Istors]].

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
