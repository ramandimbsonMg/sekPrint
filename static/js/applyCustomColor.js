function applyCustomColor(hexColor) {
  // Appliquer la couleur personnalisée en style inline (backgroundColor ou color)
  const bgElements = ["bgTop", "bgBottom", "lineColor"];
  const textElements = ["textMatricule", "textNiveau", "textClasse"];

  bgElements.forEach((id) => {
    const el = document.getElementById(id);
    if (el) {
      el.style.backgroundColor = hexColor;
      // Supprimer les classes bg- précédentes qui peuvent interférer
      el.className = el.className.replace(/bg-[a-z]+-\d+/g, "").trim();
    }
  });

  textElements.forEach((id) => {
    const el = document.getElementById(id);
    if (el) {
      el.style.color = hexColor;
      // Supprimer les classes text- précédentes qui peuvent interférer
      el.className = el.className.replace(/text-[a-z]+-\d+/g, "").trim();
    }
  });
}
