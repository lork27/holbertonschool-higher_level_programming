#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    super.print(c);
  }
}

module.exports = Square;
