#!/usr/bin/node

function multiplyByIndex(value, index) {
  return value * index;
}

const list = require('./100-data').list;

console.log(list);
console.log(list.map(multiplyByIndex));
