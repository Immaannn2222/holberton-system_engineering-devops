#!/usr/bin/python3
"""HTTP WITH PYTHON"""


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
        name = i.get("name")
    compl_tasks = 0
    for j in list_json:
        if j.get("completed"):
            compl_tasks += 1
    print("Employee {} is done with tasks({}/{}):".format(name, compl_tasks,
          len(list_json)))
    for x in list_json:
        if x.get("completed"):
            print("\t" + " " + x.get("title"))
