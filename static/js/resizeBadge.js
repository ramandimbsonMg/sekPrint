function resizeBadge(size) {
  const badge = document.getElementById("badge");
  badge.classList.remove("max-w-[280px]", "max-w-[340px]", "max-w-[400px]");
  badge.classList.add(
    size === "sm"
      ? "max-w-[280px]"
      : size === "lg"
      ? "max-w-[400px]"
      : "max-w-[340px]"
  );

  document.querySelectorAll("#radioGroup .radio-dot").forEach((dot) => {
    dot.classList.remove("scale-100");
    dot.classList.add("scale-0");
  });

  const checkedInput = document.querySelector('input[name="taille"]:checked');
  if (checkedInput) {
    const dot = checkedInput.parentElement.querySelector(".radio-dot");
    if (dot) dot.classList.add("scale-100");
  }
}
window.addEventListener("DOMContentLoaded", () => {
  resizeBadge(document.querySelector('input[name="taille"]:checked').value);

  // Écouter les changements du colorPicker
  const colorPicker = document.getElementById("colorPicker");
  if (colorPicker) {
    colorPicker.addEventListener("input", (e) => {
      const val = e.target.value;
      if (val) {
        applyCustomColor(val);
      }
    });
  }
});
