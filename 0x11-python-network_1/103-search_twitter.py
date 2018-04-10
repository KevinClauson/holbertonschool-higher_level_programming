#!/usr/bin/python3
"""
Python script that sends GET search to twitter api
"""

import sys
import requests
from requests.auth import HTTPBasicAuth
import base64


def get_url(url, api, secret, search):
        """
        prints out header value
        """
        set_of = api + ':' + secret
        my_data = base64.b64encode(set_of.encode('ascii'))
        header = {"Authorization": "Basic {}".format(my_data.decode()),
                  "Content-Type": "application/x-www-form-urlencoded;\
                  charset=UTF-8"}
        body = {"grant_type": "client_credentials"}
        r = requests.post(url, headers=header, data=body)
        my_json = r.json()
        token = my_json.get("access_token")
        new_header = {"Authorization": "Bearer {}".format(token)}
        new_url = "https://api.twitter.com/1.1/search/tweets.json"
        payload = {'q': search}
        re = requests.get(new_url, headers=new_header, params=payload)
        new_json = re.json()
        final_json = new_json.get('statuses')
        cnt = 0
        for tweet in final_json:
                t_id = tweet.get("id_str")
                t_text = tweet.get("text")
                user = tweet.get("user")
                t_owner = user.get('name')
                print("[{}] {} by {}".format(t_id, t_text, t_owner))
                cnt += 1
                if cnt == 5:
                        break

if __name__ == "__main__":
        url = 'https://api.twitter.com/oauth2/token'
        api = sys.argv[1]
        secret = sys.argv[2]
        search = sys.argv[3]
        get_url(url, api, secret, search)
