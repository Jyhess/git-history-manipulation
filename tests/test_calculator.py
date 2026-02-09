"""Tests for the calculator module."""

import pytest
from src.calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for the add function."""
    
    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),      # positive numbers
        (-2, -3, -5),   # negative numbers
        (5, -3, 2),     # mixed numbers
    ])
    def test_add(self, a, b, expected):
        """Test adding two numbers."""
        assert add(a, b) == expected


class TestSubtract:
    """Tests for the subtract function."""
    
    @pytest.mark.parametrize("a, b, expected", [
        (5, 3, 2),      # positive numbers
        (-2, -3, 1),    # negative numbers
        (3, 5, -2),     # result negative
    ])
    def test_subtract(self, a, b, expected):
        """Test subtracting two numbers."""
        assert subtract(a, b) == expected


class TestMultiply:
    """Tests for the multiply function."""
    
    @pytest.mark.parametrize("a, b, expected", [
        (3, 4, 12),     # positive numbers
        (5, 0, 0),      # multiply by zero
        (-2, -3, 6),    # both negative
        (-2, 3, -6),    # one negative
    ])
    def test_multiply(self, a, b, expected):
        """Test multiplying two numbers."""
        assert multiply(a, b) == expected


class TestDivide:
    """Tests for the divide function."""
    
    @pytest.mark.parametrize("a, b, expected", [
        (10, 2, 5),     # positive numbers
        (7, 2, 3.5),    # result float
    ])
    def test_divide(self, a, b, expected):
        """Test dividing two numbers."""
        assert divide(a, b) == expected
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
