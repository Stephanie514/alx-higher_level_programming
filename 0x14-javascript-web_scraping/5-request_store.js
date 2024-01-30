#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const args = process.argv;
const url = args[2];
const filePath = args[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf8', (error) => {
      if (error) {
        console.error(error);
      } else {
        console.log(`Content saved to ${filePath}`);
      }
    });
  } else {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
  }
});
