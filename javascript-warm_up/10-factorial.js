#!/usr/bin/node

const number = parseInt(process.argv[2]);

function factorial (n) {
  if (isNaN(n)) return 1;
  if (n === 0 || n === 1) return 1;
  return n * factorial(n - 1);
}

console.log(factorial(number));
