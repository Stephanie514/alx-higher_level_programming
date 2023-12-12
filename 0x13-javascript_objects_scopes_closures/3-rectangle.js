#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }

  print() {
    if (this.width && this.height) {
      for (let c = 0; c < this.height; c++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}

module.exports = Rectangle;
