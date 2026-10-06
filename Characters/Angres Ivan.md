---
type: "character"
aliases: []
planet:
  - "[[Aethernam]]"
importance: "main"
calendar: "aethernam"
partners:
  - "[[Angres Adelaïde]]"
status: "canon"
tags: []
wa_id: "56386d31-deb6-4f83-9217-1e94cf0e95ec"
---

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
