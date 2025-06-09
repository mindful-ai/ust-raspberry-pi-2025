import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, -1) == -2

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(4, 6) == -2

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-3, 2) == -6

def test_divide(calc):
    assert calc.divide(12, 3) == 4
    assert calc.divide(5, 2) == 2.5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)