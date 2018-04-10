#!/usr/bin/python3
"""
Python script that sends POST request
"""

import sys
import requests


def get_url(url, name):
        """
        prints out header value
        """
        payload = { 'search': name}
        r = requests.get(url, params=payload)
        print(r.url)
        try:
                my_json = r.json()
                print("Number of results: {}".format(my_json['count']))
                for i in my_json['results']:
                        print(i['name'])
        except:
                print("Not a valid JSON")

if __name__ == "__main__":
        url = 'https://swapi.co/api/people/'
        name = sys.argv[1]
        get_url(url, name)
