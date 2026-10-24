---
type: place
aliases: []
planet:
  - "[[Aethernam]]"
place_type: Theocracy
parent: "[[Aethernam main continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

The remnant of a once formidable theocracy, devoted to a long-forgotten deity called the "god of mankind" (presumably the [[God of Humankind]]). Now in decline, torn by internal strife and derision, and undermined by decades of greed and folly.

## Geography

The south-east of the [[Aethernam main continent]], next to [[Ithoria]].

## History

### In 1243

The people are heavily exploited, many living almost as slaves under the high priests, who command fortified cities that were once prosperous and are now steeped in fear and distrust of their neighbours.

Its priests control or influence much of [[Havland]]. Its slaves go to [[Tostep]] through [[Ithoria]], which has bought the Calindor provinces that could no longer keep up their production of slaves.

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
