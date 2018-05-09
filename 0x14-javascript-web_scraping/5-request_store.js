#!/usr/bin/node
/* read and prints contents of a file */

let request = require('request');
let fs = require('fs');
let url = process.argv[2];
let file = process.argv[3];

request.get(url, function getText (error, response, body) {
  if (error) console.log(error);
  else {
    fs.writeFile(file, body, 'utf8', function (err) {
      if (err) console.log(err);
    });
  }
});
