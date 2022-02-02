#!/usr/bin/node
const r = require('request');
const url = process.argv[2];
r(url, function (a, response, body) {
  const tasks = JSON.parse(body);
  const usrcompleted = {};
  tasks.forEach(function (task) {
    if (!usrcompleted[task.userId]) {
      usrcompleted[task.userId] = 0;
    }
    if (task.completed) {
      usrcompleted[task.userId]++;
    }
  });

  console.log(usrcompleted);
});
