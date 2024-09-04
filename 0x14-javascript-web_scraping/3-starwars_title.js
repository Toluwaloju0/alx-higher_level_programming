#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request(url, function (err, res, body) {
  if (!err && res.statusCode === 200) {
    const jsonBody = JSON.parse(body);
    console.log(jsonBody.title);
  }
});
