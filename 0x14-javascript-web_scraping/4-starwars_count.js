#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const wedgeAntillesId = '18';
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    const numMoviesWithWedgeAntilles = movies.reduce((count, movie) => {
      if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
        return count + 1;
      } else {
        return count;
      }
    }, 0);
    console.log(`${numMoviesWithWedgeAntilles}`);
  } else {
    console.error(`Error: ${error}`);
  }
});

