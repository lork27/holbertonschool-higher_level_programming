#!/usr/bin/node
const fs = require('request');
const id = process.argv[2];
let count = 0;
fs(id, function (a, response, body) {
  const movies = JSON.parse(body);
  for (const movie in movies.results) {
    for (const i in movies.results[movie].characters) {
      if (movies.results[movie].characters[i].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
