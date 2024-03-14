#!/usr/bin/python3

''' Module for retrieving API data'''

import requests
import sys

if __name__ == '__main__':

    def retreive_tasks(employee_id):

        site_url = "https://jsonplaceholder.typicode.com/"
        employee_url = f"{site_url}/users/{employee_id}"
        todo_url = f"{site_url}/todos"

        employee_response = requests.get(base_url+user_ext)
        employee = employee_response.json()
        todo_response = requests.get(base_url+user_ext+todo_ext)
        todos = todo_response.json()
        completed = 0
        total = 0
        for todo in todos:
            total += 1
            if todo['completed'] is True:
                completed += 1

        print("Employee {0} is done with tasks({1}/{2}):".format(
            employee['name'], completed, total
            ))
        for todo in todos:
            if todo['completed'] is True:
                print("\t {}".format(todo['title']))
