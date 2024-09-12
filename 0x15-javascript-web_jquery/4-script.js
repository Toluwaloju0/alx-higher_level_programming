/* global $ */
$('div#toggle_header').on('click', function () {
  const header = $('header');
  header.toggleClass('green');
  header.toggleClass('red');
});
