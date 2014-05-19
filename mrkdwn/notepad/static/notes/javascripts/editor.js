$(document).ready(function() {
  var editor = ace.edit("editor");
  editor.getSession().setMode("ace/mode/markdown");
  editor.getSession().setValue($('#md-content').data('md'));
  editor.renderer.setShowGutter(false)
  editor.getSession().setTabSize(2)
  editor.getSession().setUseSoftTabs(true)
  editor.getSession().setUseWrapMode(true)
  editor.setHighlightActiveLine(true)
  editor.setShowPrintMargin(false)

  $('input[type="submit"]').on('click', function() {
    $('#md-content').val(editor.getValue());
  });
});
