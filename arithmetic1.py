"""Math functions for calculator."""


def add(list_nums):
    """Return the sum of the numbers in list_nums."""
    sm = 0
    for num in list_nums:
        sm += num
    return sm

def subtract(list_nums):
    """Return the second number subtracted from the first."""
    sb = list_nums[0]
    for num in list_nums[1:]:
        sb -= num
    return sb

def multiply(list_nums):
    """Multiply the two inputs together."""
    mlt = 1
    for num in list_nums:
        mlt *= num
    return mlt


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    return num1 / num2


def square(num1):
    """Return the square of the input."""

    # Needs only one argument

    return num1 * num1


def cube(num1):
    """Return the cube of the input."""

    # Needs only one argument

    return num1 * num1 * num1


def power(num1, num2):
    """Raise num1 to the power of num and return the value."""

    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
