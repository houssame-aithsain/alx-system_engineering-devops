#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of an employee
using a REST API and exports the data to a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get the user ID from the command line argument
    user_id = sys.argv[1]

    # Fetch user information
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch tasks information
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    tasks_response = requests.get(tasks_url)
    tasks_data = tasks_response.json()

    # Prepare data for JSON export
    tasks_list = []
    for task in tasks_data:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        tasks_list.append(task_dict)

    json_data = {user_id: tasks_list}

    # Define the JSON file name
    json_file = f"{user_id}.json"

    # Write data to the JSON file
    with open(json_file, mode='w') as file:
        json.dump(json_data, file)
