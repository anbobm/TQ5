"""
Core math utilities.

This module provides small reusable math helpers.
"""

def add(a: float, b: float) -> float:
    """
    Add two numbers.

    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b


def factorial(n: int) -> int:
    """
    Compute the factorial of a non-negative integer.

    :param n: Non-negative integer
    :raises ValueError: If n is negative
    :return: n factorial
    """
    if n < 0:
        raise ValueError("n must be non-negative")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
