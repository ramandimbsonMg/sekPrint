function previewImage(event) {
  const file = event.target.files[0];
  const reader = new FileReader();
  const preview = document.getElementById("imagePreview");
  const avatar = document.getElementById("avatarPreview");

  reader.onload = function () {
    preview.src = reader.result;
    preview.classList.remove("hidden");
  };
  if (file) {
    reader.readAsDataURL(file);
  }
}
