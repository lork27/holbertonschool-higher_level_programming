#!/usr/bin/node
const fs = require('request');
const url = process.argv[2];

fs.get(url).on('response', function(response) {
  console.log("code: ", response.statusCode)
})
