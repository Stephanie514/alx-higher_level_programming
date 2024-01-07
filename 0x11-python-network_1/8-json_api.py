#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter. Sends a POST request to http://0.0.0.0:5000/search_user
with a given letter.
"""
import sys
import requests

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {"q": letter}

    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    if response.status_code != 200:
        print("Not a valid JSON")
    else:
        try:
            data = response.json()
            if not data:
                print("No result")
            else:
                print("[{}] {}".format(data.get("id"), data.get("name")))
        except ValueError:
            print("Not a valid JSON")
