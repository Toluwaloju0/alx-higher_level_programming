#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');

request(`${argv[2]}`, function (err, response) {
  if (err) {
    throw err;
  }
  console.log('code: ', response.statusCode);
});
