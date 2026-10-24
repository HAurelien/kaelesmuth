---
type: organization
aliases:
  - "The keepers"
planet:
  - "[[Aethernam]]"
org_type: Religious
founded: 
dissolved: 
calendar: aethernam
headquarters: 
leaders: []
founders: []
parent_org: 
deities:
  - "[[Valzarr]]"
status: draft
tags: []
---

## Summary

"The keepers": those who were close to the previous chosen one of [[Valzarr]]. Only they know the process that decides whether someone has been chosen by Valzarr, which ensures the new chosen one is trustworthy.

## Purpose

## Structure

## History

### In 1243

Thara Morseth and the keepers are said to be the only ones allowed into a storage building converted to an unknown purpose, in the village where [[Thara Morseth]] lives.

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
