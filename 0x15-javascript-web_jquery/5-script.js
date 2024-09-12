/* global $ */
$('div#add_item').on('click', function () {
  const items = $('ul.my_list');
  items.append('<li>Item</li>');
});
