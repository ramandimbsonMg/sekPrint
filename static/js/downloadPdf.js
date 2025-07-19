function downloadPDF() {
  const badge = document.getElementById("badge");
  var opt = {
    margin: 0.3,
    filename: "badge-etudiant.pdf",
    image: { type: "jpeg", quality: 0.98 },
    html2canvas: { scale: 2 },
    jsPDF: { unit: "in", format: "a6", orientation: "portrait" },
  };
  html2pdf().set(opt).from(badge).save();
}
