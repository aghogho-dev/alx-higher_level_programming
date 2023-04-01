#!/usr/bin/bash
# bash script to display body of response
curl -sS "$1" | grep -q "HTTP/1.1 200 OK" && curl -sS "$1" | sed -n '/^$/,$p'
