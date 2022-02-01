#!/usr/bin/node
const fs = require('request');
const id = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

fs(id, function (a, response, body) {
  console.log(body.split(':')[1].split(',')[0]);
});
