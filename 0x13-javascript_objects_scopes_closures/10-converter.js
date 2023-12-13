#!/usr/bin/node

exports.converter = function (base) {
  return function (dig) {
    return dig.toString(base);
  };
};
