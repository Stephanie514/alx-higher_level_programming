#!/bin/bash
# This displays only the status code of the response.
output=$(mktemp); curl -s -o "$output" "$1" & wait && status_code=$(awk 'NR==1{print $2}' "$output") && rm "$output" && echo "$status_code"
