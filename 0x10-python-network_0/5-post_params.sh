#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
var1="test@gmail.com"
var2="I will always be here for PLD"
curl -s -X POST -d "email=$var1&subject=$var2" "$1"
