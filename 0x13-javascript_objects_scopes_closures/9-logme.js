#!/usr/bin/node

exports.logMe = function (item) {
  if (typeof this.ttl === 'undefined') {
    this.ttl = 0;
  }
  console.log(this.ttl + ': ' + item);
  this.ttl++;
};
