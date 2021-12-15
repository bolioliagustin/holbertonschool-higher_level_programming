#!/usr/bin/node
exports.converter = function (base) {
  function getNum (i) {
    return i.toString(base);
  }
  return getNum;
};
