$(document).ready(function() {
  markdownText = $('#md').data('md');

  var converter = new Showdown.converter();
  $('#md').html(converter.makeHtml(markdownText));
});
