#!/usr/bin/node
const process = require('process');
const argInt = parseInt((process.argv[2]));
let i = 0;
let j = 0;

if (isNaN(argInt)) {
  console.log('Missing size');
} else {
  while (i < argInt) {
    while (j < argInt) {
      process.stdout.write('X');
      j++;
    }
    j = 0;
    console.log('');
    i++;
  }
}
