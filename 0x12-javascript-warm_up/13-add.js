#!/usr/bin/node
exports.add = function (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (0);
  } else {
    return a + b;
  }
}
