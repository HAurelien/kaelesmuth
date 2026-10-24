---
type: place
aliases: 
  - "Istors"
  - "Royaume d'Istors"
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

A young, warlike kingdom, ruled by the Istors family, formerly the dynasty that reigned over [[Tutsana]] before the Century of Silence. It holds every one of the biggest mines of the continent.

## Geography

Made of the old kingdom of [[Ugrya]], whose border stopped at the mountain chain, and [[Eastern Tutsana]], the richest region of the old Tutsana. A mountain chain runs through its north; [[Haullater]], the kingdom's second largest city, lies straight west of it.

## History

Founded recently (before 1770), when [[Grueca]] forced the split of Western and Eastern Tutsana and Eastern Tutsana was absorbed into Ugrya by marriage. See [[Founding of the Kingdom of Istors]].

Each half carries a heavy past. The old Ugrya is held responsible for the Century of Silence, which the gods say is directly linked to the opening of the gates of the [[City of Oubralet]]. Eastern Tutsana was the seat of Tutsana's administration, responsible among other things for the massacre of [[Miari]] during Western Tutsana's attempt to take power.

### In 1770

Because the kingdom has monopolised the continent's biggest mines since the alliance, the other countries fear a rise in the price of rare metals, so despite its warlike nature it still seems to have many days ahead of it.

Life is not rosy for everyone: most of the population are slaves, many of them in the mines, and the paranoia of Istors I, last king of Tutsana, still holds among the region's nobles. It inherited Tutsana's dictatorship and has not lost the old habits.

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
