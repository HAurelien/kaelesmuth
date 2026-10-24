---
type: place
aliases: 
  - "Stormhold"
planet:
  - "[[Aethernam]]"
place_type: City
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

A very old city on a hill, often used as the capital of regional governments, and so reinforced several times with thick stone walls.

## Geography

On a hill, with the small forest of [[Iverald]] to the north and the sea to the east.

## History

### In the age of war

Life there is hard. Food shortages are common, and the only large source of drinking water becomes unreachable or polluted for days every year during the storm season. People then rely on wells dug inside the city, not enough for everyone, or on rainwater when it isn't carrying a strange reddish sand.

Fishing, the last source of food after herding and crops, varies a lot with the seasons and is very dangerous in the storm periods, when everything is already running out. Boats are expensive, and only the toughest sailors dare to leave the coast. Many of them never come back.

The [[Amtras clan]] wants a trade route to StormHold through [[Sovnar]].

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
