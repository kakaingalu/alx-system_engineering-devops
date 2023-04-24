#!/usr/bin/python3
"""This module exports a TODO list progress of an employee to CSV format"""

import requests
import csv
from sys import argv


def employee_todo_progress():
    response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1])
    )
    if response.status_code != 200:
        print('Error: {}'.format(response.status_code))
        return

    todos = response.json()
    user_id = todos[0]['userId']
    file_name = '{}.csv'.format(user_id)

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file, 
                            delimiter=',', 
                            quotechar='"',
                            quoting=csv.QUOTE_ALL
        )
        writer.writerow([
            'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'
        ])
        for todo in todos:
            writer.writerow([
                todo['userId'], 'username', todo['completed'], todo['title']
            ])

    print('CSV file {} has been created successfully.'.format(file_name))


if __name__ == '__main__':
    employee_todo_progress()
