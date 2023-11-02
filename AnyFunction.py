#Use function any to define list have even number


numbers1 = [1, 3, 5, 6, 7]
numbers2 = [1, 3, 5, 7, 9]

#Without any

def any_even(arg):
    for number in arg:
        if(number % 2 == 0):
            return True
    return False


# Below we check every number is even
def any_even_second_version(arg):
    return any((
        number % 2 == 0
        for number in arg
    ))


kamil = {
    'name' : 'Kamil',
    'age' : 27,
    'skills' : ['Python', 'JS', 'C++']
}

Nikola = {
    'name' : 'Nikol',
    'age' : 35,
    'skills' : ['Python', 'Ruby', 'C#']
}

def have_programming_skills(*arg, skill = 'JS'):
    return any((
        skill in person.get('skills')
        for person in arg
    ))


def have_required_skills(persons, skills = ['Python', 'JS']):
    return all([
        skill in persons.get('skills')
        for skill in skills
    ])









