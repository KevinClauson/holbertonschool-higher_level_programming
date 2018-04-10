#!/usr/bin/python3
"""
Python script that sends GET search to twitter api
"""

import sys
import requests
import base64


def get_url(url, api, secret, search):
        """
        prints out header value
        """
        payload = {'search': name, 'include': 'metadata'}
        r = requests.get(url, params=payload)
        my_json = r.json()
        num_result = my_json.get('count')
        print("Number of results: {}".format(num_result))
        if num_result == 0:
                return
        while True:
                next = my_json.get('next')
                names = my_json.get('results')
                for i in names:
                        print(i.get('name'))
                        films = (i.get('films'))
                        for f in films:
                                rec = requests.get(f)
                                j = rec.json()
                                print("\t{}".format(j.get('title')))
                if next is None:
                        break
                else:
                        r = requests.get(next)
                        my_json = r.json()

if __name__ == "__main__":
        url = 'https://swapi.co/api/people/'
        api = sys.argv[1]
        secret = sys.argv[2]
        search = sys.argv[3]
        get_url(url, api, secret, search)
