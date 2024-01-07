#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value of the"""

import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
