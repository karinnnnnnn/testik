import pytest


def test_int1_stupid():
    my_int = 2 + 4 - 3

    assert my_int == 3


sum_parameters = [
    (5, 13, 18),
    (2, 3, 5),
    (7, 16, 23),
]

@pytest.mark.parametrize("a,b,expected", sum_parameters)
def test_int2_sum(a, b, expected):
    s = a + b
    assert s == expected

def test_set1():
    s = {"one", "two"}

    assert len(s) == 2


set_parameters = [
    ({"one", "three"}, {"two"}, {"one", "two", "three"}),
]


@pytest.mark.parametrize("a,b,expected", set_parameters)
def test_set2(a, b, expected):
    z = a.union(b)

    assert z == expected