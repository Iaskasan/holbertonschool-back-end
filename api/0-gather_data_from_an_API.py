#!/bin/bash/python3

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])
    response = requests.get(url)
    data = response.json()
    name = data.get("name")
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(sys.argv[1])
    response = requests.get(url)
    data = response.json()
    total = len(data)
    done = len([task for task in data if task.get("completed")])
    print("Employee {} is done with tasks({}/{}):".format(name, done, total))
    for task in data:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
            
