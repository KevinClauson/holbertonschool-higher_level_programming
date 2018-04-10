#!/usr/bin/python3
"""
Python script that sends get request to github
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def get_url(url, user, pwd):
        """
        prints out github id
        """
        r = requests.get(url, auth=HTTPBasicAuth(user, pwd))
        my_json = r.json()
        print("{}".format(my_json.get("id")))

if __name__ == "__main__":
        url = 'https://api.github.com/user'
        user = sys.argv[1]
        pwd = sys.argv[2]
        get_url(url, user, pwd)
