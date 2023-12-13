#!/usr/bin/node

const dict = require('./101-data').dict;

const result = Object.keys(dict).reduce((acc, key) => {
  const value = dict[key];
  if (!acc[value]) {
    acc[value] = [];
  }
  acc[value].push(key);
  return acc;
}, {});

console.log(result);
