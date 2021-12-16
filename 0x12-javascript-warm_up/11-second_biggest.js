#!/usr/bin/node
const array = process.argv;
let maximo = -Infinity; let res = -Infinity;
if (!array[2] || array.length < 4) {
  console.log(0);
} else {
  for (let i = 2; array[i]; i++) {
    const tmp = parseInt(array[i]);
    if (maximo < tmp) {
      [res, maximo] = [maximo, tmp];
    } else if (res < tmp && tmp < maximo) {
      res = tmp;
    }
  }
  console.log(res);
}
