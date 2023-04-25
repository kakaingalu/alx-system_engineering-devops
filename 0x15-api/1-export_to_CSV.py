#!/usr/bin/python3
"""This module exports a TODO list progress of an employee to CSV format"""

from sys import argv
import csv
import requests


def employee_todo_progress():
    # Make an HTTP GET request to retrieve the employee's
    # to-do list from the REST API
    response = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1])
    )

    # If the response status code is not 200 (OK), print an
    # error message and return
    if response.status_code != 200:
        print('Error: {}'.format(response.status_code))
        return

    # Extract the to-do list items from the response JSON
    # and the user ID from the first item
    todos = response.json()
    user_id = todos[0]['userId']

    # Construct the file name for the CSV file using the user ID
    file_name = '{}.csv'.format(user_id)

    # Open the CSV file for writing and create a CSV writer object
    # with the appropriate settings
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL
                            )

        # Write a header row to the CSV file with column names
        writer.writerow([
            'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'
        ])

        # Iterate over the to-do list items and write each one as a row
        # in the CSV file
        for todo in todos:
            writer.writerow([
                todo['userId'], 'username', todo['completed'], todo['title']
            ])

    # Print a success message with the name of the CSV file that was created
    print('CSV file {} has been created successfully.'.format(file_name))


# Check if this module is being run as the main program,
# and if so, call the employee_todo_progress function
if __name__ == '__main__':
    employee_todo_progress()
