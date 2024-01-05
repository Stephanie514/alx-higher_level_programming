#!/bin/bash
#Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
(curl -s -o >(awk 'NR==1{print $2}' >&2) -w "%{http_code}" "$1" > /dev/null)
