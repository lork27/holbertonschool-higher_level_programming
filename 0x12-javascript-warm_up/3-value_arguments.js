#!/usr/bin/node
const process = require('process');

const argvPassed = (process.argv[2]);

if (argvPassed == null) {
  console.log('No argument');
} else {
  console.log(argvPassed);
}
