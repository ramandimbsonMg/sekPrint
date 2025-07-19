document.addEventListener("DOMContentLoaded", function () {
  const chartEl = document.querySelector("#studentsChart");

  if (chartEl) {
    const options = {
      chart: {
        type: "bar",
        height: 320,
        toolbar: { show: false },
      },
      series: [
        {
          name: "Total",
          data: [
            parseInt(chartEl.dataset.etudiants) || 0,
            parseInt(chartEl.dataset.ecoles) || 0,
            parseInt(chartEl.dataset.classes) || 0,
          ],
        },
      ],
      xaxis: {
        categories: ["Étudiants", "Écoles", "Classes"],
        labels: {
          style: { fontSize: "14px", colors: "#475569" },
        },
      },
      plotOptions: {
        bar: {
          columnWidth: "20%",
          distributed: true,
        },
      },
      fill: {
        colors: ["#2563eb", "#16a34a", "#7c3aed"],
      },
      dataLabels: {
        enabled: true,
        style: {
          colors: ["#111"],
        },
      },
      tooltip: {
        theme: "light",
      },
    };

    const chart = new ApexCharts(chartEl, options);
    chart.render();
  }
});
