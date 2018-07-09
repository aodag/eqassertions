==================
eqassertion
==================

assertions in `__eq__` methods.

>>> from eqassertions import Any, NotNone, IsA, IsTrue, Match
>>> data = {"a": 1, "b": 2}
>>> assert {"a": 1, "b": Any()}
>>> assert {"a": 1, "b": NotNone()}
>>> assert {"a": 1, "b": IsA(int)}
>>> assert {"a": 1, "b": IsTrue()}
>>> assert v == {"a": 1, "b": Match(r"\d")}
>>> assert v == {"a": 1, "b": Match(r"[a-z]")}
Traceback (most recent call last):
 ...
AssertionError
