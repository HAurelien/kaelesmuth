---
type: place
aliases: []
planet:
  - "[[Aethernam]]"
place_type: Village
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

A village held by the [[Vallebord clan]]. Its people are particularly hardened.

## Geography

Between the wood of [[Calindor wood]] to the south and the [[Frostjárnafjöll]] mountain chain to the north. The area is rich in ore, and its geography makes it hard to take.

## History

### In the age of war (before Absalom the First)

A solid foothold to attack the city of [[Naridor]]. It pushed back several attacks from Naridor during the last decade.

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
