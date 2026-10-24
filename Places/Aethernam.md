---
type: "place"
aliases: []
planet:
  - "[[Aethernam]]"
calendar: "aethernam"
place_type: "Planet"
parent: "[[Kaelesmuth]]"
owner: "[[Lone Protectors]]"
status: "draft"
tags: []
wa_id: "1059c8c4-3f3f-4939-a684-45ca458cd15b"
---

Aethernam is a planet which was mostly populated by [[Human]]. But after The Great Cataclysm, it turned to a pile of dust, and only a few survives in a world cursed by the World Eater [[Arrack]].

## Maps

![[Aethernam map.png]]

Countries in 1243:

![[Aethernam countries 1243.png]]

## Timeline
- [[Aethernam main timeline]]

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
