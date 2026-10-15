---
title: "Backlog"
type: "meta"
tags:
  - "vault/backlog"
---

# Backlog

Improvement ideas for the vault. Not started yet; tick them off as they get done.

- [ ] **Interactive world map with a year slider.** A small web page built on Leaflet (the same engine as the Obsidian Leaflet plugin) with a slider for the year. Each map image and marker gets "from" and "until" years, ideally read from the notes' frontmatter. Moving the slider swaps the base map at big events (for example [[Arrack]]'s near-destruction of [[Aethernam]] in [[The Great Cataclysm]]) and shows only what exists at that date.
- [ ] **Put the vault under git** for full history and easy backups. *(Suggested by Claude.)*
- [ ] **Timeline tool.** Look for (or build) a tool to display and manage timelines from the event notes, once events are split into their own notes. Candidates to investigate: Obsidian timeline plugins, a Bases view sorted by date, or a hand-made page sharing code with the year-slider map.
- [ ] **Calendar conversion between Aethernam and Zephyrion.** Both planets orbit the same star, so their year lengths follow from their orbital distances. Needs: each planet's year length in a shared unit (or each planet's distance from the star), and one moment dated in both calendars as an anchor. The numbers go in `_tools/schema.json` (`calendar_conversion`); every tool picks them up from there (see [[Tools]]).
- [ ] **Family tree view.** Draw family trees from the `parents` and `partners` properties of character notes, so the tree updates itself. Options: a hand-made page (like the map), or an Obsidian plugin that reads those properties.
