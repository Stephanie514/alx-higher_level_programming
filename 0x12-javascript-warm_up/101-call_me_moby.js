#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let c = 0; c < x; c++) {
    theFunction();
  }
};
