from typing import TypedDict, Literal
from copy import deepcopy


# SLIDE DATA FORMAT
# =================
# slide_data = {
#     content: list[str]
#     areas: {
#         int:
#             corner1: tuple[int, int]
#             corner2: tuple[int, int]
#             foreground: int
#             background: int
#             delay: float
#             origin: CARDINALS
#             drawmethod: DRAW_METHODS
#             dirprio: str
#             erase: bool
#     }
#     foreground: int
#     background: int
#     align:
#         index: int
#         corner1: tuple[int, int]
#         corner2: tuple[int, int]
#     drawspeed: float
#     drawmethod:
#         drawmethod: DRAW_METHODS
#         dirprio: str
#     erase: bool
#     autocontinue:
#         enabled: bool
#         delay: float
#     onlyareas: bool
# }


type CARDINALS = Literal["n", "e", "s", "w", "nw", "ne", "sw", "se", "c"]
type DRAW_METHODS = Literal["linebyline", "radial", "follow", "random"]


class AreaTypes(TypedDict):
    corner1: tuple[int, int] | None
    corner2: tuple[int, int] | None
    foreground: int
    background: int
    delay: float
    origin: CARDINALS
    drawmethod: DRAW_METHODS
    dirprio: str
    erase: bool

class AlignTypes(TypedDict):
    slidepos: tuple[int, int] | CARDINALS | tuple[CARDINALS, int, int]
    canvaspos: tuple[int, int] | CARDINALS | tuple[CARDINALS, int, int]
    offset: tuple[int, int]

class DrawMethodTypes(TypedDict):
    drawmethod: DRAW_METHODS
    dirprio: str

class AutoContinueTypes(TypedDict):
    enabled: bool
    delay: float

class SlideTypes(TypedDict):
    content: list[str] | None
    areas: dict[int, AreaTypes]
    foreground: int
    background: int
    align: AlignTypes
    drawspeed: float
    drawmethod: DrawMethodTypes
    erase: bool
    autocontinue: AutoContinueTypes
    onlyareas: bool


DEFAULT_AREA: AreaTypes = {
    "corner1": None,
    "corner2": None,
    "foreground": 7,
    "background": 0,
    "delay": 0,
    "origin": "c",
    "drawmethod": "linebyline",
    "dirprio": "nesw",
    "erase": False,
}

DEFAULT_ALIGN: AlignTypes = {
    "slidepos": "c",
    "canvaspos": "c",
    "offset": (0, 0),
}

DEFAULT_DRAW_METHOD: DrawMethodTypes = {
    "drawmethod": "linebyline",
    "dirprio": "nesw",
}

DEFAULT_AUTO_CONTINUE: AutoContinueTypes = {
    "enabled": False,
    "delay": 0,
}

DEFAULT_SLIDE: SlideTypes = {
    "content": None,
    "areas": {},
    "foreground": 7,
    "background": 0,
    "align": DEFAULT_ALIGN,
    "drawspeed": 20,
    "drawmethod": DEFAULT_DRAW_METHOD,
    "erase": False,
    "autocontinue": DEFAULT_AUTO_CONTINUE,
    "onlyareas": False,
}


def get_new_slide() -> SlideTypes:
    return deepcopy(DEFAULT_SLIDE)

def get_new_area() -> AreaTypes:
    return deepcopy(DEFAULT_AREA)

def get_new_drawmethod() -> DrawMethodTypes:
    return deepcopy(DEFAULT_DRAW_METHOD)

def get_new_autocontinue() -> AutoContinueTypes:
    return deepcopy(DEFAULT_AUTO_CONTINUE)
