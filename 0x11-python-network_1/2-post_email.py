#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8).
"""
import sys
import urllib.parse
import urllib.request as req


if __name__ == "__main__":
    target = sys.argv[1]
    email_data = {"email": sys.argv[2]}
    encoded_email = urllib.parse.urlencode(email_data).encode("ascii")

    request_obj = req.Request(target, encoded_email)
    with req.urlopen(request_obj) as response_obj:
        decoded_content = response_obj.read().decode("utf-8")
        print(decoded_content)
