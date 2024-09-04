#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');

request(`${argv[2]}`, function (err, res, body) {
  if (!err && res.statusCode === 200) {
    const bodyDict = JSON.parse(body);
    const newDict = {};
    for (const key in bodyDict) {
      if (bodyDict[key].completed) {
        if (!Object.prototype.hasOwnProperty.call(newDict, bodyDict[key].userId)) {
          newDict[bodyDict[key].userId] = 1;
        } else {
          newDict[bodyDict[key].userId]++;
        }
      }
    }
    console.log(newDict);
  }
});
