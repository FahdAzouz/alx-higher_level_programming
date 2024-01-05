#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -sI "$1" | frep "Allow" | cut -d " " -f 2-
