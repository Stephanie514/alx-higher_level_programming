#!/bin/bash
#This deletes request to URL passed as first argument and displays body of the response
curl -s -X DELETE "$1"
