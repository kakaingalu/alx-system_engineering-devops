#!/usr/bin/python3
"""script to export data in the JSON format."""

import csv
import requests
import json
from sys import argv


if __name__ == "__main__":
    """Get data from API"""
    response = requests.get('https://jsonplaceholder.typicode.com/todos?',
                            params={'userId': argv[1]})
    """Check for errors"""
    if response.status_code != 200:
        print(f"Error: {response.status_code}")

    """Parse data"""
    todos = response.json()
    completed_tasks = []

    """Extract completed tasks"""
    for todo in todos:
        if todo['completed']:
            completed_tasks.append(todo)

    user_id = todos[0]['userId']
    tasks = []

    """Get username"""
    username = requests.get('https://jsonplaceholder.typicode.com/users',
                            params={'id': user_id}).json()[0]['username']

    """Prepare data for JSON file"""
    for todo in todos:
        tasks.append({
            "task": todo['title'],
            "completed": todo['completed'],
            "username": username
        })

    data = {
        str(user_id): tasks
    }

    """Write data to JSON file"""
    file_name = f"{user_id}.json"
    with open(file_name, "w") as f:
        json.dump(data, f)

    print(f"JSON file {file_name} has been created successfully.")
