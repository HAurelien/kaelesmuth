---
type: "character"
aliases: []
planet:
  - "[[Aethernam]]"
  - "[[Zephyrion]]"
importance: "main"
species: "[[Ether mirror]]"
sex: "Female"
calendar: "aethernam"
status: "draft"
tags: []
wa_id: "4f616a67-8eb4-4220-836b-53a02dab57ac"
---

Arrack "The world eater".
She is the person who destroyed Aethernam during the Great Cataclysm.
She came from another star system, from a much more advanced civilisation, through the [[Pillar]]s and the [[Ether]], and almost dissolved in its corrosive mana on the way. In the Ether she absorbed several gods, and with their knowledge and power she cursed [[Aethernam]] to force the gods to let her back in and finish eating them. See [[Magic]].

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
