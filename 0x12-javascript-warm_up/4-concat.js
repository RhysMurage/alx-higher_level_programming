#!/usr/bin/node

let len = 0;
for (const i of process.argv) {
  len++;
  i.toLowerCase();
}
if (len === 2) {
  console.log('No argument');
} else {
  const sentence = `${process.argv[2]} is ${process.argv[3]}`;
  console.log(sentence);
}
