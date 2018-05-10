#!/usr/bin/node
/* returns the reverse of list */

let cnt = 0;
exports.logMe = function (item) {
  console.log(cnt + ': ' + item);
  cnt++;
};
