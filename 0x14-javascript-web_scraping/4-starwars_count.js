#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');
const keyWord = argv[2].slice(0, -5) + 'people/18/';
let time = 0;
let a;

request(`${argv[2]}`, function (err, res, body) {
  if (!err && res.statusCode === 200) {
    const bodyDict = JSON.parse(body);
    for (a = 0; a < bodyDict.count; a++) {
      if (bodyDict.results[a].characters.includes(keyWord)) {
        time++;
      }
    }
    console.log(time);
  }
});
