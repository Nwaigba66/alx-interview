#!/usr/bin/node
const request = require('request');
const filmId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

const params = {
  url,
  method: 'GET',
  headers: { 'Content-Type': 'application/json' }
};
request(params, (error, response) => {
  if (!error) {
    const { characters } = JSON.parse(response.body);
    const info = {};
    let size = characters.length;
    characters.forEach((character, index) => {
      request({
        url: character,
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
      }, (err, resp) => {
        if (!err) {
          info[`${index}`] = JSON.parse(resp.body).name;
          size--;
          if (size === 0) {
            for (const name of Object.values(info)) console.log(name);
          }
        }
      });
    });
  }
});
