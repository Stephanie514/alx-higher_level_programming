#!/usr/bin/node
const size = Number(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let c = 0; c < size; c++) {
    console.log('X'.repeat(size));
  }
}
