#!/usr/bin/python3
"""HTTP WITH PYTHON"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """main"""
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos/')
    user = requests.get('https://jsonplaceholder.typicode.com/users')
    list_json = to_do.json()
    user_json = user.json()
    usr = {}
    with open('todo_all_employees' + '.json', mode='w') as f:
        for i in user_json:
            user_name = i.get("username")
            i_d = i.get('id')
            usr[i_d] = []
            for t in list_json:
                if i_d == t['userId']:
                    Dict = {}
                    Dict = {"username": user_name, "task": t.get("title"),
                            "completed": t.get("completed")}
                    usr[i_d].append(Dict)
        json.dump(usr, f)
