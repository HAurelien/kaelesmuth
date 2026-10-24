---
type: place
aliases: 
  - "Jovania"
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

A small country on the north coast of the [[Aethernam main continent]], with a crucial role in world politics. Renowned for producing the world's most advanced boats, for war and shipping; its traders are among the wealthiest in the world.

## Geography



## History

### In 1243

Its complex relationship with neighbouring [[Ithoria]] is central: its large navy serves as a buffer whenever tension rises between [[Tostep]] and Ithoria, which covets the rich mountains of its overseas neighbour.

Acting much like mercenaries, its naval forces keep piracy in check and deter less favourable offers from potential adversaries, which gives it diplomatic weight and keeps its waters stable.

### Around 1300 (time of Alexendre X)

Tostep's new transport ships rival Jovinia's.


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
