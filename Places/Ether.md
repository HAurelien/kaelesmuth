---
type: "place"
aliases: []
planet: []
calendar: "aethernam"
place_type: "Plane of Existence"
parent: "[[Kaelesmuth]]"
owner: "[[Lower gods]]"
included_organizations:
  - "[[Higher gods]]"
  - "[[Lower gods]]"
status: "draft"
tags: []
wa_id: "ac16903b-87b8-4f7b-9a60-3a5469e7e62f"
---

The Ether is the plane where the [[Ether mirror]] exists.
It is the inside of the contained black hole held by the [[Pillar]]: a small universe made almost only of mana, the mana produced by the minds of the living beings of Kaelesmuth, with at best a few particles that broke the containment. Every Pillar leads to this same Ether.
There, all the magic of Kaelesmuth takes it's source. Its ambient mana is corrosive: whatever is not fed dissolves into it. See [[Magic]].

### Ecosystem

This is the world of the [[Ether mirror]].

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
