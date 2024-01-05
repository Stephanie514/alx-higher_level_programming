#!/bin/bash
#This sends a GET request to URL with curl and displays body of the response
curl -s -w "%{http_code}\\n" "$1" | awk 'NR==1 && $1 == 200 {p=1} p'
