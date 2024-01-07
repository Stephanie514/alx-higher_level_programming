#!/usr/bin/python3
"""Python script that displays the X-Request-Id header
variable of a request to a given URL.
"""
import sys
import requests

if __name__ == "__main__":
    trget_url = sys.argv[1]

    response = requests.get(trget_url)
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)
