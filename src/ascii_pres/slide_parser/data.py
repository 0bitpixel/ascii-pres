from copy import deepcopy
from typing import TypedDict, Literal, Tuple


class ConfigDict(TypedDict):
    foreground: int
    background: int
    align: Tuple[
        Tuple[Literal["coord"], int, int] | Tuple[Literal["dir"], str],
        Tuple[Literal["coord"], int, int] | Tuple[Literal["dir"], str],
    ]
    draw_delay: float
    draw_method: Literal["linebyline", "radial", "square", "greedy", "random"]
    draw_origin: Literal["n", "ne", "e", "se", "s", "sw", "w", "nw", "c"]
    screen_clear: bool
    auto_advance: bool
    auto_advance_delay: float

class AreaDict(TypedDict):
    coord1: Tuple[int, int] | None
    coord2: Tuple[int, int] | None
    foreground: int
    background: int
    draw_method: str
    draw_origin: str
    draw_delay: float
    greedy_prio: str

class SlideDict(TypedDict):
    format: str | None
    slide: str | None
    areas: dict[int, AreaDict]
    config: ConfigDict


DEFAULT_SLIDE: SlideDict = {
    "format": None,
    "slide": None,
    "areas": {},
    "config": {
        "foreground": 7,
        "background": 0,
        "align": (("dir", "c"), ("dir", "c")),
        "draw_delay": 0.05,
        "draw_method": "linebyline",
        "draw_origin": "nw",
        "screen_clear": False,
        "auto_advance": False,
        "auto_advance_delay": 0,
    }
}

DEFAULT_AREA: AreaDict = {
    "coord1": None,
    "coord2": None,
    "foreground": 7,
    "background": 0,
    "draw_method": "linebyline",
    "draw_origin": "nw",
    "draw_delay": 0.05,
    "greedy_prio": "nesw",
}


def get_default_slide() -> SlideDict:
    return deepcopy(DEFAULT_SLIDE)


def get_default_area() -> AreaDict:
    return deepcopy(DEFAULT_AREA)
