import builtins
import re
from dataclasses import field
from urllib.parse import urlparse

from rdflib import Literal, XSD


def empty_list():
    return field(default_factory=list)


def empty_dict():
    return field(default_factory=dict)


def empty_set():
    return field(default_factory=set)


builtinnames = dir(builtins)


class NCName(str):
    """ Wrapper for NCName class

    See: <https://www.w3.org/TR/1999/REC-xml-names-19990114/#NT-NCName>
    """
    ncname_pattern = re.compile(r'[a-zA-Z][a-zA-Z0-9._-]*$')

    def __init__(self, v: str) -> None:
        if not self.is_valid(v):
            raise ValueError(f"{v}: invalid prefix")

    @classmethod
    def is_valid(cls, v: str) -> bool:
        return bool(cls.ncname_pattern.match(v))


class URIorCURIE(str):
    """ A URI represented as a URI or a CURIE """
    def __init__(self, v: str) -> None:
        if not URIorCURIE.is_valid(v):
            raise ValueError(f"{v} is not a valid URI or CURIE")

    @classmethod
    def is_valid(cls, v: str) -> bool:
        if ':' in v and '://' not in v:
            return URIorCURIE.is_curie(v)
        else:
            return URI.is_valid(v)

    @staticmethod
    def is_absolute(v: str) -> bool:
        return bool(urlparse(v).netloc)

    @staticmethod
    def is_curie(v: str) -> bool:
        if ':' in v and '://' not in v:
            parts = v.split(':', 1)
            return len(parts[0]) == 0 or NCName.is_valid(parts[0])
        return False

class URI(str):
    """ A relative absolute URI
    """
    def __init__(self, v: str) -> None:
        if not URI.is_valid(v):
            raise ValueError(f"{v}: is not a valid URI")

    @classmethod
    def is_valid(cls, v: str) -> bool:
        return not URIorCURIE.is_curie(v) and bool(urlparse(v))


class Bool:
    """ Wrapper for boolean class """
    bool_true = re.compile(r'([Tt]rue)|(1)$')
    bool_false = re.compile(r'([Ff]alse)|(0)$')

    def __new__(cls, v):
        if isinstance(v, bool):
            return v
        if cls.bool_true.match(str(v)):
            return True
        if cls.bool_false.match(str(v)):
            return False
        raise ValueError(f"{v}: Must be a boolean value")


class XSDTime(str):
    """ Wrapper for time class """
    def __init__(self, value: str) -> None:
        super().__init__()
        self = Literal(value, datatype=XSD.time).value


class XSDDate(str):
    """ Wrapper for date class """
    def __init__(self, value: str) -> None:
        super().__init__()
        self = Literal(value, datatype=XSD.date).value


class XSDDateTime(str):
    """ Wrapper for date time class """
    def __init__(self, value: str) -> None:
        super().__init__()
        self = Literal(value, datatype=XSD.dateTime).value
