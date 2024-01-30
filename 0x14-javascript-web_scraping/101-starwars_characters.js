#!/usr/bin/node

const httpRequest = require('request');

const givenMovieId = process.argv[2];
const movieApiUrl = `https://swapi.dev/api/films/${givenMovieId}/`;

httpRequest(movieApiUrl, function (movieError, movieResponse, movieBody) {
  if (!movieError && movieResponse.statusCode === 200) {
    const movieData = JSON.parse(movieBody);

    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        httpRequest(characterUrl, function (charError, charResponse, charBody) {
          if (!charError && charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            resolve(characterData.name);
          } else {
            reject(new Error(`Error fetching character data: ${charError}`));
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        console.log(characterNames.join('\n'));
      })
      .catch((error) => {
        console.error(error.message);
      });
  } else {
    console.error('Error fetching movie data:', movieError);
  }
});
