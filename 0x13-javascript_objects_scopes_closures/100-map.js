#!/usr/bin/node
/* convert number to different base */

exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
