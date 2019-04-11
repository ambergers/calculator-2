"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic1 import *

import functools

def is_valid(list):
    if len(list) < 2:
        print('List must have at least 2 numbers in it. Try again. \n')
        return False
    try:
        num_list = [float(i) for i in list[1:]]
        return True
    except ValueError:
        print('List can only have numeric values. Try again. \n')
        return False

while True:
    input_string = input('Type your calculator command \n')
    tokens = input_string.split(' ')
    
    if tokens[0] == 'q':
        break

    while is_valid(tokens) == False:
        input_string = input('Type your calculator command \n')
        tokens = input_string.split(' ')

    num_list = [float(i) for i in tokens[1:]]
    

    if tokens[0] == '+':
        print(add(num_list))
        # print (functools.reduce(lambda x,y: x + y, numbers_float))

    elif tokens[0] == '-':
        print(subtract(num_list))

    elif tokens[0] == '*':
        print(multiply(num_list))

    elif tokens[0] == '/':
        while '0' in tokens[2:]:
            input_string = input('Only the first list item can be 0. Try again. \nType your calculator command \n')
            tokens = input_string.split(' ')
            num_list = [float(i) for i in tokens[1:]]

        print(divide(num_list))

    elif tokens[0] == 'power':
        print(power(num_list))

    elif tokens[0] == 'mod':
        print(mod(num_list))

