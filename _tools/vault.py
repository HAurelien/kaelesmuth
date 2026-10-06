"""Read the Kaelesmuth vault: notes, their properties, links and the schema.

Shared by the checker and by the tools built later (export, "state of the
world at year X"). Standard library only, so it runs anywhere Python 3.8+ does.

Properties are read with a small parser for the subset of YAML that
Obsidian's property editor writes:

    key: value          key: "quoted value"      key: []
    key:                key: [a, "b"]
      - item
      - "[[Link]]"

Anything outside that subset is reported as a parse error, which keeps the
notes editable from Obsidian's property panel.
"""

import json
import os
import re
import unicodedata

TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.dirname(TOOLS_DIR)
SKIP_DIRS = {".git", ".obsidian", ".trash", "_tools", "Attachments"}
TEMPLATES_DIR = "_templates"

LINK_RE = re.compile(r"!?\[\[([^\]|#]*)(#[^\]|]*)?(\|[^\]]*)?\]\]")
FULL_LINK_RE = re.compile(r"^\[\[([^\]|#]+)(#[^\]|]*)?(\|[^\]]*)?\]\]$")
DATE_RE = re.compile(r"^(-?\d+)(?:-(\d{2})(?:-(\d{2})(?: (\d{2}):(\d{2}))?)?)?$")


class ParseError(Exception):
    def __init__(self, line, message):
        super().__init__(message)
        self.line = line


# ---------------------------------------------------------------- properties

def _scalar(raw, line):
    s = raw.strip()
    if s == "" or s in ("null", "~"):
        return None
    if s.startswith('"'):
        if not s.endswith('"') or len(s) < 2:
            raise ParseError(line, "unclosed double quote")
        try:
            return json.loads(s)
        except ValueError:
            raise ParseError(line, "bad escape in double-quoted value")
    if s.startswith("'"):
        if not s.endswith("'") or len(s) < 2:
            raise ParseError(line, "unclosed single quote")
        return s[1:-1].replace("''", "'")
    if s.startswith("[["):
        raise ParseError(line, "links in properties must be quoted: \"%s\"" % s)
    if s in ("true", "True"):
        return True
    if s in ("false", "False"):
        return False
    if re.fullmatch(r"-?\d+", s):
        return int(s)
    if re.fullmatch(r"-?\d+\.\d+", s):
        return float(s)
    if s[0] in "{&*!|>%@`":
        raise ParseError(line, "unsupported YAML syntax: %s" % s)
    if s[0] == "#":
        return None
    return s


def _inline_list(raw, line):
    inner = raw.strip()[1:-1].strip()
    if not inner:
        return []
    items, buf, quote, depth = [], "", None, 0
    for ch in inner:
        if quote:
            buf += ch
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            buf += ch
        elif ch == "[":
            depth += 1
            buf += ch
        elif ch == "]":
            depth -= 1
            buf += ch
        elif ch == "," and depth == 0:
            items.append(_scalar(buf, line))
            buf = ""
        else:
            buf += ch
    if quote:
        raise ParseError(line, "unclosed quote in list")
    items.append(_scalar(buf, line))
    return items


def parse_properties(text):
    """Return (properties dict, body text, first body line number).

    Notes without a frontmatter block return ({}, text, 1) and props None
    is signalled by returning None as the first element."""
    if not text.startswith("---"):
        return None, text, 1
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None, text, 1
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise ParseError(1, "frontmatter is not closed with ---")
    props = {}
    current = None  # key whose block list is being read
    for i in range(1, end):
        n = i + 1
        raw = lines[i].rstrip("\r")
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t", "-")):
            stripped = raw.strip()
            if current is None or not stripped.startswith("-"):
                raise ParseError(n, "unexpected indented line: %s" % stripped)
            item = stripped[1:]
            if item and not item.startswith(" "):
                raise ParseError(n, "list items need a space after '-'")
            if props[current] is None:
                props[current] = []
            props[current].append(_scalar(item, n))
            continue
        m = re.match(r"^([A-Za-z0-9_\-]+):(.*)$", raw)
        if not m:
            raise ParseError(n, "not a 'key: value' line: %s" % raw)
        key, rest = m.group(1), m.group(2)
        if key in props:
            raise ParseError(n, "property '%s' appears twice" % key)
        rest_s = rest.strip()
        if rest_s.startswith("[") and not rest_s.startswith("[["):
            if not rest_s.endswith("]"):
                raise ParseError(n, "unclosed list")
            props[key] = _inline_list(rest_s, n)
            current = None
        else:
            props[key] = _scalar(rest, n)
            current = key if rest_s == "" else None
    body = "\n".join(lines[end + 1:])
    return props, body, end + 2


# ---------------------------------------------------------------- links

def norm(name):
    """Normalise a note name for lookups (Obsidian is case-insensitive)."""
    return unicodedata.normalize("NFC", name).strip().casefold()


def link_target(value):
    """'[[Name#h|alias]]' -> 'Name'; None if the value is not a single link."""
    if not isinstance(value, str):
        return None
    m = FULL_LINK_RE.match(value.strip())
    return m.group(1).strip() if m else None


