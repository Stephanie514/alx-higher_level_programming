#!/usr/bin/node

$(document).ready(function () {
  function fetchTranslation() {
    var languageCode = $('#language_code').val();

    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}/`, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(fetchTranslation);

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      fetchTranslation();
    }
  });
});
