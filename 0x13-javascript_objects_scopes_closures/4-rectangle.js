#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || typeof (w) === 'undefined' || h <= 0 || typeof (h) === 'undefined') {
      return null;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const a = 'X'.repeat(this.width);
    for (let b = 0; b < this.height; b++) {
      console.log(a);
    }
  }

  rotate () {
    const a = this.height;
    this.height = this.width;
    this.width = a;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
