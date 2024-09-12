/* global $ */
const pList = $('ul#list_movies');
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

fetch(url)
  .then(response => response.json())
  .then(data => {
    const count = data.count;
    const mList = [];
    for (let a = 0; a < count; a++) {
      mList.push(data.results[a].title);
    }
    for (let a = 0; a < mList.length; a++) {
      pList.append(`<l1>${mList[a]}</li><br>`);
    }
  });
