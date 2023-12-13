#!/usr/bin/node

const fs = require('fs');
const process = require('process');

const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

const readStream1 = fs.createReadStream(file1, { encoding: 'utf8' });
const readStream2 = fs.createReadStream(file2, { encoding: 'utf8' });
const writeStream = fs.createWriteStream(destination, { encoding: 'utf8' });

readStream1.pipe(writeStream, { end: false });
readStream2.pipe(writeStream, { end: false });

readStream1.on('end', () => {
  readStream2.pipe(writeStream);
});
