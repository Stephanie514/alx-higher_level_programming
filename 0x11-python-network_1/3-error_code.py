#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
to the URL and displays the body of the response
(decoded in utf-8)
  - Handles HTTP errors.
"""
import sys
import urllib.error
import urllib.request as req


if __name__ == "__main__":
    target_url = sys.argv[1]

    try:
        request_obj = req.Request(target_url)
        response_obj = req.urlopen(request_obj)
        print(response_obj.read().decode("utf-8"))
        response_obj.close()
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
