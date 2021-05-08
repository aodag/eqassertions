import pytest


class TestAny:
    @pytest.fixture
    def target(self):
        from eqassertions import Any
        return Any

    def test_eq(self, target):
        a = target()
        assert "abcde" == a

    def test_repr(self, target):
        a = target()
        assert repr(a) == "Any"

    def test_repr_after_eq(self, target):
        a = target()
        a == "abcde"
        assert repr(a) == "'abcde'"


class TestNotNone:
    @pytest.fixture
    def target(self):
        from eqassertions import NotNone
        return NotNone

    def test_eq(self, target):
        n = target()
        assert n == "a"

    def test_eq_none(self, target):
        n = target()
        assert not n == None

    def test_repr(self, target):
        n = target()
        assert repr(n) == 'NotNone'

    def test_repr_after_eq(self, target):
        n = target()
        n == "abcde"
        assert repr(n) == "'abcde'"

    def test_repr_after_eq_fail(self, target):
        n = target()
        n == None
        assert repr(n) == "'None is None'"


class TestIsTrue:
    @pytest.fixture
    def target(self):
        from eqassertions import IsTrue
        return IsTrue

    def test_eq(self, target):
        t = target()
        assert t == "a"

    def test_eq_false(self, target):
        t = target()
        assert not t == ""

    def test_repr(self, target):
        t = target()
        assert repr(t) == "IsTrue"

    def test_repr_after_eq(self, target):
        t = target()
        t == "a"
        assert repr(t) == "'a'"

    def test_repr_after_false(self, target):
        t = target()
        t == []
        assert repr(t) == "'[] == False'"


class TestIsA:
    @pytest.fixture
    def target(self):
        from eqassertions import IsA
        return IsA

    def test_eq(self, target):
        class Dummy:
            pass

        a = target(Dummy)
        assert a == Dummy()

    def test_eq_not_instance(self, target):
        class Dummy:
            pass

        a = target(Dummy)
        assert not a == 1
        
    def test_repr(self, target):
        a = target(int)
        assert repr(a) == "IsA(<class 'int'>)"

    def test_repr_after_eq(self, target):
        a = target(int)
        a == 1
        assert repr(a) == "1"

    def test_repr_after_eq_fail(self, target):
        a = target(int)
        a == "1"
        assert repr(a) == '"type(1) == <class \'str\'> is not <class \'int\'>"'


class TestMatch:
    @pytest.fixture
    def target(self):
        from eqassertions import Match
        return Match

    def test_eq(self, target):
        m = target(r"\d")
        assert m == "1"

    def test_eq_not_match(self, target):
        m = target(r"\d")
        assert not m == "a"

    def test_repr(self, target):
        m = target(r"\d")
        assert repr(m) == "Match(\\d)"

    def test_repr_after_eq(self, target):
        m = target(r"\d")
        m == "1"
        assert repr(m) == "'1'"

    def test_repr_after_eq_not_match(self, target):
        m = target(r"\d")
        m == "a"
        assert repr(m) == r"'a is not match \\d'"


class TestIn:
    @pytest.fixture
    def target(self):
        from eqassertions import In
        return In

    def test_eq(self, target):
        m = target([1, 2, 3])
        assert m == 1

    def test_eq_not_in(self, target):
        m = target([1, 2, 3])
        assert not m == 4

    def test_repr(self, target):
        m = target([1, 2, 3])
        assert repr(m) == "In([1, 2, 3])"

    def test_repr_after_eq(self, target):
        m = target([1, 2, 3])
        m == 1
        assert repr(m) == "1"
