#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.
"""
import json
import requests

def export_todo_all_employees():
    url = "https://jsonplaceholder.typicode.com/"
    users_response = requests.get(url + "users")
    if users_response.status_code != 200:
        print("Failed to retrieve user data from the API.")
        return

    users_data = users_response.json()

    todo_data_all_employees = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")

        todos_response = requests.get(url + "todos", params={"userId": user_id})
        if todos_response.status_code == 200:
            todos_data = todos_response.json()
            user_tasks = [{"task": task.get("title"),
                           "completed": task.get("completed"),
                           "username": username} for task in todos_data]
            todo_data_all_employees[user_id] = user_tasks
        else:
            print(f"Failed to retrieve todo data for user ID: {user_id}")

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(todo_data_all_employees, jsonfile, indent=4)

    print(f"To-do list for all employees has been exported to {filename}")

if __name__ == "__main__":
    export_todo_all_employees()
