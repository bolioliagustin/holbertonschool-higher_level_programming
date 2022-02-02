#!/usr/bin/node
const req = require('request');
const fs = require('fs');

req(process.argv[2], function (error, response, body) {
  if (error) console.log(error);

  else {
    fs.writeFile(process.argv[3], body, 'utf-8', function (error) {
      if (error) console.log(error);
    });
  }
});
