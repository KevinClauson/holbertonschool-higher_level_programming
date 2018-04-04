#!/bin/bash
# takes in a URL, sends a request to URL, and displays size of body of response
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2
