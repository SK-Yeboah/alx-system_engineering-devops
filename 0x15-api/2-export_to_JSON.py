#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""
import json
import requests
import sys

def export_todo_to_json(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    todos_response = requests.get(url + "todos", params={"userId": employee_id})

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to retrieve data. Please check the employee ID.")
        return

    user_data = user_response.json()
    username = user_data.get("username")
    todo_data = todos_response.json()

    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump({employee_id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        } for task in todo_data]}, jsonfile, indent=4)

    print(f"Todo list for Employee {username} has been exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
    else:
        employee_id = sys.argv[1]
        export_todo_to_json(employee_id)
