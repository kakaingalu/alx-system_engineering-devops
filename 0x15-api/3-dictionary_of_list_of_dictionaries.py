#!/usr/bin/python3
"""This module returns information about employee's TODO list progress"""

import requests
import json


def all_employees_todo_progress():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    todos = response.json()
    tasks = {}
    for todo in todos:
        user_id = todo['userId']
        if user_id not in tasks:
            tasks[user_id] = []
        tasks[user_id].append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": ""
        })

    # Now, for each user ID, we need to get the username
    for user_id in tasks:
        response = requests.get('https://jsonplaceholder.typicode.com/users/' +
                                f'{user_id}')

        if response.status_code == 200:
            username = response.json()['username']
            for task in tasks[user_id]:
                task['username'] = username
        else:
            print(f"Error: could not retrieve username for user ID {user_id}")

    # Export the tasks to a JSON file
    file_name = 'todo_all_employees.json'
    with open(file_name, mode='w') as file:
        json.dump(tasks, file)

    print(f"JSON file {file_name} has been created successfully.")
    return


if __name__ == "__main__":
    all_employees_todo_progress()
