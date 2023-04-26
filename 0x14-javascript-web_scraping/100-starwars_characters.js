#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(apiUrl, (err, response, body) => {
  if (err) console.error(err);
  const movie = JSON.parse(body);
  movie.characters.forEach((characterUrl) => {
    request(characterUrl, (err, response, body) => {
      if (err) console.error(err);
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
