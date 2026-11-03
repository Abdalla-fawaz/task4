
import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# ADDITION TESTS

def test_add_positive(calc):
    assert calc.add(5, 3) == 8

def test_add_negative(calc):
    assert calc.add(-5, -3) == -8

def test_add_positive_negative(calc):
    assert calc.add(5, -3) == 2

def test_add_zero(calc):
    assert calc.add(5, 0) == 5

def test_add_decimals(calc):
    assert calc.add(2.5, 1.5) == 4.0


# SUBTRACTION TESTS

def test_subtract_positive(calc):
    assert calc.subtract(10, 5) == 5

def test_subtract_negative(calc):
    assert calc.subtract(-5, -3) == -2

def test_subtract_result_negative(calc):
    assert calc.subtract(3, 8) == -5

def test_subtract_zero(calc):
    assert calc.subtract(5, 0) == 5

def test_subtract_decimals(calc):
    assert calc.subtract(5.5, 2.5) == 3.0


# MULTIPLICATION TESTS

def test_multiply_positive(calc):
    assert calc.multiply(5, 3) == 15

def test_multiply_negative(calc):
    assert calc.multiply(-5, -3) == 15

def test_multiply_positive_negative(calc):
    assert calc.multiply(5, -3) == -15

def test_multiply_by_zero(calc):
    assert calc.multiply(100, 0) == 0

def test_multiply_decimals(calc):
    assert calc.multiply(2.5, 2) == 5.0


# DIVISION TESTS

def test_divide_positive(calc):
    assert calc.divide(10, 2) == 5

def test_divide_negative(calc):
    assert calc.divide(-10, 2) == -5

def test_divide_decimals(calc):
    assert calc.divide(5, 2) == 2.5

def test_divide_zero_numerator(calc):
    assert calc.divide(0, 5) == 0

def test_divide_by_zero(calc):
    with pytest.raises(ValueError):
        calc.divide(10, 0)


# ADDITIONAL EDGE CASES

def test_large_numbers(calc):
    assert calc.add(1000000, 2000000) == 3000000

def test_divide_same_number(calc):
    assert calc.divide(10, 10) == 1
