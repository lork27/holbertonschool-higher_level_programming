#!/usr/bin/node

const list = require('./100-data').list;

console.log(list);

const newList = list.map((num, i) => num * i);

console.log(newList);
