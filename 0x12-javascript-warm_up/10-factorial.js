#!/usr/bin/node
const process = require('process');

const i = parseInt(process.argv[2]);
function factorial (a) {
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(factorial(i));
