---
type: god
aliases: []
planet:
  - "[[Aethernam]]"
importance: secondary
species: 
sex: male
born: 
died: 
calendar: aethernam
birthplace: 
residence: 
affiliations: []
parents: []
partners: []
titles: []
divine_classification: 
realm: 
status: draft
tags: []
---

## Summary

The god worshipped only by the people of [[Cliphetoristu]]. Legend says that in times of dire need, Valzarr watches over his believers.

## Appearance

## Personality

## History

No temple has ever been built for him, as he wants none. Nothing is written about him either: his words are spread by a few chosen ones among the leaders, every few generations. The latest touched by his grace is [[Thara Morseth]], leader of the eastern region, chosen in 1242.

Who has been chosen is determined by a process known only to the [[Keepers of Valzarr]], those who were close to the previous chosen one, which ensures the new one is trustworthy.

Legends say some leaders stopped armies of thousands single-handedly. In exchange for his guidance and blessing, Valzarr expects only the highest respect from his followers and two heartfelt prayers a day, one at sunrise and one at sunset.

## Relationships


```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "relationship"
    - file.hasLink(this.file)
views:
  - type: table
    name: Relationships
    order:
      - file.name
      - first
      - first_role
      - second
      - second_role
```

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
