#!/usr/bin/node
const { argv } = require('node:process');
let a = parseInt(argv[2]);
let b = 0;
let c = 0;
if (isNaN(a)) {
  console.log('missing size');
} else {
  for (let b = 0; b < a; b++) {
    for(let c = 0; c < a; c++) {
      console.log('X');
    }
  }
}
