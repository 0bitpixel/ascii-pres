# DATA SPECIFICATION 1.0

## Table of Contents
- 1: Input Folder Structure
- 2:`<nat>.slide`
  - 2.1: File Sections
  - 2.2: Types
  - 2.3. Draw Methods
  - 2.4. Color IDs

---

## 1. Input Folder Structure

- `{rootfolder}`
  - `slides`
    - `1.slide`
    - `2.slide`
    - `...`
    - `<nat>.slide`

## 2. `<nat>.slide`

- *basename*: slide index
 - index defines order of slides
 - index required to be a positive integer 
 - index continuity not required
   - allows for basic-like insertions without full restructuring (e.g. 10, *15*, 20, 30, *35*, 40, ...)
 - Zero-Prefixing (`1` -> `001`) not required but recommended for proper ordering in file managers.
- `.slide`: mandatory file type
  - possible future purpose: grouping different types of files to an index (`n.slide`, `n.note`, etc.)

### 2.1. File Sections

#### 2.1.1. General Format
```slide
SECTION sectionname
keyword: option=value option2=value
keyword: {
option=value
option2=value
}
ENDSECTION
```

- Whitespace amount is irrelevant, but it *must* exist.
  - Whitespace is used as a separator between tokens.
  - Legal
    - `SECTION␣sectionname`
    - `keyword:␣␣␣␣␣option=value␣␣␣option2=value`
  - Illegal
    - `SECTIONsectionname`
    - `keyword:option=value`
    - `option=valueoption2=value`
- Whitespace within tokens *must not* exist.
  - Legal
    - `option=value`
    - `longoptionname=longvalue`
  - Illegal
    - `option = value`
    - `long optionname=long value`
- SECTION `content` *must not* contain string `ENDSECTION` verbatim.

#### 2.1.2. Implemented Sections
- `format`
- `content`
- `areas`
- `config`

##### 2.1.2.1. `format`

> Used to specify the format of the .slide file.

###### Keywords

- `version: version=<version>`
  - `version [=1.0]`: Version of the .slide file.

##### 2.1.2.2 `content`

> Contains raw Unicode Slide Data.
> Gets drawn *on top of existing canvas*, without it getting cleared.

###### Special Cases

- Empty `SECTION slide`
  - Canvas *cleared* using draw options specified in `SECTION config` (→ 2.1.2.4.).

##### 2.1.2.3. `areas`

> Separates Areas of the Content to be drawn *after* all non-area is drawn.
> Areas can have special options and draw modes set, allowing for primitive draw-in and erase animations.  
> Areas *may overlap*. Because areas get drawn sequentially, later areas will overwrite earlier areas
> on the canvas. (Reminder: Spaces/Whitespace is not drawn. Only non-whitespace characters are drawn.)

###### Keywords

- `area: index=<nat> corner1=<coordinate> corner2=<coordinate> foreground=<colorid> background=<colorid>
   delay=<posfloat> origin=<cardinal> drawmethod=<drawmode> drawspeed=<posfloat> dirprio=<cardinalpermutation> 
   erase=<bool>`
  - `index [required]`: Positive integer; index defines draw order of areas; continuity not required
  - `corner1` & `corner2 [required]`: Line and Column of area corners
  - `foreground [inherited from config.foreground]`: Foreground Color ID (→ 2.4)
  - `background [inherited from config.background]`: Background Color ID (→ 2.4)
  - `delay [=0]`: Delay in Seconds to wait *before* area is drawn to screen
  - `origin [=c]`: Where to begin drawing. Nearest character if `drawmode=follow`, else corner/side-middle of area
  - `drawmethod [=radial]`: Draw Method (→ 2.3.)
  - `drawspeed [=20]`: Draw Speed in characters per second
  - `dirprio [=nesw]`: Only relevant if `drawmode=follow`, else ignored.
    Defines directional priority of follow mode if forks are encountered.
  - `erase [=false]`: Decides if positions that would be drawn erase from the canvas instead.
    If set, drawn character doesn't matter.

#### 2.1.2.4. `config`

> Specifies further configuration for the slide, along with draw options for all non-area.

##### Keywords

- `foreground: color=<colorid>`
  - `color [=7]`: Color ID (→ 2.4)
- `background: color=<colorid>`
  - `color [=0]`: Color ID (→ 2.4)
- `align: slidepos=(<coordinate> | <cardinal> | <relcoordinate>) canvaspos=(<coordinate> | <cardinal> | <relcoordinate>)
   offset=<relcoordinate>`
  - *Defines, which position on the slide gets aligned to which position on the canvas, and what offset to apply.*
  - `slidepos [=c]`: Position on the Slide
  - `canvaspos [=c]`: Position on the Canvas
  - `offset [=0,0]`: Offset of Slide once positioned on Canvas
- `drawspeed: speed=<posfloat>`
  - `speed [=20]`: Draw Speed in characters per second
- `drawmethod: method=<drawmethod> dirprio=<cardinalpermutation>`
  - `method [=linebyline]`: Draw Method (→ 2.3.)
