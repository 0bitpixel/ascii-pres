import pytest

from ascii_pres.parser.version_1_0 import exceptions
from ascii_pres.parser.version_1_0.sectionize import sectionize


def test_minimal():
    minimal_input = [
    "STARTSECTION format",
    "version: value=1.0",
    "ENDSECTION",
    ]

    assert sectionize(minimal_input) == {
        "format": [
            "version: value=1.0"
        ]
    }


def test_valid():
    valid_input = [
    "STARTSECTION format",
    "version: value=1.0",
    "ENDSECTION",
    "",
    "STARTSECTION areas",
    "area: {",
    "corner1=1,1",
    "corner2=2,3",
    "foreground=12",
    "}",
    "ENDSECTION",
    "",
    "STARTSECTION config",
    "background: color=8",
    "drawmethod: method=radial dirprio=nwse",
    "ENDSECTION",
    ]

    assert sectionize(valid_input) == {
        "format": [
            "version: value=1.0",
        ],
        "areas": [
            "area: {",
            "corner1=1,1",
            "corner2=2,3",
            "foreground=12",
            "}",
        ],
        "config": [
            "background: color=8",
            "drawmethod: method=radial dirprio=nwse",
        ]
    }


def test_whitespace():
    whitespaced_input = [
    "        STARTSECTION section        ",
    "     foo",
    "  bar",
    "             ENDSECTION  ",
    ]

    assert sectionize(whitespaced_input) == {
        "section": [
            "foo",
            "bar",
        ]
    }


def test_duplicates():
    duplicate_sections = [
    "STARTSECTION section",
    "foo",
    "ENDSECTION",
    "",
    "STARTSECTION section",
    "bar",
    "ENDSECTION",
    ]

    with pytest.raises(exceptions.DuplicateSectionError):
        sectionize(duplicate_sections)


def test_nested_sections():
    nested_sections = [
    "STARTSECTION section",
    "STARTSECTION section2",
    "foo",
    "ENDSECTION",
    "ENDSECTION",
    ]

    with pytest.raises(exceptions.NestedSectionError):
        sectionize(nested_sections)


def test_outside_section():
    content_outside_section = [
    "foo",
    ]

    with pytest.raises(exceptions.OutsideSectionError):
        sectionize(content_outside_section)


def test_unopened_section():
    unopened_section = [
    "ENDSECTION",
    ]

    with pytest.raises(exceptions.UnopenedSectionError):
        sectionize(unopened_section)


def test_unclosed_section():
    unclosed_section = [
    "STARTSECTION section",
    "foo",
    ]

    with pytest.raises(exceptions.UnclosedSectionError):
        sectionize(unclosed_section)


def test_invalid_section():
    invalid_section_definition = [
    "STARTSECTION section error",
    "ENDSECTION",
    ]

    with pytest.raises(exceptions.InvalidSectionError):
        sectionize(invalid_section_definition)
