"""Unit tests for the coords class of the katan.board module"""
from katan_ai.katan.board.coords import Coords

def test_eq_overwrite():
    test1, test2 = Coords(1, 2), Coords(1, 2)
    assert(test1 == test2)

def test_add_overwrite():
    test1, test2 = Coords(1, 2), Coords(1, 2)
    expected = Coords(2, 4)
    assert(test1 + test2 == expected)

def test_subtract_overwrite():
    test1, test2 = Coords(1, 2), Coords(1, 2)
    expected = Coords(0, 0)
    assert(test1 - test2 == expected)

def test_str_overwrite():
    testCoord = Coords(1, 2)
    expected = "(q: 1, r:2)"
    assert(str(testCoord) == expected)