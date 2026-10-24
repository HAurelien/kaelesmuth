---
type: place
aliases: 
  - "Deans of Oubralet"
  - "Les doyens d'Oubralet"
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

The country of the Deans of Oubralet, charged with guarding the [[City of Oubralet]].

## Geography

Its borders are extremely well guarded.

## History

A country with no origin, born from the inability to manage the rebuilding of [[Grueca]] and the old kingdom of [[Ugrya]], and from the will of the gods. Little is known about it since its creation, apart from the fact that it guards the City of Oubralet.

### In 1770

It doesn't make many waves. It keeps fairly cordial exchanges with its neighbours, stays far from conflicts and is, people suppose, under the protection of the gods. The exact makeup of its government and the shape of its political system remain fairly unclear to the rest of the world.

## Notable places

- [[City of Oubralet]]

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
