/* global $ */
const tag = $('div#red_header');
tag.on('click', function () {
  const header = $('header');
  header.css('color', '#FF0000');
});
