import random
import collections


# Random float number
def random_float(start_range, end_range):
    return random.uniform(start_range, end_range)

# Random int number
def random_float(start_range, end_range):
    return random.randrange(start_range, end_range)

nameList = ["Kamil", "Wojtek", "Nikodem", "Anita", "Tomek"]

def random_choice(list):
    return random.choice(nameList)

def random_choices(list):
    return random.choices(nameList, [10,10,50,25,25], k= 2000)

def count_element(list):
    return collections.Counter(list)

