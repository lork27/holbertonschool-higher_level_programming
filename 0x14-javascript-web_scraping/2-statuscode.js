#!/usr/bin/node
const fs = require('request');
if (process.argv.length == 3) {
  const url = process.argv[2];

  fs(url, function (a, response, b) {
    console.log('Code:', response.statusCode); // Print the response status code if a response was received
  });
}
else {
  console.log("ayy")
}