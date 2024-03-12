#!/usr/bin/node
const { argv } = require('node:process');
let a = parseInt(argv[2]);
let b = 1;
if (isNaN(a)) {
  console.log(b);
} else {
  while (a > 0) {
    b = b * (a);
    a--;
  }
  console.log(b);
}
