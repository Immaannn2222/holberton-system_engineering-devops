#!/usr/bin/python3
"""HTTP WITH PYTHON"""
import csv
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
        i_d = i.get('id')
    with open(str(i_d) + '.csv', mode='w') as f:
        csv = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for t in list_json:
            status = t.get("completed")
            task_title = t.get("title")
            csv.writerow([i_d, name, status, task_title])
