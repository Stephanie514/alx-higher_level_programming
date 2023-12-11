#!/usr/bin/node
const addMeMaybe = function (number, theFunction) {
  return theFunction(++number);
};

module.exports = addMeMaybe;
