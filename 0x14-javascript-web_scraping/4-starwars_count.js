#!/usr/bin/node
/* read and prints contents of a file */

let url;
let request = require('request');
let incomingUrl = process.argv[2];
if (incomingUrl == 'http://swapi.co/api/films') {
  url = 'https://swapi.co/api/people/18/';
} else {
  url = incomingUrl;
}

request.get(url, function getUrl (error, response, body) {
  if (error) console.log(error);
  else if (response && body) {
    let bodyParse = JSON.parse(body);
    console.log(bodyParse['films'].length);
  }
});
