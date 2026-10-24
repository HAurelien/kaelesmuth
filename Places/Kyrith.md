---
type: place
aliases: []
planet:
  - "[[Aethernam]]"
place_type: Fortified city
parent: "[[Cliphetoristu]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

A fortified city, the command centre of the eastern region of [[Cliphetoristu]], and always a very important place.

## Geography

Its impressive walls were built around a clean water source.

## History

### In 1243

Many troops and weapons pass through it on their way to the front, about every week, which makes it vital to the supply chain. Food arrives almost daily and is sent out to, or collected by, the other villages and major cities every few days. The city has many workshops, storage buildings and a fairly important medical centre.

In the last 20 years it has been besieged twice, for one month in 1235 and three months in 1237, and never taken, mostly thanks to its steady water supply (see [[Siege of Kyrith (1235)]], [[Siege of Kyrith (1237)]]).

The city itself is fairly poor compared to those of the south, which once opposed the eastern ones, but food, water and medicine have never been a problem. Life is a little easier here, all the more since the last siege, as the enemy has been pushed back quite far.

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
