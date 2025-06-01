#!/usr/bin/node

const request = require('request');

// Get the movie ID from the first CLI argument
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// URL of the movie resource
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// First, fetch the movie data
request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Fetch each character URL in order and print the name
  const fetchCharacters = (index) => {
    if (index >= characters.length) return;

    request(characters[index], (err, res, body) => {
      if (!err) {
        const character = JSON.parse(body);
        console.log(character.name);
        fetchCharacters(index + 1); // Recursive call for the next character
      }
    });
  };

  fetchCharacters(0);
});
