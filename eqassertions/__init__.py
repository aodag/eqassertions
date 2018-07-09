__version__ = '0.1.1'


class Any:
    """
    >>> v = {"a": 1, "b": 2}
    >>> assert v == {"a": 1, "b": Any()}
    """
    def __eq__(self, o):
        return True


class NotNone:
    """
    >>> v = {"a": 1, "b": 2}
    >>> assert v == {"a": 1, "b": NotNone()}
    """
    def __eq__(self, o):
        return o is not None


class IsTrue:
    """
    >>> v = {"a": 1, "b": 2}
    >>> assert v == {"a": 1, "b": IsTrue()}
    """
    def __eq__(self, o):
        return bool(o)


class IsA:
    """
    >>> v = {"a": 1, "b": 2}
    >>> assert v == {"a": 1, "b": IsA(int)}
    """
    def __init__(self, typ):
        self.typ = typ

    def __eq__(self, o):
        return isinstance(o, self.typ)
