#!/usr/bin/node
let { argv } = require('process');
const process = require('process');
const argA = parseInt((process.argv[2]));
// let argList = [];

if (argv.length === 2 || argA === 1) {
  console.log(0);
} else {
  argv = argv.sort((a, b) => a - b);
  console.log(argv[argv.length - 2]);
}
