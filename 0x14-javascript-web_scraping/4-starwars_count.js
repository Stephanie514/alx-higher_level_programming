#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    return;
  }

  const films = JSON.parse(body).results;
  const characterId = '18';
  const count = films.filter(film => film.characters.some(character => character.toLowerCase() === `https://swapi-api.alx-tools.com/api/people/${characterId}/`.toLowerCase())).length;

  console.log(count);
});

