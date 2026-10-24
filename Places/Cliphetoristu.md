---
type: place
aliases: []
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

A country whose political landscape stays fairly obscure to foreigners.

## Geography

The west of the country is covered in desert, so its food depends heavily on fishing along the west coast and farming in the east.

## History

### Around 1100 (time of Alexendre X)

Its alliance with [[Tostep]] is starting to crumble as the country recovers from its intensive, exhausting war economy, now that [[Thoear]] has collapsed. See [[Fall of Thoear]].

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
