import re

__version__ = '0.2'

marker = object()


class Any:
    """
    >>> v = {"a": 1, "b": 2}
    >>> assert v == {"a": 1, "b": Any()}
    """
    o = marker

    def __eq__(self, o):
        self.o = o
        return True

    def __repr__(self):
        return repr(self.o) if self.o != marker else 'Any'


class NotNone:
    """
    >>> v = {"a": 1, "b": 2}
    >>> assert v == {"a": 1, "b": NotNone()}
    """
    o = marker

    def __eq__(self, o):
        e = o is not None
        if e:
            self.o = o
        else:
            self.o = "%s is None" % o
        return e

    def __repr__(self):
        return repr(self.o) if self.o != marker else 'NotNone'


class IsTrue:
    """
    >>> v = {"a": 1, "b": 2}
    >>> assert v == {"a": 1, "b": IsTrue()}
    """
    o = marker

    def __eq__(self, o):
        e = bool(o)
        if e:
            self.o = o
        else:
            self.o = "%s == False" % o
        return e

    def __repr__(self):
        return repr(self.o) if self.o != marker else 'IsTrue'


class IsA:
    """
    >>> v = {"a": 1, "b": 2}
    >>> assert v == {"a": 1, "b": IsA(int)}
    """
    o = marker

    def __init__(self, typ):
        self.typ = typ

    def __eq__(self, o):
        e = isinstance(o, self.typ)
        if e:
            self.o = o
        else:
            self.o = "type(%s) == %s is not %s" % (o, type(o), self.typ)
        return e

    def __repr__(self):
        return repr(self.o) if self.o != marker else ('IsA(%s)' % self.typ)


class Match:
    """
    >>> v = {"a": 1, "b": 2}
    >>> assert v == {"a": 1, "b": Match(r"\d")}
    >>> assert v == {"a": 1, "b": Match(r"[a-z]")}
    Traceback (most recent call last):
     ...
    AssertionError
    """
    o = marker

    def __init__(self, pattern):
        self.pt = re.compile(pattern)

    def __eq__(self, o):
        e = self.pt.match(str(o))
        if e:
            self.o = o
        else:
            self.o = "%s is not match %s" % (o, self.pt.pattern)
        return e

    def __repr__(self):
        return repr(self.o) if self.o != marker else ('Match(%s)' % self.pt.pattern)


class Len:
    o = marker

    def __init__(self, l):
        self.l = l

    def __eq__(self, o):
        e = len(o) == self.l
        if e:
            self.o = o
        else:
            self.o = "len(%s) = %d != %d" % (o, len(o), self.l)
        return e

    def __repr__(self):
        return repr(self.o) if self.o != marker else 'Len'

