#!/usr/bin/node
const { argv } = require('process');
let argList = [];

if (argv.length <= 3) {
  console.log(0);
} else {
  argv.forEach(element => {
    if (!isNaN(parseInt(element))) {
      argList.push(element);
    }
  });
  argList = argList.sort((a, b) => a - b);
  console.log(argList[argList.length - 2]);
}
