// ── MAP SVG CONNECTION LINE ────────────────────────────────────────────────
(function () {
  const board = document.getElementById("mapBoard");
  const svg   = document.getElementById("boardSvg");
  if (!board || !svg) return;

  // chapter IDs in the order we want to draw the path
  const ORDER = [
    "liczby", "algebra", "funkcje",
    "ciagi", "trygonometria", "geometria", "kombinatoryka"
  ];

  function drawLine() {
    const br = board.getBoundingClientRect();
    const pts = ORDER.map(id => {
      const el = document.getElementById("circle-" + id);
      if (!el) return null;
      const r = el.getBoundingClientRect();
      return `${r.left - br.left + r.width / 2},${r.top - br.top + r.height / 2}`;
    }).filter(Boolean).join(" ");

    svg.setAttribute("viewBox", `0 0 ${board.offsetWidth} ${board.offsetHeight}`);
    svg.innerHTML = `
      <polyline
        points="${pts}"
        fill="none"
        stroke="#a78bfa"
        stroke-width="3"
        stroke-dasharray="10 7"
        stroke-linecap="round"
        stroke-linejoin="round"
        opacity="0.55"
      />`;
  }

  drawLine();
  window.addEventListener("resize", drawLine);
})();
