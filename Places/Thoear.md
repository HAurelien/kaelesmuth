---
type: place
aliases: 
  - "Kingdom of Thoear"
planet:
  - "[[Aethernam]]"
place_type: Kingdom
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

A kingdom in the south of the [[Aethernam main continent|main continent]]. A relatively poor sovereignty with a modest army in 1243; around 1100 (time of Alexendre X) it is crushed onto its peninsula and tearing itself apart.

## Geography

The south-eastern peninsula of the [[Aethernam main continent|main continent]].

## History

### In 1243

Hostile to both [[Cliphetoristu]] and [[Ichtar]], it is focused on fortifying its defences: King Jaratak II fears the conflict in the north might reach its borders.

It trades a lot with [[Tostep]], the [[Stalaras Confederation]] and [[Halmea]]; Cliphetoristu's southern region also trades with it in secret. Efforts to open a reliable trade route with [[Ithoria]] have been halted for some time, because the sea there is too treacherous for current ships.

Its food production is often disrupted by natural disasters, but recent advances in agricultural research have greatly improved it, and the population is growing fast.

### Around 1100 (time of Alexendre X)

The lordships are gaining more and more weight under the influence of [[Tostep]] and of what remains of the confederation of [[Stalaras Confederation]]. The army, with no reinforcements at all, can no longer hold the hierarchy together, and the legitimacy of Uril III and his line is wavering. See [[Fall of Thoear]].

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
