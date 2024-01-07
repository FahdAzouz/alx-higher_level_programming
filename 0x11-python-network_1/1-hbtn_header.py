#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    from urllib import request
    import sys
    url = sys.argv[1]
    with request.urlopen(url) as response:
        response = response.info()
        print(response['X-Resquest-Id'])
