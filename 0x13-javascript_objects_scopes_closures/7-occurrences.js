exports.nbOccurences = function (list, searchElement) {
  let Count = 0;
  for (const element of list) {
    if (element === searchElement) {
     Count++;
    }
  }
  return Count;
};
