#!/usr/bin/python3
"""HTTP WITH PYTHON"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    """main"""
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos/',
                         params={"userId": argv[1]})
    user = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={"id": argv[1]})
    list_json = to_do.json()
    user_json = user.json()
    for i in user_json:
        user_name = i.get("username")
        i_d = i.get('id')
    usr = {i_d: []}
    with open(str(i_d) + '.json', mode='w') as f:
        for t in list_json:
            Dict = {}
            Dict = {"task": t.get("title"), "completed": t.get("completed"),
                    "username": user_name}
            usr[i_d].append(Dict)
        json.dump(usr, f)
