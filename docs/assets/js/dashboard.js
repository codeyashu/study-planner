// Dashboard widgets: KPIs, heatmap and per-track progress, fed by assets/stats.json (built by scripts/stats.py).
(function () {
  function siteBase() {
    try {
      var cfg = JSON.parse(document.getElementById("__config").textContent);
      return new URL(cfg.base + "/", location.href).href;
    } catch (e) {
      return new URL("./", location.href).href;
    }
  }

  function isoDate(d) {
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }

  function renderKpis(stats) {
    var set = function (key, value) {
      var el = document.querySelector('[data-kpi="' + key + '"]');
      if (el) el.textContent = value;
    };
    set("streak", stats.streak);
    set("done", stats.total.done + "/" + stats.total.planned);
    set("behind", stats.total.behind);
    set("week", stats.current_week);
  }

  function renderHeatmap(stats, el) {
    if (!stats.start || !stats.end) return;
    var start = new Date(stats.start + "T00:00:00");
    // align to Monday so rows are weekdays
    start.setDate(start.getDate() - ((start.getDay() + 6) % 7));
    var end = new Date(stats.end + "T00:00:00");
    var today = isoDate(new Date());
    var frag = document.createDocumentFragment();
    for (var d = new Date(start); d <= end; d.setDate(d.getDate() + 1)) {
      var key = isoDate(d);
      var n = stats.heatmap[key] || 0;
      var cell = document.createElement("span");
      cell.className = "sp-heatmap__cell";
      cell.dataset.level = n === 0 ? "0" : n < 2 ? "1" : n < 4 ? "2" : "3";
      if (key === today) cell.dataset.today = "true";
      cell.title = key + ": " + n + " task" + (n === 1 ? "" : "s");
      frag.appendChild(cell);
    }
    el.replaceChildren(frag);
  }

  function renderTracks(stats, el) {
    var frag = document.createDocumentFragment();
    Object.keys(stats.by_track).forEach(function (key) {
      var t = stats.by_track[key];
      if (!t.planned) return;
      var pct = Math.round((100 * t.done) / t.planned);
      var row = document.createElement("div");
      row.className = "sp-track__row";
      row.innerHTML =
        '<span>' + t.label + '</span><span class="sp-track__bar"><span class="sp-track__fill" style="width:' + pct +
        '%"></span></span><span class="sp-track__num">' + t.done + "/" + t.planned + "</span>";
      frag.appendChild(row);
    });
    el.replaceChildren(frag);
  }

  function init() {
    var heat = document.querySelector("[data-heatmap]");
    var tracks = document.querySelector("[data-tracks]");
    var kpis = document.querySelector("[data-stats]");
    if (!heat && !tracks && !kpis) return;
    fetch(siteBase() + "assets/stats.json", { cache: "no-store" })
      .then(function (r) { return r.json(); })
      .then(function (stats) {
        if (kpis) renderKpis(stats);
        if (heat) renderHeatmap(stats, heat);
        if (tracks) renderTracks(stats, tracks);
      })
      .catch(function () { /* stats not built yet — widgets stay as placeholders */ });
  }

  // Material's instant navigation exposes document$; fall back to DOMContentLoaded.
  if (window.document$ && window.document$.subscribe) {
    window.document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
