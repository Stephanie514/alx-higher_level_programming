#!/usr/bin/node

const fs = require('fs');

const args = process.argv;
const filePath = args[2];
const contentToWrite = args[3];

fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`Content written to ${filePath}`);
});
