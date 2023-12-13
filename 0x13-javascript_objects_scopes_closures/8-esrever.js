#!/usr/bin/node
exports.esrever = function (list) {
  let l = list.length - 1;
  let a = 0;
  while ((l - a) > 0) {
    const Add = list[l];
    list[l] = list[a];
    list[a] = Add;
    a++;
    l--;
  }
  return list;
};
