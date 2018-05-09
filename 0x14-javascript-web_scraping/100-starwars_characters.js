#!/usr/bin/node
/* read and prints contents of a file */

let request = require('request');
let url = 'http://swapi.co/api/films/';
let num = process.argv[2];
url = url + num + '/';
let bodyParse;
request.get(url, function getUrl (error, response, body) {
  if (error) console.log(error);
  else if (response && body) {
    bodyParse = JSON.parse(body);
    for (let i in bodyParse['characters']) {
      request.get(bodyParse['characters'][i], function (err, res, bo) {
        if (err) console.log(err);
        else {
          console.log(JSON.parse(bo)['name']);
        }
      });
    }
  }
});
