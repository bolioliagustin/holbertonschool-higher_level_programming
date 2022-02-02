#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let number = 0;
    for (const film of JSON.parse(body).results) {
      for (const i of film.characters) {
        if (i.includes('/18/')) {
          number++;
        }
      }
    }
    console.log(number);
  }
});
