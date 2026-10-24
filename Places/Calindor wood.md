---
type: place
aliases: 
  - "Wood of Calindor"
planet:
  - "[[Aethernam]]"
place_type: Forest
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: idea
tags: []
---

## Summary

A wood south of [[Valmar]], in the age of war. Probably the same land as the later theocracy of [[Calindor]], in the south-east of the same continent (to confirm).

## Geography



## History



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
