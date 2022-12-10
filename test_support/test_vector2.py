import pytest

from support import Vector2


@pytest.mark.parametrize("first,second,expected", [
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 2)),
    (Vector2(1, 1), (0, 1), Vector2(1, 2)),
    ((1, 1), Vector2(0, 1), Vector2(1, 2)),
])
def test_add(first, second, expected):
    assert first + second == expected


@pytest.mark.parametrize("first,second,expected", [
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 0)),
    (Vector2(1, 1), (0, 1), Vector2(1, 0)),
    ((1, 1), Vector2(0, 1), Vector2(1, 0)),
])
def test_sub(first, second, expected):
    assert first - second == expected


@pytest.mark.parametrize("vector,expected", [
    (Vector2(1, 1), Vector2(1, 1)),
    (Vector2(-1, -1), Vector2(1, 1)),
    (Vector2(-1, 1), Vector2(1, 1)),
    (Vector2(1, -1), Vector2(1, 1)),
])
def test_abs(vector, expected):
    assert abs(vector) == expected


@pytest.mark.parametrize("first,second,expected", [
    (Vector2(1, 1), Vector2(1, 1), True),
    (Vector2(1, 1), (1, 1), True),
    (Vector2(1, 1), Vector2(2, 2), False),
    (Vector2(1, 1), (2, 2), False),
    ((1, 1), Vector2(1, 1), True),
])
def test_equal(first, second, expected):
    assert (first == second) is expected


@pytest.mark.parametrize("first,second,expected", [
    (Vector2(8, 4), 2, Vector2(4, 2)),
    (Vector2(9, -5), 2, Vector2(4.5, -2.5)),
])
def test_truediv(first, second, expected):
    assert (first / second) == expected


@pytest.mark.parametrize("first,second,expected", [
    (Vector2(8, 4), 2, Vector2(4, 2)),
    (Vector2(9, -5), 2, Vector2(4, -3)),
])
def test_floordiv(first, second, expected):
    assert (first // second) == expected
