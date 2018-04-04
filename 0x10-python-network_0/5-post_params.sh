#!/bin/bash
# takes in URL sends a POST request to the passed URL displays body of response
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
