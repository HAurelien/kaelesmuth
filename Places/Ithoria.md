---
type: place
aliases: 
  - "Itthora"
  - "Kingdom of Ithoria"
planet:
  - "[[Aethernam]]"
place_type: Kingdom
parent: "[[Eastern continent]]"
owner: 
from: 
until: 
calendar: aethernam
status: draft
tags: []
---

## Summary

By far the most populous and largest kingdom. Its power is centralised in its vast capital, once a fortress and now a cosmopolitan hub renowned for its advances in art and science.

## Geography

Covers most of the [[Eastern continent]]. Rich mines in the north; fertile fields in its greener regions. [[Jovinia]] lies on its north coast and [[Calindor]] to the south-east.

## History

### In 1243

King Simon VI has ruled for over three decades; as he ages, his succession is being prepared.

The rich mines discovered in the north let it produce the highest-quality metals, drawing renowned blacksmiths from all over the world. It covets the mountains of [[Tostep]], overseas.

Slavery is a pillar of its wealth: it is the transit point for slaves from [[Calindor]] to Tostep, and it has bought Calindor provinces that could no longer keep up their production of slaves. It holds the planet's second-largest slave population, who work its fertile fields. [[Thoear]]'s attempts at a trade route with it have stalled because of the treacherous sea.

## Notable places

- Its capital (name not recorded yet)

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
