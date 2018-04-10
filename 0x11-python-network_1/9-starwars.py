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
        my_json = r.json()
        num_result = my_json.get('count')
        print("Number of results: {}".format(num_result))
        if num_result > 0:
                names = my_json.get('results')
                for i in names:
                        print(i.get('name'))

if __name__ == "__main__":
        url = 'https://swapi.co/api/people/'
        name = sys.argv[1]
        get_url(url, name)
