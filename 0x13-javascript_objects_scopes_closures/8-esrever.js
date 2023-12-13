exports.esrever = function (list) {
  let reversedList = [];
  for (let a = list.length - 1; a >= 0; a--) {
    reversedList.push(list[a]);
  }
  return reversedList;
};
