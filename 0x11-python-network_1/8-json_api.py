#!/usr/bin/python3
"""Takes in a letter and sends a POST request to http://
0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(url, data={'q': q})
    if response.headers.get('content-type') != 'application/json':
        print("Not a valid JSON")
    elif response.json() == {}:
        print('No result')
    else:
        print('[{}] {}'.format(response.json().get('id'),
                               response.json().get('name')))
