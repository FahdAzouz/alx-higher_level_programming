#!/usr/bin/python3
"""Takes in a URL and an email address,
sends a POST request to the passed URL"""

if __name__ == "__main__":
    from urllib import request, error
    import sys

    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
