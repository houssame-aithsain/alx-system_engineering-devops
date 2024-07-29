#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of all employees
using a REST API and exports the data to a JSON file.
"""

import requests
import json

# URL to fetch data from
users_url = 'https://jsonplaceholder.typicode.com/users'
todos_url = 'https://jsonplaceholder.typicode.com/todos'

# Fetch data from the APIs
users_response = requests.get(users_url)
todos_response = requests.get(todos_url)

# Convert response to JSON
users = users_response.json()
todos = todos_response.json()

# Create a dictionary to hold the tasks for each user
tasks_dict = {}

# Populate the dictionary
for user in users:
    user_id = user['id']
    username = user['username']

    # List to hold tasks for the current user
    user_tasks = []

    for todo in todos:
        if todo['userId'] == user_id:
            task_info = {
                "username": username,
                "task": todo['title'],
                "completed": todo['completed']
            }
            user_tasks.append(task_info)

    tasks_dict[user_id] = user_tasks

# Export the data to a JSON file
with open('todo_all_employees.json', 'w') as json_file:
    json.dump(tasks_dict, json_file)
