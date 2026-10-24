---
type: place
aliases: 
  - "Tutsana Ouest"
  - "Western Tutsana"
planet:
  - "[[Zephyrion]]"
place_type: Country
parent: "[[Zephyrion]]"
owner: 
from: 
until: 
calendar: zephyrion
status: draft
tags: []
---

## Summary

A country in the north-west where life is now fairly good. It is governed by an assembly elected every ten years. Poorer than Istors, but free, and it has the food: large farmlands, which is no accident, since that is where all the slaves were.

## Geography

In the north-west. Large agricultural lands.

The old, undivided Tutsana: the north is fairly cold and snowy for a good part of the year, so the people lived in the west and the east, separated by a large desert. The west held the fields, the east and south the mines. The desert forced the country to keep a great maritime trade power to hold itself together. To the east, imposing mountains along the border with [[Ugrya]] guard the mines; they are hard to cross and even harder to go around because of the hot desert winds, which discouraged most armed conflicts between the two countries.

## History

### Before the Silence

Tutsana was one kingdom, its politics turned toward trade, with a large slave population in the mines of the east and south and in the fields of the west. The main government sat in the east ([[Eastern Tutsana]]) under King Istors; the west, agricultural and more populous, was ruled through intendants.

Resentment between east and west ran deep after several attempts at treason: the king's last two intendants in the west were both executed after insurrections, about ten and fifteen years before. Since then the ageing but paranoid king ruled with an iron fist, more set on controlling his own people than on foreign relations, which generally went his way.

Almost everyone believed the plots came from the west, against the better-armed and richer east. In truth they came from the neighbouring [[Ugrya]], which coveted the mines on its western border.

### The Silence and after

Before magic appeared, this region of the world was mostly made of slaves, ruled from [[Eastern Tutsana]] by the Istors dynasty. Their rebellion was helped by the gods during the Century of Silence (see [[Tutsana slave revolt]]). There were few survivors, which is why its population is still small compared to the rest of the world.

Under pressure from [[Grueca]], Tutsana was split: the west became today's Tutsana, and the east joined [[Ugrya]] as the [[Kingdom of Istors]].

### In 1770

Its large farmlands recently let it negotiate a peace with Grueca that it hopes will last. Apparently there are no more slaves in Tutsana. Rumours say it is allied with [[Isrïl]], helping the confederation feed its people.

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
