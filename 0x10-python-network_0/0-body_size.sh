#!/usr/bin/bash


if [ $# -eq 0 ]; then
	echo "Usage: $0 <url>"
	exit 1
fi

url=$1

response_body=$(curl -s $url)

body_size=$(echo -n "$response_body" | wc -c)

echo "$body_size"
