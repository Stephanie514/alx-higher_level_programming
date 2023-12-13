#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((b, r) => (r === searchElement ? b + 1 : b), 0);
};
