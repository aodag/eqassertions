==================
eqassertion
==================

assertions in `__eq__` methods.

>>> data = {"a": 1, "b": 2}
>>> assert {"a": 1, "b": Any()}
>>> assert {"a": 1, "b": NotNone()}
>>> assert {"a": 1, "b": IsA(int)}
>>> assert {"a": 1, "b": IsTrue()}
