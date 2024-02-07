$('document').ready( function() {
  $('INPUT#btn_translate').click( function() {
    const val = $('INPUT#language_code').val();
    $.ajax({
      type: 'GET',
      url: `https://www.fourtonfish.com/hellosalut/hello/${val}`,
      success: function (data) {
        $('DIV#hello').html(data.hello);
      },
    });
  });
});
