exports.logMe = (function() {
  let Count = 0;
  return function(item) {
    console.log(Count + ': ' + item);
    Count++;
  };
})();
