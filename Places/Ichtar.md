---
type: place
aliases: 
  - "Kingdom of Ichtar"
planet:
  - "[[Aethernam]]"
place_type: Kingdom
parent: "[[Western continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

A kingdom in the north-east of the [[Western continent]]. Thanks to its alliance with [[Tostep]], it has the most formidable navy in the world and a significant land army.

## Geography

Between [[Cliphetoristu]] to the west, [[Thoear]] to the south and [[Tostep]] to the north-east.

## History

### In 1243

Ruled by Queen Sylsta, who governs while waiting for the heir to come of age and claim the throne. The king was assassinated a few months ago (see [[Assassination of the king of Ichtar]]), which badly weakened Ichtar and disrupted its chain of command, as the late king's cousin tries to seize the throne for himself.

It is winning its war against [[Cliphetoristu]] (see [[War between Ichtar and Cliphetoristu]]), sending armed groups to raid the east of that country. Queen Sylsta, despite her strategic advantage, has refrained from acting, and many doubt her ability to rule. [[Thoear]] is hostile to it.

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
