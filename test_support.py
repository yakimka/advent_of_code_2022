import pytest

from support import Vector2


@pytest.mark.parametrize("first,second,expected", [
    (Vector2(1, 1), Vector2(0, 1), Vector2(1, 2)),
    (Vector2(1, 1), (0, 1), Vector2(1, 2)),
    ((1, 1), Vector2(0, 1), Vector2(1, 2)),
])
def test_add(first, second, expected):
    assert first + second == expected
