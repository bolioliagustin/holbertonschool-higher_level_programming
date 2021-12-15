#!/usr/bin/node
const { argv } = require('process');
if (!argv[2] || !parseInt(argv[2])) {
  console.log('Missing size');
} else if (argv[2] >= 0) {
  for (let i = 0; i < argv[2]; i++) {
    console.log('X'.repeat(argv[2]));
  }
}
