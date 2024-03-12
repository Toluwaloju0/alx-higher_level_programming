#!/usr/bin/node
const { argv } = require('node:process');
let a = parseInt(argv[2]);
if (isNaN(a)) {
  console.log('Missing number of occurrences');
} else {
  while (a > 0) {
    console.log('C is fun');
    a = a - 1;
  }
}
