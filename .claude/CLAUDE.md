# Kaelesmuth vault

This folder is an Obsidian vault for the user's fantasy world, Kaelesmuth (planets Aethernam and Zephyrion, plus the Ether).

- Rules: `Schema.md` (exact property rules, time and place) and `Vault conventions.md` (why). Tools and the export format: `Tools.md`.
- Never put the user's real name in a note. No spoiler markup: the vault is private and writer-only.
- Scripts in `_tools/` (Python 3, standard library): `check_vault.py` (runs before every commit), `world_at.py` (the world at a year), `compile.py` (dossiers), `export.py` (data file for tools). Build new tools on `vault.py` and `world_at.World`.
- Skills: `write-lore` to add lore, `compile-dossier` for dossiers, `export-world` for the tool data file.
- Commit changes with git; remind the user to `git push`.
