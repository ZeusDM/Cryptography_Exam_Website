/**
 * Main client-side interactivity for UW Cryptography Exam Site
 * Theme switcher, matrix filtering, solution toggles, copy actions
 */

// Theme Management
(function initTheme() {
  const savedTheme = localStorage.getItem("theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  if (savedTheme) {
    document.documentElement.setAttribute("data-theme", savedTheme);
  } else if (prefersDark) {
    document.documentElement.setAttribute("data-theme", "dark");
  }
})();

function toggleTheme() {
  const current = document.documentElement.getAttribute("data-theme");
  const target = current === "dark" ? "light" : "dark";
  document.documentElement.setAttribute("data-theme", target);
  localStorage.setItem("theme", target);
}

// Toast notification helper
function showToast(message) {
  let toast = document.getElementById("site-toast");
  if (!toast) {
    toast = document.createElement("div");
    toast.id = "site-toast";
    toast.className = "toast";
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.classList.add("show");
  setTimeout(() => {
    toast.classList.remove("show");
  }, 2200);
}

// Global Solution Expand / Collapse
function toggleAllSolutions(expand) {
  const details = document.querySelectorAll(".solution-details");
  details.forEach((d) => {
    d.open = expand;
  });
  showToast(expand ? "All solutions expanded" : "All solutions collapsed");
}

// Copy actions
function copyProblemLatex(btn, isSolution = false) {
  const card = btn.closest(".problem-card");
  if (!card) return;
  const rawSelector = isSolution ? ".problem-raw-solution" : ".problem-raw-statement";
  const el = card.querySelector(rawSelector);
  if (!el) return;

  const text = el.textContent.trim();
  navigator.clipboard.writeText(text).then(() => {
    showToast(isSolution ? "Solution LaTeX copied!" : "Problem statement LaTeX copied!");
  }).catch(() => {
    showToast("Failed to copy to clipboard.");
  });
}

function copyPermalink(url) {
  const fullUrl = window.location.origin + url;
  navigator.clipboard.writeText(fullUrl).then(() => {
    showToast("Problem link copied to clipboard!");
  }).catch(() => {
    showToast("Failed to copy link.");
  });
}

// Interactive Solution Status Matrix Filters
function initMatrixFilters() {
  const chips = document.querySelectorAll(".matrix-filter-chip");
  const topicSelect = document.getElementById("matrix-topic-filter");
  const cells = document.querySelectorAll(".status-matrix .matrix-cell");

  if (!chips.length && !topicSelect) return;

  let currentMode = "all"; // "all" | "solved"
  let currentTopic = "all";

  function applyFilter() {
    cells.forEach((cell) => {
      const status = cell.getAttribute("data-status");
      const topic = cell.getAttribute("data-topic-slug");
      let visible = true;

      if (currentMode === "solved") {
        if (status !== "complete" && status !== "draft") {
          visible = false;
        }
      }

      if (currentTopic !== "all") {
        if (topic !== currentTopic) {
          visible = false;
        }
      }

      if (visible) {
        cell.style.opacity = "1";
        cell.style.filter = "none";
      } else {
        cell.style.opacity = "0.15";
        cell.style.filter = "grayscale(100%)";
      }
    });
  }

  chips.forEach((chip) => {
    chip.addEventListener("click", () => {
      chips.forEach((c) => c.classList.remove("active"));
      chip.classList.add("active");
      currentMode = chip.getAttribute("data-filter");
      applyFilter();
    });
  });

  if (topicSelect) {
    topicSelect.addEventListener("change", (e) => {
      currentTopic = e.target.value;
      applyFilter();
    });
  }
}

document.addEventListener("DOMContentLoaded", () => {
  initMatrixFilters();
});
