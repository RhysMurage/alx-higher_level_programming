#!/usr/bin/node
const process = require('process');

const args = process.argv;
/*
let len = 0;
for (const i of process.argv) {
  len++;
  i.toLowerCase();
}
if (len === 2) {
  console.log('No argument');
} else {
  for (let step = 2; step < len; step++) {
    console.log(process.argv[step]);
  }
}
*/

if (args[2]) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
