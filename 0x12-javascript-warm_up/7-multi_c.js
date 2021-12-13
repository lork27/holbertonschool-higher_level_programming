#!/usr/bin/node
const process = require('process');
const argInt = parseInt((process.argv[2]));
let i = 0;

if (isNaN(argInt)) {
  console.log('Missing number of occurrences');
} else {
  while (i < argInt) {
    console.log('C is fun');
    i++;
  }
}
