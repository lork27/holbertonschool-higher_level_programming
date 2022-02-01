#!/usr/bin/node
const r = require('request');
const fs = require('fs');
const url = process.argv[2];
r(url, function (a, response, body) {
  fs.writeFile(process.argv[3], body, err => {
    if (err) {
      console.log(err);
    }
  }
  );
});
