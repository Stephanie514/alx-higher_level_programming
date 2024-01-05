#!/bin/bash
#This one sends a request to URL and then displays size of body of the response
curl -sI "$1" | awk '/Content-Length/ {print $2}' | tr -d '\r\n'
