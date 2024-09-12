/* global $ */
const chaR = $('div#character');
const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const name = data.name;
    chaR.text(name);
  });
