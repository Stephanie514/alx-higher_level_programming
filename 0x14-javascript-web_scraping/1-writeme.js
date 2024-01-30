#!/usr/bin/node

const fs = require('fs');

const [,, filePath, contentToWrite] = process.argv;

fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) console.error(err);
});
