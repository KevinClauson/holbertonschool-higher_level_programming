#!/usr/bin/python3
"""
Python script that sends POST request
"""

import sys
import requests


def get_url(url, q):
        """
        prints out header value
        """
        payload = {'q': q}
        r = requests.post(url, data=payload)
        try:
                my_json = r.json()
                if my_json:
                    print("[{}] {}".format(my_json['id'], my_json['name']))
                else:
                        print("No result")
        except:
                print("Not a valid JSON")

if __name__ == "__main__":
        url = 'http://0.0.0.0:5000/search_user'
        q = ""
        try:
                q = sys.argv[1]
        except:
                pass
        get_url(url, q)
