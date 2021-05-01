from quadratic_equation import *
import pytest


@pytest.mark.square
def test_square():
    num = 25
    assert sqrt(num) == 5


@pytest.mark.square
def test_mul():
    num = 7
    assert 7 * 7 == 40


@pytest.mark.others
def test_quality():
    assert 10 == 11
