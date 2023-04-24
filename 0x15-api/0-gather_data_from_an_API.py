import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/todos"
    params = {"userId": employee_id}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        todos = response.json()
        completed = []
        for todo in todos:
            if todo["completed"]:
                completed.append(todo["title"])

        employee_name = (
            requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(employee_id)).json()["name"]
        )
        total_tasks = len(todos)
        num_completed = len(completed)

        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, num_completed, total_tasks))
        for task in completed:
            print("\t {}".format(task))
    else:
        print("User not found")
