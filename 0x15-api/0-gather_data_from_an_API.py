#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of an employee
using a REST API.
"""

import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        return

    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee data
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url).json()
    employee_name = user_response.get("name")

    # Fetch TODO list data
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url).json()

    # Calculate the number of completed tasks and total tasks
    total_tasks = len(todos_response)
    done_tasks = [task for task in todos_response if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Print the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    # Print the titles of completed tasks
    for task in done_tasks:
        print("\t {}".format(task.get("title")))

if __name__ == "__main__":
    main()
