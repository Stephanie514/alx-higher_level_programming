#!/usr/bin/node

$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    const items = data.results.map(function (value) {
      return '<li>' + value.title + '</li>';
    });
    $('ul#list_movies').append(items.join(''));
  });
});
