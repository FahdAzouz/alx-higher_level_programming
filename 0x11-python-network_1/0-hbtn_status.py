#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.Request(url) as response:
    html = response.read()