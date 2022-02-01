#!/usr/bin/node
const number = process.argv[2];
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + number, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
