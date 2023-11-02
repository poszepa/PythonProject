import enum

"""
1. create a list named `tasks` that contains several string elements, each of which represents a task to be performed.

2. use a for loop and the `enumerate` function to browse through the list of tasks. For each iteration, print the index and the task.

3. Search the Internet for how to change the starting point of the enumerate function. Modify the for loop to use a starting index of 1 instead of 0 for the enumerate.

4. again modify the loop so that the first letter of each task in the list is capitalized and print it.
"""

tasks = ["clean the room", "out rubbish", "cook a cake"]

def print_list_tasks(list_task):
    enumerate_list = enumerate(list_task,start = 1)
    for index_task, task in enumerate_list:
        print(index_task,":", task)

