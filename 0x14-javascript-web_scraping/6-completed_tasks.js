#!/usr/bin/node
/* read and prints contents of a file */

let request = require('request');
let url = process.argv[2];

request.get(url, function getText (error, response, body) {
  if (error) console.log(error);
  else {
    let tasks = JSON.parse(body);
    let myDict = {};
    let key;
    for (let i in tasks) {
      key = tasks[i].userId.toString();
      if (tasks[i].completed === true) myDict[key] = (myDict[key] || 0) + 1;
      else myDict[key] = (myDict[key] || 0);
    }
    console.log(myDict);
  }
});
