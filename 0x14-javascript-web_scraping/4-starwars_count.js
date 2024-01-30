#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode} - ${response.statusMessage}`);
    return;
  }

  const films = JSON.parse(body).results;
  const count = films.filter(film => {
    const characterUrl = `https://swapi-api.alx-tools.com/api/people/${characterId}/`;
    return film.characters.includes(characterUrl);
  }).length;

  console.log(count);
});
