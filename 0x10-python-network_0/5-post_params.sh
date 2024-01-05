#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
var1="test@gmail.com"
var2="I will always be here for PLD"
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
