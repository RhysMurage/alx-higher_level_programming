#!/usr/bin/node

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
