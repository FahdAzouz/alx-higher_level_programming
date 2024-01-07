#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    response = requests.get("https://github.com/repos/{}/{}/commits".format(owner, repo))
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get('sha'),
                                  commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
