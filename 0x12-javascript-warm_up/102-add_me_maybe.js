#!/usr/bin/node

function addMeMaybe (num, thefunc) {
  thefunc(num + 1);
}

exports.addMeMaybe = addMeMaybe;
