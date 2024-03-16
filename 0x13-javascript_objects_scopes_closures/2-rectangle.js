#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || typeof(w) === 'undefined' || h <= 0 || typeof(h) === 'undefined') {
      return null;
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
