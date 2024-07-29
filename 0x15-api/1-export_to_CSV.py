#!/usr/bin/python3
"""
Export data in the CSV format.
"""
import csv
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

    # Define the CSV file name
    csv_file = f"{user_id}.csv"

    # Write data to the CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in tasks_data:
            writer.writerow([user_id, username,
                             task.get("completed"), task.get("title")])
