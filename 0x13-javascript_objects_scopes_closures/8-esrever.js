#!/usr/bin/node
/* returns the reverse of list */

exports.esrever = function (list) {
  let end = list.length - 1;
  for (let start = 0; start < end; ++start, --end) {
    let temp = list[start];
    list[start] = list[end];
    list[end] = temp;
  }
  return list;
};
