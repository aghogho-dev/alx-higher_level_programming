#!/usr/bin/bash
# bash script to display body of response
curl -s -o /dev/null -w "%{http_code}\n{body}" "$1" | awk 'NR==1{if($0!=200) exit} NR>1{print}'
