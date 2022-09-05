#!/usr/bin/node
const process = require('process');
const i = parseInt(process.argv[2]);
if (Number.isNaN(i)) {
  console.log('Missing size');
} for (let len = 0; len < i; len++) {
  console.log('X'.repeat(i));
}
