import importlib

__author__ = "James \"clug\" <clug@clug.xyz>"
__version__ = "1.0.0"

__all__ = ["_datetime", "_string", "collection", "number"]

from . import collection, _datetime as datetime, number, _string as string
