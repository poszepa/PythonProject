"""
Write a program, which calculate sum every number from 1 to input a number.
"""
import time


def sumNumberInRange(endOfRange):
    return sum(range(1, endOfRange + 1))


def sumNumberInLoop(endOfRange):
    sum = 0
    for number in range(1, endOfRange + 1):
        sum += number
    return sum

def sumNumberInGenerator(endOfRange):
    numberGenerator = [
        number
        for number in range(1, endOfRange + 1)
    ]
    return sum(numberGenerator)

def sumNumberByArythmetic(endOfRange):
    return (1 + endOfRange) / 2 * endOfRange