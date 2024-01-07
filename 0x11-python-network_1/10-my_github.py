#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id Uses the GitHub API to display
a GitHub ID based on given credentials.
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    URL = "https://api.github.com/user"
    AUTH = (username, password)
    response = requests.get(URL, AUTH=AUTH)

    if response.stat_code == 200:
        user_id = response.json().get("id")
        print(user_id)
    else:
        print("Error fetching user info. Status code:", response.stat_code)
