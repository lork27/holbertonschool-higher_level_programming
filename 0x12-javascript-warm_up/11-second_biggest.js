#!/usr/bin/node
let { argv } = require('process');
const process = require('process');
const argA = parseInt((process.argv[2]));
let argList = [];

if (argv.length === 2 || argA === 1) {
  console.log(1);
} else {
  argv.forEach(element => {
    if(!isNaN(parseInt(element)))
    {
      argList.push(element);
    }
  });
  argList = argList.sort((a, b) => a - b);
  console.log(argList[argList.length - 2]); 
}
