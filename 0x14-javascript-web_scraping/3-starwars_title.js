#!/usr/bin/node
/* read and prints contents of a file */

let num;
if (process.argv[2]) num = process.argv[2];
else num = '';
let request = require('request');
let url = 'http://swapi.co/api/films/' + num;

request.get(url, function getUrl (error, response, body) {
  if (error) console.log(error);
  else console.log(JSON.parse(body).title);
});
