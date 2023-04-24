#!/usr/bin/python3
"""This module returns information about employee's TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    # Retrieve the employee ID from the command line arguments
    employee_id = sys.argv[1]

    # Create the URL to retrieve the TODO list for the
    # employee with the given ID
    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": employee_id}
    response = requests.get(url, params=params)

    # If the request was successful (status code 200),
    # extract the completed tasks
    if response.status_code == 200:
        todos = response.json()
        completed = []
        for todo in todos:
            if todo["completed"]:
                completed.append(todo["title"])

        # Retrieve the employee name from the API and calculate task statistics
        employee_name = (
            requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(employee_id)).json()["name"]
        )
        total_tasks = len(todos)
        num_completed = len(completed)

        # Print the task statistics and list of completed tasks
        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, num_completed, total_tasks))
        for task in completed:
            print("\t {}".format(task))
    else:
        # If the request was unsuccessful, print an error message
        print("User not found")
