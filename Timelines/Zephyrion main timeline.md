---
type: "timeline"
aliases: []
planet:
  - "[[Zephyrion]]"
calendar: "zephyrion"
status: "draft"
tags: []
wa_id: "ce67aca8-a521-41f9-aadd-67f493987798"
---

This is the timeline retracing the major events of Zephyrion. It will only trace the most important events of this planet.

## Eras

### The pre-enlightenment

*... 2500 PME*

During this first Era, nature evolved, until Humans got born and begun to write down ideas, passing knowledge to future generations.

### The sedentarization

*2501 PME → 200 PME*

This era is marked by the first human technologies. Starting with one of the firsts human group who started to count with marks on rocks, until the mastery of the wheel.

### The Bronze metallurgy

*201 PME → 1300*

This Era was marked by the usage of the firsts metallurgy techniques, including actually both the bronze and the iron mastery, as the mountains

### The pre-magical age

*1301 → 1668*

During this era, false religions took much power upon the world. Latest scientifics discoveries allowed the world to connect through the seas, for both commercial and war purpose. Country from the east and south islands quickly got invaded. by the ones of the main continent. And a religion came to arise from the new trade opportunities of the est island collonies, spreading the words of the main owner's religion throughout the world. During this age, almost half of the world accepted this religion as their own, sometimes willingly, often not.

### The Silence

*1669 and beyond*

Also called the Century of Silence. It is the side-effect on Zephyrion of the curse of [[The Great Cataclysm]] (1669 here), much less harsh than on [[Aethernam]] but still felt. During this Era, magic appeared in the world. Almost spontaneously, because of the firsts unstable and underestimated effects of Magic, the world's population almost halved. However, as humans tried to understand what was happening, the [[Lower gods|The lower gods]] seemed to appear from nowhere, imposing themselves as the true gods. (Need to create an entry with the apparition date of the gods to sort out which ones where there at this moment)
Another funny information about this age is that an important element of the star map changed. This is something very well documented as stars were very important in navigation in this era. Lots of ships had accident before new and accurate star maps could be drawn, including the alteration of a star's trajectory. Even if we all know now it is and never was actually a Star.

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
      - date
      - era
      - event_type
    sort:
      - property: year
        direction: ASC
```
