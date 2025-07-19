function changeColor(color) {
  const elements = [
    { id: "bgTop", base: "bg" },
    { id: "bgBottom", base: "bg" },
    { id: "lineColor", base: "bg" },
    { id: "textMatricule", base: "text" },
    { id: "textNiveau", base: "text" },
    { id: "textClasse", base: "text" },
  ];
  elements.forEach(({ id, base }) => {
    const el = document.getElementById(id);
    if (!el) return;

    // Supprimer les styles inline de couleur qui pourraient bloquer la classe
    el.style.backgroundColor = "";
    el.style.color = "";

    // Supprimer les classes tailwind de couleurs précédentes (cyan,yellow,rose,green)
    el.className = el.className
      .replace(/(bg|text)-(cyan|yellow|rose|green)-400/g, "")
      .trim();

    // Ajouter la nouvelle classe (ex: bg-cyan-400)
    el.classList.add(`${base}-${color}-400`);
  });

  // Reset la valeur du colorPicker (pour ne pas confondre)
  const colorPicker = document.getElementById("colorPicker");
  if (colorPicker) {
    colorPicker.value = "";
  }
}
