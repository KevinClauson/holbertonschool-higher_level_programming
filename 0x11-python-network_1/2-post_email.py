#!/usr/bin/python3
"""
Python script that sends POST request
"""

import sys
from urllib import request, parse


def get_url(url, email):
    """
    prints out header value
    """
    values = {'email': email}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        resp = response.read()
    print("{}".format(resp.decode('utf8')))

if __name__ == "__main__":
    get_url(sys.argv[1], sys.argv[2])
