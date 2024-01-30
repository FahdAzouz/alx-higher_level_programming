#!/usr/bin/node

const { request } = require('http');

fs = require('fs');
request = require('request');

request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
