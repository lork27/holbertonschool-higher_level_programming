#!/usr/bin/node
const process = require('process');
const argA = parseInt((process.argv[2]));

if (isNaN(argA) || argA === 1) {
  console.log(1);
} else {
  function factorial (number) {
    if (number === 0 || number === 1) {
      return (1);
    } else {
      return (number * factorial(number - 1));
    }
  }

  console.log(factorial(argA));
}
