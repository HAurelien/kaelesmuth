---
type: place
aliases: 
  - "Isle of Maraha"
  - "Free Confederation of the Isle of Maraha"
  - "Confédération libre de l'île du Maraha"
planet:
  - "[[Zephyrion]]"
place_type: Island
parent: "[[Zephyrion]]"
owner: 
from: 
until: 
calendar: zephyrion
status: draft
tags: []
---

## Summary

The free confederation of the isle of Maraha: a chaotic assembly of many tiny chiefdoms whose leaders change with the wind.

## Geography

An island.

## History

Like [[Isrïl]], it is one of the two islands Grueca once ruled half-officially. It jumped at the chance offered by its neighbours' war (with [[Grueca]]) to win its own independence too.

### In 1770

Part of the island is still under Grueca's control.

With no clear leader and a nation torn at its heart, the battles are hard, and a collapse of this revolution in the coming years is seriously plausible, although the borders have been fairly stable lately.

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
