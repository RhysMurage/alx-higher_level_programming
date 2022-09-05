#!/usr/bin/node
const process = require('process');
/*
const i = parseInt(process.argv[2]);
function factorial (a) {
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(factorial(i));
*/

let digit = Number(process.argv[2]);

if (isNaN(digit)) {
  digit = 1;
}
console.log(doFactorial(digit));

function doFactorial (a) {
  if (a === 0 || isNaN(a)) {
    return (1);
  }
  const result = a * doFactorial(a - 1);
  return (result);
}
