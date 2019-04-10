"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

# # No setup
# repeat forever:
#     read input
#     tokenize input
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token


# Your code goes here
import functools

while True:
    input_string = input('Type your calculator command \n')
    tokens = input_string.split(' ')
    # numbers_string = tokens.slice(1, -1, 1)
    # numbers_float = [float(i) for i in numbers_string]

    if tokens[0] == 'q':
        break

    elif tokens[0] == '+':
        print(add(float(tokens[1]), float(tokens[2])))
        # print (functools.reduce(lambda x,y: x + y, numbers_float))

    elif tokens[0] == '-':
        print(subtract(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == '*':
        print(multiply(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == '/':
        while tokens[2] == '0':
            input_string = input('Second number cannot be 0. Try again. \nType your calculator command \n')
            tokens = input_string.split(' ')
        print(divide(float(tokens[1]), float(tokens[2])))

    elif tokens[0] == "square":
        print(square(float(tokens[1])))

    elif tokens[0] == "cube":
        print(cube(float(tokens[1])))