def body_links(body, first_line):
    """Yield (line number, target) for every wikilink in the body."""
    in_code = False
    for i, line in enumerate(body.split("\n")):
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        for m in LINK_RE.finditer(re.sub(r"`[^`]*`", "", line)):
            if m.group(1).strip():
                yield first_line + i, m.group(1).strip()


def parse_date(value):
    """'2701-07-09 06:00' -> (2701, 7, 9, 6, 0) with None for missing parts."""
    if isinstance(value, int):
        value = str(value)
    if not isinstance(value, str):
        return None
    m = DATE_RE.match(value.strip())
    if not m:
        return None
    return tuple(int(g) if g is not None else None for g in m.groups())


# ---------------------------------------------------------------- notes

class Note:
    def __init__(self, path, rel):
        self.path = path
        self.rel = rel                     # path relative to the vault, with /
        self.name = os.path.splitext(os.path.basename(rel))[0]
        self.folder = os.path.dirname(rel)
        self.props = {}
        self.has_frontmatter = False
        self.body = ""
        self.body_line = 1
        self.parse_error = None
        with open(path, encoding="utf-8") as f:
            text = f.read().lstrip("﻿")
        try:
            props, self.body, self.body_line = parse_properties(text)
        except ParseError as e:
            self.parse_error = e
            return
        if props is not None:
            self.has_frontmatter = True
            self.props = props

    @property
    def type(self):
        return self.props.get("type")

    def get(self, key, default=None):
        return self.props.get(key, default)

    def __repr__(self):
        return "Note(%r)" % self.rel


class Vault:
    def __init__(self, root=VAULT_DIR, schema_path=None):
        self.root = root
        with open(schema_path or os.path.join(TOOLS_DIR, "schema.json"), encoding="utf-8") as f:
            self.schema = json.load(f)
        self.notes = []          # every note outside _templates
        self.templates = []      # notes in _templates
        self.files = set()       # normalised names of every file (for embeds)
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
            for fn in sorted(filenames):
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, root).replace(os.sep, "/")
                self.files.add(norm(fn))
                self.files.add(norm(rel))
                if not fn.endswith(".md"):
                    continue
                note = Note(full, rel)
                if rel.split("/")[0] == TEMPLATES_DIR:
                    self.templates.append(note)
                else:
                    self.notes.append(note)
        for dirpath, _, filenames in os.walk(os.path.join(root, "Attachments")):
            for fn in filenames:
                self.files.add(norm(fn))
        self.by_name = {}        # normalised name or alias -> [notes]
        for note in self.notes:
            keys = {norm(note.name), norm(note.rel[:-3])}
            for alias in note.get("aliases") or []:
                if isinstance(alias, str) and alias.strip():
                    keys.add(norm(alias))
            for k in keys:
                self.by_name.setdefault(k, []).append(note)

    # -- lookups

    def resolve(self, name):
        """Note a link target points to, or None. Names win over aliases."""
        hits = self.by_name.get(norm(name), [])
        if not hits:
            return None
        exact = [n for n in hits if norm(n.name) == norm(name) or norm(n.rel[:-3]) == norm(name)]
        return (exact or hits)[0]

    def resolve_link(self, value):
        target = link_target(value)
        return self.resolve(target) if target else None

    def of_type(self, *types):
        return [n for n in self.notes if n.type in types]

    # -- schema

    def type_schema(self, type_name):
        """Full property spec for a type: common + inherited + own."""
        types = self.schema["types"]
        t = types.get(type_name)
        if t is None:
            return None
        chain = [t]
        while chain[-1].get("inherits"):
            chain.append(types[chain[-1]["inherits"]])
        props, forbidden, span = {}, {}, None
        skip = set(t.get("skip_common", []))
        for k, v in self.schema["common_properties"].items():
            if k not in skip:
                props[k] = v
        for part in reversed(chain):
            props.update(part.get("properties", {}))
            forbidden.update(part.get("forbidden", {}))
            span = part.get("span", span)
        merged = dict(t)
        merged["properties"] = props
        merged["forbidden"] = forbidden
        merged["span"] = span
        return merged

    def enum_values(self, spec, prop):
        if "values" in spec:
            return list(spec["values"])
        src = spec.get("values_from")
        if src == "calendars":
            return list(self.schema["calendars"])
        if src == "statuses":
            return list(self.schema["statuses"])
        if prop == "type":
            return list(self.schema["types"])
        return None

    def span(self, note):
        """(start year, end year) of a note's existence, from its schema span.

        Either may be None when unknown. A one-year event returns (y, y)."""
        ts = self.type_schema(note.type)
        if not ts or not ts["span"]:
            return None, None
        start = note.get(ts["span"]["start"])
        end = note.get(ts["span"]["end"])
        start = start if isinstance(start, int) and not isinstance(start, bool) else None
        end = end if isinstance(end, int) and not isinstance(end, bool) else None
        if note.type == "event" and end is None:
            end = start
        return start, end
