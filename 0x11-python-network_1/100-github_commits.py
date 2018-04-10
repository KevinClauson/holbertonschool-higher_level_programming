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
        cnt = 0
        length = len(my_json)
        for i in range(len(my_json) - 1, 0, -1):
                sha = my_json[i].get('sha')
                commit_dic = my_json[i].get("commit")
                author = commit_dic.get("author")
                name = author.get("name")
                print("{} {}".format(sha, name))
                cnt += 1
                if cnt == 10:
                        break

if __name__ == "__main__":
        url = 'https://api.github.com/repos/'
        repo = sys.argv[1]
        owner = sys.argv[2]
        get_url(url, repo, owner)
