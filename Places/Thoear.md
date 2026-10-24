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

A kingdom now crushed onto the south-eastern peninsula of the continent, and tearing itself apart.

## Geography

The south-eastern peninsula of the [[Aethernam main continent|main continent]].

## History

### Around 1100 (time of Alexendre X)

The lordships are gaining more and more weight under the influence of [[Tostep]] and of what remains of the confederation of [[Starala]]. The army, with no reinforcements at all, can no longer hold the hierarchy together, and the legitimacy of Uril III and his line is wavering. See [[Fall of Thoear]].

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
