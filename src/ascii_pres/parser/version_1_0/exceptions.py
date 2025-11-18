"""
SlideError
    DataError
        SectionError
            DuplicateSectionError
            NestedSectionError
            OutsideSectionError
            UnopenedSectionError
            UnclosedSectionError
            InvalidSectionError
"""


class SlideError(Exception):
    pass

class DataError(SlideError):
    pass

class SectionError(DataError):
    pass

class DuplicateSectionError(SectionError):
    pass

class NestedSectionError(SectionError):
    pass

class OutsideSectionError(SectionError):
    pass

class UnopenedSectionError(SectionError):
    pass

class UnclosedSectionError(SectionError):
    pass

class InvalidSectionError(SectionError):
    pass