#!/usr/bin/node

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completed = {};
    content = JSON.parse(body);
    for (const i in content) {
      const task = content[i];
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('Error has occured, Status Code: ' + response.statusCode);
  }
});
