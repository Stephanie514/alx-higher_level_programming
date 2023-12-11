#!/usr/bin/node
function calculateFactorial(n) {
  return (n <= 1 || isNaN(n)) ? 1 : n * calculateFactorial(n - 1);
}

const input = Number(process.argv[2]);
console.log(calculateFactorial(input));
