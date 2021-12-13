#!/usr/bin/node
const { argv } = require('process');
const process = require('process');
const argA = parseInt((process.argv[2]));
// let argList = [];

if (argv.length === 2 || argA === 1) {
  console.log(1);
} else {
  // let i = 2;
  // let x = 0;
  // while (i < argv.length) {
  //   argList[x] = parseInt(argv[i]);
  //   i++;
  //   x++;
  // }
  // console.log(Math.max(argList));
  console.log(argv);
  }