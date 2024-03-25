#!/usr/bin/python3
"""Returns List of To-do of Employee ID"""
import requests;
import sys;

def get_todo_list(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(url + "users/{}".format(employee_id))
    todos_response = requests.get(url + "todos", params={"userId": employee_id})

    if user_response.status_code == 200 and todos_response.status_code == 200:
        user_data = user_response.json()
        todo_data = todos_response.json()

        completed_tasks = [task for task in todo_data if task['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todo_data)

        print("Employee {} is done with tasks ({}/{}):".format(
            user_data.get("name"), num_completed_tasks, total_tasks))
        for task in completed_tasks:
            print("\t{}".format(task['title']))
    else:
        print("Failed to retrieve data. Please check the employee ID.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
    else:
        employee_id = sys.argv[1]
        get_todo_list(employee_id)