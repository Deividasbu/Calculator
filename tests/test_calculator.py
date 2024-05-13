from calculator.calculator import Calculator
import pytest


def test_value():
    c = Calculator(value=6)
    ans = c.value
    assert ans == 6


def test_set_value():
    c = Calculator()
    c.value = 5
    with pytest.raises(ValueError):
        c.value = 'test text'
    assert c.value == 5


def test_reset_value():
    c = Calculator(value=50)
    c.reset_value()
    assert c.value == 0


def test_add():
    c = Calculator(1000)
    with pytest.raises(ValueError):
        c.add('test text')
    assert c.add(100) == 1100


def test_subtract():
    c = Calculator(1000)
    with pytest.raises(ValueError):
        c.subtract('test text')
    assert c.subtract(100) == 900


def test_multiply():
    c = Calculator(1000)
    with pytest.raises(ValueError):
        c.add('test text')
    assert c.multiply(5) == 5000


def test_divide():
    c = Calculator(1000)
    with pytest.raises(ValueError):
        c.add('test text')
    assert c.divide(10) == 100


def test_n_root():
    c = Calculator(10000)
    with pytest.raises(ValueError):
        c.add('test text')
    assert c.n_root(2) == 100