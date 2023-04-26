#!/usr/bin/python3
"""script to export data in the JSON format."""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":

    # intialization of the userid from terminal
    user_id = argv[1]

    # get information of user from the api
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'
    request = requests.get(user_url.format(user_id)).json()

    # extract username
    user_name = request.get('username')

    # get information of todo list of users from api
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todos = requests.get(todos_url.format(user_id)).json()

    # Json file name defination
    file_name = user_id + ".json"

    # create list to store tasks
    task_lists = []

    # loop through todo assigning the title, completed and username of tasks
    # into the task_lists
    for todo in todos:
        copy_dict = {}
        copy_dict["task"] = todo.get('title')
        copy_dict["completed"] = todo.get('completed')
        copy_dict["username"] = user_name
        task_lists.append(copy_dict)

    # store the list into a dictonary with key = user_id
    dict_name = {}
    dict_name[user_id] = task_lists

    # write to json file
    with open(file_name, "w") as j_file:
        json.dump(dict_name, j_file)
