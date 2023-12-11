#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
const second = args.length > 1 ? Math.max(...args.filter(num => num !== Math.max(...args))) : 0;
console.log(second);
