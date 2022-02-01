#!/usr/bin/node
const fs = require('request');
const id = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

fs(id, function (a, response, body) {
  let feo = body.split(':')[1].split(',')[0];
  feo = feo.replace('"', '');
  feo = feo.replace('"', '');
  console.log(feo);
});
