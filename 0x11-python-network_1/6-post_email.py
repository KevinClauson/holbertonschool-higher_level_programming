#!/usr/bin/python3
"""
Python script that sends POST request
"""

import sys
import requests


def get_url(url, email):
    """
    prints out header value
    """
    payload = {'email': email}
    r = requests.post(url, data=payload)
    print("{}".format(r.text))

if __name__ == "__main__":
    get_url(sys.argv[1], sys.argv[2])
