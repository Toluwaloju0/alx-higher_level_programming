#!/usr/bin/node
const { argv } = require('node:process');
const a = parseInt(argv[2], 10);
const b = parseInt(argv[3], 10);

if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(`${a + b}`);
}
