#!/usr/bin/node

const requestModule = require('request');
const fs = require('fs');

const commandLineArgs = process.argv;
const requestUrl = commandLineArgs[2];
const destinationPath = commandLineArgs[3];

requestModule(
  {
    method: 'GET',
    uri: requestUrl
  },
  function (error, response, body) {
    if (error) throw error;
    if (response.statusCode === 200) {
      fs.writeFile(destinationPath, body, 'utf8', function (error) {
        if (error) throw error;
      });
    }
  }
);
