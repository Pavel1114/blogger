$('.js-image-upload-with-preview').change(function () {
  const input = this;
  if (input.files && input.files[0]) {
    const reader = new FileReader();

    reader.onload = function (e) {
      const img = $('<img class="img-fluid w-100" alt="image preview" src="' + e.target.result + '">');
      $(input).parent().siblings('.js-image-preview').html(img);
      $(input).siblings('label').hide();
    }

    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
})
