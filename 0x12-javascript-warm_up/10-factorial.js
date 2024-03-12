#!/usr/bin/node
function factorial (a) {
  if (a === 1) {
    return (1);
  }
  b = a * (factorial(a - 1));
  return (b);
}
const { argv } = require('node:process');
const a = parseInt(argv[2]);
let b = 1;
if (isNaN(a)) {
  console.log(b);
} else {
  console.log(factorial(a));
}
