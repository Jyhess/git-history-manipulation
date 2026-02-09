"""A simple calculator module for demonstration purposes."""


def _binary_operation_doc(operation, result_desc, arg_a="First number", arg_b="Second number", raises=None):
    """Generate docstring for binary operations."""
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
    return doc


def add(a, b):
    return a + b

add.__doc__ = _binary_operation_doc(
    "Add two numbers together",
    "The sum of a and b"
)


def subtract(a, b):
    return a - b

subtract.__doc__ = _binary_operation_doc(
    "Subtract b from a",
    "The difference of a and b"
)


def multiply(a, b):
    return a * b

multiply.__doc__ = _binary_operation_doc(
    "Multiply two numbers together",
    "The product of a and b"
)


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

divide.__doc__ = _binary_operation_doc(
    "Divide a by b",
    "The quotient of a and b",
    arg_a="Numerator",
    arg_b="Denominator",
    raises="ValueError: If b is zero"
)
