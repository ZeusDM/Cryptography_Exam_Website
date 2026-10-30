/**
 * Instant Client-Side Search for UW Cryptography Exam Site
 * Uses site/data/search_index.json without any external dependencies.
 */

let searchIndex = null;

async function loadSearchIndex() {
  if (searchIndex) return searchIndex;
  try {
    const res = await fetch((window.baseURL ? window.baseURL.replace(/\/+$/, "") : "") + "/data/search_index.json");
    searchIndex = await res.json();
    return searchIndex;
  } catch (err) {
    console.error("Failed to load search index:", err);
    return [];
  }
}

function openSearch() {
  const modal = document.getElementById("search-modal");
  const input = document.getElementById("search-modal-input");
  if (!modal) return;
  modal.classList.add("open");
  loadSearchIndex();
  setTimeout(() => input && input.focus(), 50);
}

function closeSearch() {
  const modal = document.getElementById("search-modal");
  if (!modal) return;
  modal.classList.remove("open");
}

function performSearch(query) {
  const resultsContainer = document.getElementById("search-modal-results");
  if (!resultsContainer || !searchIndex) return;

  const q = query.trim().toLowerCase();
  if (!q) {
    resultsContainer.innerHTML = '<li style="padding:1rem; text-align:center; color:var(--text-muted); font-size:0.9rem;">Type to search problems, topics, years, or mathematical terms...</li>';
    return;
  }

  const terms = q.split(/\s+/).filter(Boolean);
  const matched = searchIndex.filter((item) => {
    const text = (item.title + " " + item.topic + " " + item.year + " " + item.id + " " + item.statement_snippet).toLowerCase();
    return terms.every((t) => text.includes(t));
  });

  if (matched.length === 0) {
    resultsContainer.innerHTML = `<li style="padding:1.5rem; text-align:center; color:var(--text-muted);">No problems found matching <strong>"${escapeHtml(query)}"</strong></li>`;
    return;
  }

  const html = matched.slice(0, 15).map((item) => {
    const statusPill = item.status === "complete" 
      ? '<span class="badge" style="background:var(--badge-green-bg); color:var(--badge-green-text);">Solved</span>'
      : item.status === "draft"
      ? '<span class="badge" style="background:var(--badge-orange-bg); color:var(--badge-orange-text);">Draft</span>'
      : '<span class="badge" style="background:var(--badge-gray-bg); color:var(--badge-gray-text);">No solution</span>';

    return `
      <li class="search-result-item">
        <a href="${(window.baseURL ? window.baseURL.replace(/\/+$/, "") : "") + ("/" + item.url.replace(/^\/+/, ""))}">
          <div class="search-result-title">
            <span>${item.id}: ${escapeHtml(item.title)}</span>
            ${statusPill}
          </div>
          <div style="font-size:0.75rem; color:var(--primary); margin-bottom:0.25rem;">
            ${escapeHtml(item.topic)} • ${item.year}
          </div>
          <div class="search-result-snippet">
            ${escapeHtml(item.statement_snippet)}
          </div>
        </a>
      </li>
    `;
  }).join("");

  resultsContainer.innerHTML = html;
}

function escapeHtml(str) {
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

document.addEventListener("DOMContentLoaded", () => {
  const triggerBtn = document.getElementById("search-trigger");
  const modal = document.getElementById("search-modal");
  const input = document.getElementById("search-modal-input");

  if (triggerBtn) {
    triggerBtn.addEventListener("click", openSearch);
  }

  if (modal) {
    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeSearch();
    });
  }

  if (input) {
    input.addEventListener("input", (e) => performSearch(e.target.value));
  }

  // Keyboard shortcut listener (/ or Ctrl+K or Cmd+K)
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") {
      closeSearch();
    } else if ((e.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "TEXTAREA") ||
               ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) {
      e.preventDefault();
      openSearch();
    }
  });
});
