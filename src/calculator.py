"""A simple calculator module for demonstration purposes."""

from functools import wraps


def binary_operation_doc(operation, result_desc, arg_a="First number", arg_b="Second number", raises=None):
    """Decorator to add standardized docstrings to binary operations."""
    def decorator(func):
        doc = f"""{operation}.
    
    Args:
        a: {arg_a}
        b: {arg_b}
        
    Returns:
        {result_desc}"""
        if raises:
            doc += f"""
        
    Raises:
        {raises}"""
        func.__doc__ = doc
        return func
    return decorator


@binary_operation_doc("Add two numbers together", "The sum of a and b")
def add(a, b):
    return a + b


@binary_operation_doc("Subtract b from a", "The difference of a and b")
def subtract(a, b):
    return a - b


@binary_operation_doc("Multiply two numbers together", "The product of a and b")
def multiply(a, b):
    return a * b


@binary_operation_doc(
    "Divide a by b",
    "The quotient of a and b",
    arg_a="Numerator",
    arg_b="Denominator",
    raises="ValueError: If b is zero"
)
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
