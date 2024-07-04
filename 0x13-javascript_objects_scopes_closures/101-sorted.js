#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};
let a;

for (const key in dict) {
  a = dict[key];
  if (a in Object.keys(newDict)) {
    newDict[a].push(key);
  } else {
    newDict[a] = [key];
  }
}
console.log(newDict);
