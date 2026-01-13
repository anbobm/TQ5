# Docstrings und die verschiedenen Konventionen

# reST / sphinx native
def add(a, b):
    """
    Add two numbers.

    :param a: First number
    :type a: int
    :param b: Second number
    :type b: int
    :return: The sum
    :rtype: int
    """

# Google Style (unterstützt von sphinx' napoleon Extension)
def add(a, b):
    """
    Add two numbers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: The sum
    """

# NumPy Style (unterstützt von sphinx' napoleon Extension)
def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : int
        First number
    b : int
        Second number

    Returns
    -------
    int
        The sum
    """
