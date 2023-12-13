#!/usr/bin/node

const myList = require('./100-data').list;

const multipliedList = myList.map((value, index) => value * index);

console.log("Initial List:", myList);
console.log("Multiplied List:", multipliedList);
