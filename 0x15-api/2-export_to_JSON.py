#!/usr/bin/python3
"""This module returns information about an employee's TODO list progress."""


import requests
import json
from sys import argv


def employee_todo_progress():
    response = requests.get('https://jsonplaceholder.typicode.com/todos?',
                            params={'userId': argv[1]})
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    todos = response.json()
    completed_tasks = []
    for todo in todos:
        if todo['completed']:
            completed_tasks.append(todo)

    user_id = todos[0]['userId']
    tasks = []
    username = requests.get('https://jsonplaceholder.typicode.com/users',
                            params={'id': user_id}).json()[0]['username']
    for todo in todos:
        tasks.append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        })

    data = {
        str(user_id): tasks
    }

    file_name = f"{user_id}.json"
    with open(file_name, "w") as f:
        json.dump(data, f)

    print(f"JSON file {file_name} has been created successfully.")


if __name__ == "__main__":
    employee_todo_progress()
