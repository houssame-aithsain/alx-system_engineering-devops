#!/usr/bin/python3
"""
This script fetches and displays the TODO list progress of an employee
using a REST API and exports the data to a CSV file.
"""

import csv
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

    # Open CSV file for writing
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write tasks to CSV file
        for task in todos_response:
            csv_writer.writerow([employee_id, employee_name,
                                 task.get("completed"), task.get("title")])


if __name__ == "__main__":
    main()
