import addition
import pytest


def test_add():
    assert addition.add(4, 5) != 8

def test_sub():
    assert addition.sub(4, 5) < 0