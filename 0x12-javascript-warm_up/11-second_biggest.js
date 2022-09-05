#!/usr/bin/node
const process = require('process');
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const newArray = process.argv.slice(2);
  console.log(newArray.sort(function (a, b) { return b - a; })[1]);
}
