#!/usr/bin/node
const { argv } = require('node:process');
const numA = parseInt(argv[2]);

if (isNaN(numA)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${numA}`);
}
