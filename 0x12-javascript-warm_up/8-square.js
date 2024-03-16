#!/usr/bin/node
const { argv } = require('node:process');
const a = parseInt(argv[2]);
const c = 'X'.repeat(a);
if (isNaN(a)) {
  console.log('missing size');
} else {
  for (let b = 0; b < a; b++) {
    console.log(c);
  }
}
