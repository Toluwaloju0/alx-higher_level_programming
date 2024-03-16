#!/usr/bin/node
const oldSquare = require('./5-square');
module.exports = class Square extends oldSquare {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      return this.print();
    } else {
      for (let a = 0; a < this.width; a++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
