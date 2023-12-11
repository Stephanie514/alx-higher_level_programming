#!/usr/bin/node
function addMeMaybe(number, theFunction) {
  return theFunction.call(this, ++number);
}

module.exports = addMeMaybe;
