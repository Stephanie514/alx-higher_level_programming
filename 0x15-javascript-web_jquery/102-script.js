#!/usr/bin/node

$(document).ready(function () {
  $('#btn_translate').click(function () {
    var languageCode = $('#language_code').val();

    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
