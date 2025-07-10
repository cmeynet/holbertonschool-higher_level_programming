#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);
const sentence = 'C is fun';

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log(sentence);
  }
}
