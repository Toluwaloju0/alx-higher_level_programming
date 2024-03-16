#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');
fs.readfile(argv[2], 'utf8', (err, data1));
fs.readfile(argv[3], 'utf8', (err, data2));
const fullData = data1 + '\n' + data2;
fs.writefile(argv[4], fullData, 'utf8', (err));
