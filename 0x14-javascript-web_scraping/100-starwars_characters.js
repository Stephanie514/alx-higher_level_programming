#!/usr/bin/node

const requestModule = require('request');

const givenMovieId = process.argv[2];
const givenApiUrl = `https://swapi.dev/api/films/${givenMovieId}/`;

requestModule(givenApiUrl, function (reqError, reqResponse, reqBody) {
  if (!reqError && reqResponse.statusCode === 200) {
    const movieData = JSON.parse(reqBody);
    console.log(`Characters of "${movieData.title}":`);

    movieData.characters.forEach((characterUrl) => {
      requestModule(characterUrl, function (charError, charResponse, charBody) {
        if (!charError && charResponse.statusCode === 200) {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        } else {
          console.error('Error fetching character data:', charError);
        }
      });
    });
  } else {
    console.error('Error fetching movie data:', reqError);
  }
});
