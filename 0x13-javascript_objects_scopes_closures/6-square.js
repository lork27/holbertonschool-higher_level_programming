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
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
}

module.exports = Square;
