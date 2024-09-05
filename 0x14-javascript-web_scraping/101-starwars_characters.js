#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

request(url, function (err, res, body) {
  if (!err && res.statusCode === 200) {
    const bodyDict = JSON.parse(body);
    for (let a = 0; a < bodyDict.characters.length; a++) {
      request(bodyDict.characters[a], function (err, res, body) {
        if (!err && res.statusCode === 200) {
          const newUrlBody = JSON.parse(body);
          console.log(newUrlBody.name);
        }
      });
    }
  }
});
