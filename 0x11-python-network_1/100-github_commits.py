#!/usr/bin/python3
"""
Python script that sends get request to github
"""
import sys
import requests


def get_url(url, repo, owner):
        """
        prints out github commits
        """
        url += repo + '/' + owner + "/commits"
        r = requests.get(url)
        my_json = r.json()
        my_list = []
        for rec in my_json:
                sha = rec.get('sha')
                commit_dic = rec.get("commit")
                author = commit_dic.get("author")
                name = author.get("name")
                print("{} {}".format(sha, name))

if __name__ == "__main__":
        url = 'https://api.github.com/repos/'
        repo = sys.argv[1]
        owner = sys.argv[2]
        get_url(url, repo, owner)
