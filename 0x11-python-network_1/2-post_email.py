#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response"""

if __name__ == "__main__":
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode("ascii")
    with request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
