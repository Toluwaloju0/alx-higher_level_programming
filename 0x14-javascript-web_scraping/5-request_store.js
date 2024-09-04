#!/usr/bin/node
const request = require('request');
const { argv } = require('node:process');
const fs = require('fs');

request(`${argv[2]}`, function (err, res, body) {
  if (!err && res.statusCode === 200) {
    fs.writeFile(`${argv[3]}`, body, (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
