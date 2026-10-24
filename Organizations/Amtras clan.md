---
type: organization
aliases: 
  - "Amtras"
planet:
  - "[[Aethernam]]"
org_type: Clan
founded: 
dissolved: 
calendar: aethernam
headquarters: 
leaders: []
founders: []
parent_org: 
status: draft
tags: []
---

## Summary

The other clan fighting over the village of [[Sovnar]], in the age of war.

## Purpose

## Structure

Controls two of the three villages to the east.

## History

It tries to take Sovnar to open a trade route with [[StormHold]], hoping to solve the famines, since it enjoys fairly stable crops thanks to a very favourable microclimate south-east of the [[Frostjárnafjöll]] mountains.

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