- `erase: enabled=<bool>`:
  - `enabled [=false]`: Decides if positions that would be drawn erase from the canvas instead.
              If set, drawn character doesn't matter.
- `autocontinue: enabled=<bool> delay=<posfloat>`
  - `enabled [=false]`: Decides, if drawing is automatically continued to the next slide
                        instead of waiting for user trigger.
  - `delay [=0]`: Delay to wait after finishing drawing before auto continuing to next slide.
- `onlyareas: enabled=<bool>`
  - `enabled [=false]`: If enabled, only areas get drawn, all non-area characters will get ignored.

### 2.2. Types

> Note: No whitespace allowed except if specified (e.g. no `1,␣2` for `<coordinate>`)

- Numeric
  - `<nat>`: Natural Number
  - `<int>`: Integer (any whole number)
  - `<float>`: Real Number (. as decimal separator)
    - `<posfloat>`: Positive Number
  - `<version>`: `<nat>.<nat>`
- Boolean
  - `<bool>`: `true` or `false`
- Spatial
  - `cardinal`: Cardinal Direction
    - `=n` = Top Edge Middle
    - `=e` = Right Edge Middle
    - `=s` = Bottom Edge Middle
    - `=w` = Left Edge Middle
    - `=nw` = Top Left Corner
    - `=ne` = Top Right Corner
    - `=sw` = Bottom Left Corner
    - `=se` = Bottom Right Corner
    - `=c` = Center
    - `cardinalpermutation`: Any permutation (=exactly one of each, in any order) of `n`, `e`, `s` and `w`. 
                             Examples: `nesw`, `senw`, `wens`, `nswe`, etc.
  - `<coordinate>`: `<nat>,<nat>`
    - `<relcoordinate>`: `<cardinal>,<int>,<int>` (coordinate relative to given cardinal)
- Misc
  - `<colorid>`: Color ID (→ 2.4)
  - `<drawmethod>`: Draw Method (→ 2.3)

### 2.3. Draw Methods

> Specifies, how the slide/area are drawn to the canvas.

#### 2.3.1. Supported Methods

- `linebyline`
- `radial`
- `follow`
- `random`

##### 2.3.1.1. `linebyline` Method

Content gets drawn in one line at a time, starting at origin and writing away from it.

Only Corners (`nw`, `ne`, `sw`, `se`) supported as origins.

###### Example:
```text
0 1 2 3
4 5 6 7 8 9
A B C D E F
```

##### 2.3.1.2. `radial` Method

Content gets drawn radially out from origin.  
Based on Euclidean distance from origin.  
Prioritizes based on `dirprio` if encountering multiple undrawn characters with equal distance.

###### Example (`dirprio=nesw`)

```text
0 1 4 9
2 3 6 B
5 7 8 D
A C E F
```

##### 2.3.1.3. `follow` Method

Starts at nearest character to given origin, choosing by `dirprio` if there's multiple candidates.  
Follows paths of characters.  
Chooses direction at forks based on `dirprio`.
Backtracks if there's no more characters to draw (e.g. end of path, completed fork).  
To-be-drawn content should be fully continuous. It not being continuous is not an error, but characters disconnected
from the main path will not be drawn because the algorithm never reaches them.

###### Example (`dirprio=nesw`)

Original:
```text
  │   ┌ ─
  ├ ─ ┤
─ ┤   └ ─
  ├ ─ ─
  ├ ─
  │     X
```

Draw Order:
```text
  1   5 6
  2 3 4
F 9   7 8
  0 A B
  C D
  E
```
Attention on: X is disconnected from content -> ignored

##### 2.3.1.4. `random` Method

Draws characters at random.

### 2.4. Color IDs

ANSI/xTerm 8-Bit color ID from 0 to 255.  
[Color Reference](https://gcollic.github.io/ansi-console-to-html/ansi_colors_table.html)

If it can't be detected that the current terminal supports 8-Bit color (based on `TERM` environment variable),
all non-4-Bit Colors (16 and above) get rounded to the nearest 4-Bit Color (0-15).

### 2.5. Example `.slide` File

```slide
SECTION format
version: value=1.0
ENDSECTION

SECTION content
            _____  _____ _____ _____                  _   
     /\    / ____|/ ____|_   _|_   _|      /\        | |  
    /  \  | (___ | |      | |   | |______ /  \   _ __| |_ 
   / /\ \  \___ \| |      | |   | |______/ /\ \ | '__| __|
  / ____ \ ____) | |____ _| |_ _| |_    / ____ \| |  | |_ 
 /_/    \_\_____/ \_____|_____|_____|  /_/    \_\_|   \__|
                                                          
\    /\
 )  ( ')
(  /  )
 \(__)|
ENDSECTION

SECTION areas
area:{
   index=1
   corner1=8,1
   corner2=11,8
   foreground=174
   origin=ne
   drawspeed=4
}
ENDSECTION

SECTION config
align slidepos=nw canvaspos=nw offset=5,5
ENDSECTION
```
