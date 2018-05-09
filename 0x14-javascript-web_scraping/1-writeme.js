#!/usr/bin/node
/* read and prints contents of a file */

let file;
let text;
let fs = require('fs');
if (process.argv[2]) file = process.argv[2];
else file = '';
if (process.argv[3]) text = process.argv[3];
else text = '';

fs.writeFile(file, text, 'utf8', function write (err) {
  if (err) {
    console.log(err);
  }
});
