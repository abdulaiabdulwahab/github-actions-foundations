def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def divide(a, b):
    """Divide a by b."""

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b