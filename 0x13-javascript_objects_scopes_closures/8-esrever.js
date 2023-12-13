exports.esrever = function (list) {
  const l = list.length;
  for (let a = 0; a < Math.floor(l / 2); a++) {
    const vaar = list[a];
    list[a] = list[l - 1 - a];
    list[l - 1 - a] = vaar;
  }
  return list;
};
