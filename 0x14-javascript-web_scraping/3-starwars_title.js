#!/usr/bin/node

const { FILE } = require('dns');
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const FilmId = process.argv[2];

request(url + FilmId, (err, response, data) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode == 200) {
    const body = JSON.parse(data);
    console.log(body.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
