#!/usr/bin/node
/* read and prints contents of a file */

let url = 'https://swapi.co/api/people/18/';
let request = require('request');

request.get(url, function getUrl (error, response, body) {
  if (error) console.log(error);
  else {
    let bodyParse = JSON.parse(body);
    console.log(bodyParse['films'].length);
  }
});
