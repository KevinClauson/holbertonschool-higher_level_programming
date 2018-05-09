#!/usr/bin/node
/* read and prints contents of a file */

let url;
if (process.argv[2]) url = process.argv[2];
else url = '';
let request = require('request');

request.get(url, function getUrl (error, response) {
  if (error) console.log(error);
  else console.log('code:', response.statusCode);
});
