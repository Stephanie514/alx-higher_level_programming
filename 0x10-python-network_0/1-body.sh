#!/bin/bash
#This sends a GET request to URL with curl and displays body of the response
curl -s -o response.txt -w "%{http_code}" "$1" && [ "$(cat response.txt)" = "200" ] && tail -n +2 response.txt
