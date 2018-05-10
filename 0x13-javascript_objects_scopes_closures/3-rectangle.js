#!/usr/bin/node
/* makes a rectangle class */

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let myStr = Array(this.width + 1).join('X');
    for (let i = 0; i < this.height; i++) {
      console.log(myStr);
    }
  }
}

module.exports = Rectangle;
