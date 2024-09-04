#!/usr/bin/node
const fs = require('fs');
const { argv } = require('node:process');

fs.readFile(`${argv[2]}`, (err, file) => {
  if (err) {
    console.log(err);
  } else {
    console.log(file.toString());
  }
});
