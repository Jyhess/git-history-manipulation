"""Tests for the calculator module."""

import pytest
from src.calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5
    
    def test_add_mixed_numbers(self):
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2


class TestSubtract:
    """Tests for the subtract function."""
    
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2
    
    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        assert subtract(-2, -3) == 1
    
    def test_subtract_result_negative(self):
        """Test subtraction resulting in negative number."""
        assert subtract(3, 5) == -2


class TestMultiply:
    """Tests for the multiply function."""
    
    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(3, 4) == 12
    
    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, -3) == 6
        assert multiply(-2, 3) == -6


class TestDivide:
    """Tests for the divide function."""
    
    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5
    
    def test_divide_result_float(self):
        """Test division resulting in float."""
        assert divide(7, 2) == 3.5
    
    def test_divide_by_zero(self):
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)
