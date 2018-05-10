#!/usr/bin/node
/* makes a rectangle class */

const Sqr = require('./5-square');

class Square extends Sqr {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let myStr = Array(this.width + 1).join(c);
    for (let i = 0; i < this.height; i++) {
      console.log(myStr);
    }
  }
}

module.exports = Square;
