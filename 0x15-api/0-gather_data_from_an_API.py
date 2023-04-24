#!/usr/bin/python3
"""
This script accesses a REST API to retrieve information\
 about an employee's TODO list,
including their name and the tasks they have completed.
"""

import requests
import sys


if __name__ == '__main__':
    # Retrieve the employee ID from the command line arguments
    employee_id = sys.argv[1]

    # Build the URL to retrieve the employee's name
    base_url = "https://jsonplaceholder.typicode.com/users"
    name_url = f"{base_url}/{employee_id}"

    # Send a GET request to retrieve the employee's name
    name_response = requests.get(name_url)
    employee_name = name_response.json().get('name')

    # Build the URL to retrieve the employee's tasks
    todo_url = f"{name_url}/todos"

    # Send a GET request to retrieve the employee's tasks
    tasks_response = requests.get(todo_url)
    tasks = tasks_response.json()

    # Count the number of tasks that have been completed
    # and store them in a list
    num_done = 0
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            num_done += 1

    # Print the employee's name and the number of tasks they have completed
    total_tasks = len(tasks)
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_done, total_tasks))

    # Print the titles of the completed tasks
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
