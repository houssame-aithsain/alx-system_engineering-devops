#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of all employees
using a REST API and exports the data to a JSON file.
"""

import json
import requests

if __name__ == "__main__":
    # Fetch all users information
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Dictionary to hold all tasks for all users
    all_tasks = {}

    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        # Fetch tasks information for each user
        tasks_url = f"https://jsonplaceholder.typicode.com/\
            todos?userId={user_id}"
        tasks_response = requests.get(tasks_url)
        tasks_data = tasks_response.json()

        # Prepare data for JSON export
        tasks_list = []
        for task in tasks_data:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            tasks_list.append(task_dict)

        all_tasks[user_id] = tasks_list

    # Define the JSON file name
    json_file = "todo_all_employees.json"

    # Write data to the JSON file
    with open(json_file, mode='w') as file:
        json.dump(all_tasks, file)
