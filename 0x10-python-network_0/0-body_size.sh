#!/bin/bash
# Get the body size of the response
curl -s "$1" | wc -c
