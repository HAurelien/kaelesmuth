---
type: "meta"
tags: []
---

# Kaelesmuth

**Current date:** 3048/01/01

This is a world I'm building on my own. I will need to setup a few things before being able to write something down, so I'll try out this software. We never know how usefull it could be.
I would have set this world to private, if I had the choice.

**Improvement ideas:** [[Backlog]]

**How the world works:** [[Magic]]

Every list below fills itself from the notes' `type` property.

## Timelines

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "timeline"
views:
  - type: table
    name: Timelines
    order:
      - file.name
      - planet
      - calendar
```

## Events

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "event"
views:
  - type: table
    name: Events
    order:
      - file.name
      - year
      - calendar
      - era
      - event_type
    sort:
      - property: year
        direction: ASC

```

## Places

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "place"
views:
  - type: table
    name: Places
    order:
      - file.name
      - place_type
      - planet
```

## Characters

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "character"
views:
  - type: table
    name: Characters
    order:
      - file.name
      - importance
      - species
      - planet
      - affiliations
```

## Gods

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "god"
views:
  - type: table
    name: Gods
    order:
      - file.name
      - affiliations
      - planet
```

## Organizations

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "organization"
views:
  - type: table
    name: Organizations
    order:
      - file.name
      - org_type
      - planet
```

## Species

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "species"
views:
  - type: table
    name: Species
    order:
      - file.name
      - planet
```

## Conditions

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "condition"
views:
  - type: table
    name: Conditions
    order:
      - file.name
      - condition_type
```

## Items

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "item"
views:
  - type: table
    name: Items
    order:
      - file.name
      - item_type
      - importance
```

## Languages

```base
filters:
  and:
    - '!file.inFolder("_templates")'
    - type == "language"
views:
  - type: table
    name: Languages
    order:
      - file.name
```
