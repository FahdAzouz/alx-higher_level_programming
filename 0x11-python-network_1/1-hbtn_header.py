#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    from urllib import request
    import sys
    url = sys.argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
