#!/usr/bin/node

// Get arguments starting from index 2 (ignoring 'node' and script path)
const args = process.argv.slice(2);

// Convert all arguments to integers and remove any NaN values
const numbers = args
  .map(arg => parseInt(arg))
  .filter(num => !isNaN(num));

// If fewer than two numbers, print 0
if (numbers.length < 2) {
  console.log('0');
} else {
  // Sort numbers in descending order (biggest to smallest)
  numbers.sort((a, b) => b - a);

  // Print the second biggest number (at index 1)
  console.log(numbers[1]);
}
