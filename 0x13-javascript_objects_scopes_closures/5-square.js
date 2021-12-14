#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Squere extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
