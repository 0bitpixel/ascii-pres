# ASCII-Pres

A terminal- and text-based ASCII presentation tool.

## Installation

``` bash
poetry install
```

## Usage

``` bash
poetry run ascii-pres ./data/demo
```

The argument expects a folder containing the presentation data.

## .slide Specification (FORMAT 0.1)

A text-based slide definition format for **ascii-pres**.  
Designed for human-editable, machine-validated presentation slides containing ASCII art, configuration data, and drawing instructions.  
This document defines the syntax, structure, and runtime behavior of `.slide` files for **FORMAT 0.1**.

---

### FORMAT Header

Every `.slide` file **must begin** with a version declaration:

```
### FORMAT = 0.1 ###
```

- Must appear before any other content.  
- Parser must reject any version other than `0.1` unless explicitly supported.  
- No leading whitespace allowed.  
- Comments may follow on the same line.  

---

### Overview

Each `.slide` file defines a single presentation slide.  
File names determine order, not content.  
Parsing is strict — any syntax violation aborts the presentation before runtime.  
Whitespace, section order, and content order are irrelevant; delimiters and token prefixes define structure.

---

### 1. File Naming and Structure

| Property | Rule |
|-----------|------|
| **Extension** | `.slide` (mandatory) |
| **Name** | Integer filename (`0.slide`, `12.slide`, `401.slide`) |
| **Ordering** | Determined numerically by file stem (`int(filename)`) |
| **Skipping** | Allowed — numbering need not be continuous |
| **Encoding** | UTF-8 |
| **Line endings** | `\n` or `\r\n` both valid |
| **Tabs** | Treated as four spaces |

---

### 2. File Sections

Each file may contain up to three **major sections**, each enclosed by triple brackets.

```
SLIDE[[[
...content...
]]]
AREAS[[[
...content...
]]]
CONFIG[[[
...content...
]]]
```

Rules:

- **Order** of sections doesn’t matter.  
- **Opening brackets** (`[[[`) appear on the **same line** as the section name.  
- **Closing brackets** (`]]]`) must appear on their **own line**.  
- Sections may **repeat**:  
  - `SLIDE`: last one wins.  
  - `AREAS` and `CONFIG`: merged; later entries override earlier ones.  
- **Missing sections** are valid:  
  - No `SLIDE`: interpreted as screen clear.  
  - No `AREAS`: slide has no areas.  
  - No `CONFIG`: global/default config used.  

Section headers are uppercase and case-sensitive.

---

### 3. Comments and Whitespace

| Rule | Description |
|------|--------------|
| Comment syntax | `//` starts a comment. Everything after it on that line is ignored. |
| Comments allowed | Anywhere — even inside `SLIDE`; they are treated literally there. |
| Blank lines | Ignored except inside `SLIDE` (where they are literal). |
| Indentation | Ignored everywhere except inside `SLIDE`, where it counts toward coordinates. |
| Tabs | Equivalent to **four spaces** inside `SLIDE`. |

---

### 4. The `SLIDE` Section

The literal ASCII content displayed for the slide.

```
SLIDE[[[
<raw ASCII art, whitespace, symbols, text>
]]]
```

- All text inside is **literal** — including `//`, spaces, and symbols.  
- Coordinates are **1-indexed** (top-left = 1,1).  
- Tabs count as **4 spaces**.  
- No parsing, filtering, or substitution.  
- Supports full Unicode where terminals allow it.  

---

### 5. The `AREAS` Section

Defines interactive regions or drawing subareas within the slide.

#### Syntax

```
<id> = <coord1> <coord2> [F:<color>] [B:<color>] [M:<method>] [O:<origin>] [P:<priority>]
```

#### Example

```
1 = 3,5 10,12 F:ID34 B:black M:radial O:nw P:nesw
```

#### Components

| Token | Description | Required | Notes |
|--------|--------------|-----------|-------|
| `<id>` | Integer identifier | ✅ | Defines draw order (lower = earlier) |
| `<coord>` | `<x>,<y>` — two positive integers | ✅ | No spaces inside |
| `F:` | Foreground color | ❌ | See color rules |
| `B:` | Background color | ❌ | See color rules |
| `M:` | Draw method | ❌ | `linebyline`, `radial`, `square`, `greedy`, or `random` |
| `O:` | Draw origin | ❌ | `n`, `e`, `s`, `w`, `ne`, `se`, `sw`, `nw`, or `c` |
| `P:` | Greedy fork priority | ❌ | Only for `M:greedy`; must be a permutation of `n`, `e`, `s`, `w` |

