#!/bin/bash
#This one sends a request to URL and then displays size of body of the response
curl -s "$1" | wc -c
