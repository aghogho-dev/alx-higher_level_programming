#!/bin/bash
# Sends a request to a URL passed as an argument, dispay status code
curl -so /dev/null -w "%{http_code}" "$1"
