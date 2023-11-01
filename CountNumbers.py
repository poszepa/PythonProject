"""
Here I'm testing simple use *args
"""

def sum_numbers(*arg):
    sum = 0
    for number in arg:
        sum += number
    return sum
