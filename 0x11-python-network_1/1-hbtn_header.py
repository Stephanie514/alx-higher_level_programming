#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to
the URL and displays the value of the X-Request-Id variable
found in the header of the response.
"""
import sys
import urllib.request as req


if __name__ == "__main__":
    url = sys.argv[1]

    request = req.Request(url)
    with req.urlopen(request) as response:
        headers_dict = dict(response.getheaders())
        x_request_id = headers_dict.get("X-Request-Id")
        print(x_request_id)
