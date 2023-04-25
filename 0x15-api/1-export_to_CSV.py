#!/usr/bin/python3
"""This module exports a TODO list progress of an employee to CSV format"""

from sys import argv
import csv
import requests


if __name__ == '__main__':
    # Retrieve the user ID from the command line argument
    user_id = argv[1]
    # Construct the URL to retrieve the user's information
    user_info_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        user_id)

    # Make a request to the API and extract the user's username
    user_response = requests.get(user_info_url)
    user_username = user_response.json().get('username')

    # Construct the URL to retrieve the user's tasks
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    user_tasks_url = url.format(user_id)

    # Make a request to the API and convert the response to a JSON object
    user_tasks = requests.get(user_tasks_url).json()

    # Create a new CSV file and write the user's tasks to it
    with open(
              '{}.csv'.format(user_id),
              'w',
              encoding='UTF8',
              newline=''
             ) as csv_file:
        # Create a CSV writer object with quoting set to QUOTE_ALL
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Loop through the tasks and write each one to a row in the CSV file
        for task in user_tasks:
            task_completed = task.get('completed')
            task_title = task.get('title')
            csv_writer.writerow([
                user_id,
                user_username,
                task_completed,
                task_title
            ])
