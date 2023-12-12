#!/usr/bin/node

const supSquare = require('./5-square');

class Square extends supSquare {
  charPrint(c = 'X') {
    const char = c || 'X';
    for (let a = 0; a < this.height; a++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
