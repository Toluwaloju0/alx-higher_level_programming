/* global $ */
const tag = $('div#hello');
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(document).ready(function () {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      tag.text(data['hello']);
    });
});