#### Behavior

- Multiple `AREAS` sections **merge**.  
- Duplicate IDs **overwrite** earlier ones.  
- Token order after coordinates is **irrelevant**.  
- Unrecognized prefixes are **fatal errors**.  
- Whitespace acts as a separator but otherwise doesn’t matter.  

---

### 6. The `CONFIG` Section

Defines slide-specific configuration and overrides.

#### Syntax

```
<key> = <value> // comment
```

#### Rules

- Keys and values are **case-insensitive**.  
- Unknown keys cause **fatal errors**.  
- Keys may repeat; last value wins.  
- Missing CONFIG uses defaults.  
- Prefix-style (`K:<value>`) may be used for multi-token lines if readability requires.  

#### Supported Keys

| Key | Type | Description |
|------|------|-------------|
| `foreground` | color | Default text color |
| `background` | color | Default background color |
| `align` | `<coord>` \| `<direction>` `<anchor>` `<offset>` | Alignment or screen anchor |
| `delay` | float or fraction | Delay between character draws |
| `draw-method` | string | Default draw style for non-area drawing |
| `screen-clear` | boolean | Clears the screen using current draw method |

##### Boolean Rules

| Form | Meaning |
|------|----------|
| `flag` | true |
| `flag = true` | true |
| `flag = false` | false |
| *(absent)* | false |

---

### 7. `@@@!!!...!!!@@@` Escape

Marks ASCII line ranges to be excluded from parsing when ASCII content conflicts with delimiters.

#### Syntax

```
@@@!!!<start-line>,<end-line>!!!@@@
```

- Only **one** per file.  
- Both numbers must be positive integers.  
- Multiple markers → **fatal syntax error**.  
- Parser removes those lines before section parsing.  
- Can appear anywhere in the file.

---

### 8. Colors

Colors may be specified as numeric IDs or ANSI names.

| Form | Description |
|------|--------------|
| `ID<n>` | ANSI 256-color ID (`0–255`) |
| `<name>` | One of 16 standard ANSI color names (case-insensitive): `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `brightblack`, `brightred`, `brightgreen`, `brightyellow`, `brightblue`, `brightmagenta`, `brightcyan`, `brightwhite` |

If only a 16-color terminal is detected, `ID<n>` values are **approximated** to the nearest available color.

---

### 9. Defaults and Overrides

| Behavior | Rule |
|-----------|------|
| **Config priority** | `slide CONFIG` → `global config.toml` → hardcoded defaults |
| **Missing CONFIG** | Use global/default settings |
| **Missing SLIDE** | Equivalent to `screen-clear = true` |
| **Missing AREAS** | No areas defined |
| **Multiple CONFIG/AREAS** | Merge; last-wins per key/ID |

---

### 10. Error Handling

| Error | Behavior |
|--------|-----------|
| Unknown section | Ignored (reserved for future expansion) |
| Missing delimiters | Fatal syntax error |
| Invalid coordinates, direction, or method | Fatal syntax error |
| Duplicate escape markers | Fatal syntax error |
| Invalid greedy priority | Fatal syntax error |
| Unknown config key or prefix | Fatal syntax error |
| Any other syntax violation | Abort before presentation start |

All slide files are validated **before** presentation runtime.  
If any file fails validation, execution stops immediately.

---

### 11. Implementation Notes

- Parsing is **strict**, but insensitive to order and whitespace.  
- Prefix tokens (`F:`, `B:`, `M:`, etc.) may appear in any order after mandatory tokens.  
- All characters inside `SLIDE` are literal.  
- Tabs inside `SLIDE` equal four spaces for coordinate math.  
- Case-insensitive data should be normalized to lowercase internally.  
- The `FORMAT` header is mandatory and must match exactly.  
- Future versions should remain backward-compatible or explicitly rejected.  

---

### 12. Example

```
### FORMAT = 0.1 ###

// Example slide demonstrating all sections

SLIDE[[[
   /\    /\
  {  `---'  }
  {  O   O  }
~~|   V   |~~
]]]

AREAS[[[
1 = 3,2 8,4 F:brightred B:black M:radial O:nw P:nesw
]]]

CONFIG[[[
foreground = ID231
background = black
align = 0,0 c
delay = 0.05
draw-method = linebyline
screen-clear = true
]]]
```

### config.toml

WORK IN PROGRESS

## License

MIT
