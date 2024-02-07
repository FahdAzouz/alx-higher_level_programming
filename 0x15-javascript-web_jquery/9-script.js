$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
    $('div#hello').append(`<p>${data.hello}</p>`);
  }); 
});

