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


def divide(list_nums):
    """Divide the first input by the second, returning a floating point."""
    div = list_nums[0]
    for num in list_nums[1:]:
        div /= num
    return div

def power(list_nums):
    """Raise num1 to the power of num and return the value."""
    pwr = list_nums[0]
    for num in list_nums[1:]:
        pwr **= num
    return pwr
    

def mod(num1, num2):
    """Return the remainder of num / num2."""

    return num1 % num2
