#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  for (let b = list.length - 1; b >= 0; b--) {
    newList.push(list[b]);
  }
  return newList;
};
