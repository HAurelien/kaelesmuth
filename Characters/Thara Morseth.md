---
type: character
aliases: []
planet:
  - "[[Aethernam]]"
importance: secondary
species: "[[Human]]"
sex: male
born: 
died: 
calendar: aethernam
birthplace: 
residence: 
affiliations: []
parents: []
partners: []
titles: 
  - "Leader of the eastern region of Cliphetoristu"
  - "Chosen one of Valzarr"
status: draft
tags: []
---

## Summary

The leader of the eastern region of [[Cliphetoristu]] since 1243, and the latest chosen one of [[Valzarr]] (since 1242).

## Appearance

## Personality

## History

Many believe that his being chosen by Valzarr and the [[Assassination of the king of Ichtar]] were no coincidence.

About a year ago he settled in a small village of about a hundred inhabitants (name not recorded yet), though he has spent no more than three months there since. His parents, his brother and his wife live there. They are all very well respected, and his wife almost runs the village while he is away, completely supplanting the village chiefs; whether that is for better or worse depends on whom you ask.

Recently, a small area was set up in the village for volunteers to gather and pray to Valzarr. A storage building was also converted to an unknown purpose: even the village administrators were refused entry, on his direct order. Rumour says only the [[Keepers of Valzarr|keepers]] and Thara Morseth himself may go in; no one else has ever been seen even trying.

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
