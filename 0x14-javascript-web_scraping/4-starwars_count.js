#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');
let time = 0;
let a;

request(`${argv[2]}`, function (err, res, body) {
  if (!err && res.statusCode === 200) {
    const bodyDict = JSON.parse(body);
    const keyWord = bodyDict.results[0].characters[1].slice(0, -2) + '18/';
    for (a = 0; a < bodyDict.count; a++) {
      if (bodyDict.results[a].characters.includes(keyWord)) {
        time++;
      }
    }
    console.log(time);
  }
});
