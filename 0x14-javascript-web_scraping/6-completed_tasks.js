#!/usr/bin/node
/* read and prints contents of a file */

let request = require('request');
let url = process.argv[2];

request.get(url, function getText (error, response, body) {
  if (error) console.log(error);
  else {
    let tasks = JSON.parse(body);
    let myDict = {};
    for (let i in tasks) {
      let key = (tasks[i].userId);
      myDict[key] = (myDict[key] || 0) + 1;
    }
    console.log(myDict);
  }
});
