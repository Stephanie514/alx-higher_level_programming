#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request.get(`${apiUrl}/people/${characterId}`, (error, response, characterBody) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    return;
  }

  const character = JSON.parse(characterBody);
  const films = character.films.length;

  console.log(films);
});
