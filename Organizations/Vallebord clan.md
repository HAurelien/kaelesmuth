---
type: organization
aliases: 
  - "Vallebord"
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

One of the two clans fighting over the village of [[Sovnar]], in the age of war.

## Purpose

## Structure

Very recently led by a man named Vallebord Straïs, son of Vallebord Laurem.

## History

Controls the village of [[Valmar]], between the wood of [[Calindor]] and the [[Frostjárnafjöll]] mountains, and uses it as a foothold against [[Naridor]].

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
