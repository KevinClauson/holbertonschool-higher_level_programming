#!/usr/bin/node
/* read and prints contents of a file */

let fs = require('fs');
let file = process.argv[2];

fs.readFile(file, 'utf8', function read (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
