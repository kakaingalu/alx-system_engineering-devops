#!/usr/bin/python3

"""script to export data in the JSON format."""

import json
import requests

# check if this is main program
if __name__ == "__main__":

    # get information from api
    url = "https://jsonplaceholder.typicode.com/users/"
    users_dict = requests.get(url).json()

    # filename defination
    filename = "todo_all_employees.json"

    # dictionary defination
    dictionary = {}

    # loop through users_dict
    for data in users_dict:
       
        # get infomation on user's name
        user_name = data.get("username")

        # get information on user's id
        users_id = str(data.get("id"))

        # get information on todo list for the user
        request = requests.get(f"{url}{users_id}/todos").json()

        # assigning the key user_id in dictionary with empty list
        dictionary[users_id] = []

        # loop through request
        for item in request:
            # declare empty dictionary
            each_item = {}

            # assign each key with corresponding value
            each_item["username"] = user_name
            each_item["task"] = item.get("title")
            each_item["completed"] = item.get("completed")

            # append all keys and the values into the key users_id
            dictionary[users_id].append(each_item)

    # write the json file
    with open(filename, "w") as j_file:
        json.dump(dictionary, j_file)
