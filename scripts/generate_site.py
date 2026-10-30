#!/usr/bin/env python3
"""
Pre-build content generator for the Cryptography Comprehensive Exam Hugo website.
Parses LaTeX problem files, applies Union-Find deduplication, converts markup
using Pandoc + MathJax, and outputs structured Hugo content and data files.
"""

import os
import re
import json
import hashlib
import argparse
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SITE_DIR = REPO_ROOT / "site"
CONTENT_DIR = SITE_DIR / "content"
DATA_DIR = SITE_DIR / "data"
CACHE_FILE = SITE_DIR / ".cache" / "pandoc_cache.json"

def resolve_problems_dir(custom_path=None):
    if custom_path:
        p = Path(custom_path).resolve()
        if p.is_dir() and (p / "problems").is_dir():
            return p / "problems"
        return p
    env_dir = os.environ.get("MATH_PROBLEMS_DIR")
    if env_dir:
        p = Path(env_dir).resolve()
        return p / "problems" if (p / "problems").is_dir() else p
    # Check sibling Cryptography_Exam directory
    sibling = REPO_ROOT.parent / "Cryptography_Exam" / "problems"
    if sibling.is_dir():
        return sibling
    # Check local fallback
    local = REPO_ROOT / "problems"
    return local

PROBLEMS_DIR = resolve_problems_dir()

def load_cache():
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def save_cache(cache):
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        CACHE_FILE.write_text(json.dumps(cache), encoding="utf-8")
    except Exception:
        pass

PREFERRED_TOPICS = [
    "Elementary Number Theory",
    "Discrete Logarithm",
    "Elliptic Curves",
    "Provable Security",
    "Digital Signatures",
    "Symmetric-Key Cryptography",
    "Hash Functions",
    "RSA Cryptosystem",
]

TOPIC_INITIALS = {
    "Elementary Number Theory": "ENT",
    "Discrete Logarithm": "DL",
    "Elliptic Curves": "EC",
    "Provable Security": "PS",
    "Digital Signatures": "DS",
    "Symmetric-Key Cryptography": "SKC",
    "Hash Functions": "HF",
    "RSA Cryptosystem": "RSA",
}

OFFICIAL_PDF_URLS = {
    "2025": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/cryptography_comp_2025.pdf",
    "2020": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/cryptography_comp2020.pdf",
    "2019": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/cryptography_2019.pdf",
    "2018": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/crypto2018.pdf",
    "2017": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/crypto_comp_exam_2017.pdf",
    "2016": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/crypto2016-_revised.pdf",
    "2013": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/cryptography.pdf",
    "2011": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/crypt-2011.pdf",
    "2007": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/crypt-2007.pdf",
    "2004": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/crypt-2004.pdf",
    "2003": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/crypt-2003.pdf",
    "2002": "https://uwaterloo.ca/combinatorics-and-optimization/sites/default/files/uploads/documents/crypt-2002.pdf",
}

def topic_slug(topic: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", topic.strip().lower()).strip("-")
    return slug

def parse_same_as(val: str):
    if not val:
        return None
    val = val.strip()
    m_custom = re.match(r"^([a-zA-Z0-9_\-]+)/([a-zA-Z0-9_\-]+)$", val)
    if m_custom:
        return f"{m_custom.group(1)}/{m_custom.group(2)}"
    m_num = re.search(r"(\d{4})[/_\-\s]+(\d+)", val)
    if m_num:
        return f"{m_num.group(1)}/{m_num.group(2)}"
    return None

def parse_problem_file(filepath: Path):
    content = filepath.read_text(encoding="utf-8")
    lines = content.splitlines()

    meta = {
        "title": "",
        "topic": "Unknown",
        "status": "none",
        "author": "",
        "same_as": None,
        "has_solution": False,
        "is_incomplete": False,
        "is_reference": False,
        "raw_statement": "",
        "raw_solution": "",
    }

    for line in lines:
        m = re.match(r"^%\s*([a-zA-Z0-9_\-\s]+)\s*:\s*(.*)$", line)
        if m:
            k = m.group(1).strip().lower().replace(" ", "_").replace("-", "_")
            val = m.group(2).strip()
            if k == "title":
                meta["title"] = val
            elif k == "topic":
                meta["topic"] = "Unknown" if val in ("", "UNKNOWN") else val
            elif k == "status":
                raw_stat = val.lower()
                if raw_stat in ("done", "complete", "solved", "finished"):
                    meta["status"] = "complete"
                elif raw_stat in ("draft", "incomplete", "partial"):
                    meta["status"] = "draft"
                else:
                    meta["status"] = raw_stat
            elif k == "author":
                meta["author"] = val
            elif k in ("same_as", "equivalent_to", "duplicate_of", "variant_of"):
                meta["same_as"] = parse_same_as(val)

    # Extract statement body
    stmt_match = re.search(r"\\begin\{statement\}(.*?)\\end\{statement\}", content, re.DOTALL)
    if stmt_match:
        meta["raw_statement"] = stmt_match.group(1).strip()
    else:
        meta["raw_statement"] = content.strip()

    # Extract solution body
    sol_match = re.search(r"\\begin\{solution\}(.*?)\\end\{solution\}", content, re.DOTALL)
    if sol_match:
        meta["raw_solution"] = sol_match.group(1).strip()

    has_own = bool(meta["raw_solution"].strip())
    meta["has_own_solution"] = has_own
    meta["has_solution"] = has_own
    if has_own:
        if meta["status"] in ("draft", "incomplete", "partial"):
            meta["status"] = "draft"
            meta["is_incomplete"] = True
        else:
            meta["status"] = "complete"
            meta["is_incomplete"] = False
    meta["is_reference"] = False

    return meta

def convert_latex_to_html(latex_str: str, cache: dict = None) -> str:
    if not latex_str.strip():
        return ""
    # Normalize enumitem syntax so pandoc creates proper <ol type="...">
    proc_latex = re.sub(r"\\begin\{enumerate\}\[[^\]]*label=\(?\\roman\*\)?[^\]]*\]", r"\\begin{enumerate}[(i)]", latex_str)
    proc_latex = re.sub(r"\\begin\{enumerate\}\[[^\]]*label=\(?\\alph\*\)?[^\]]*\]", r"\\begin{enumerate}[(a)]", proc_latex)
    proc_latex = re.sub(r"\\begin\{enumerate\}\[[^\]]*label=\(?\\arabic\*\)?[^\]]*\]", r"\\begin{enumerate}[1.]", proc_latex)

    if cache is not None:
        h = hashlib.sha256(proc_latex.strip().encode("utf-8")).hexdigest()
        if h in cache:
            return cache[h]

    # Use pandoc with mathjax
    res = subprocess.run(
        ["pandoc", "-f", "latex", "-t", "html", "--mathjax"],
        input=proc_latex,
        capture_output=True,
        text=True,
        check=True
    )
    html = res.stdout.strip()
    # Unpack outer <div class="statement"> or <div class="solution"> only if pandoc generated it
    if re.match(r"^<div class=\"(?:statement|solution)\">", html):
        html = re.sub(r"^<div class=\"(?:statement|solution)\">\s*", "", html)
        html = re.sub(r"\s*</div>$", "", html)

    # Bind trailing punctuation to inline math so justified lines never orphan punctuation marks
    html = re.sub(
        r'(<span class="math inline">(?:(?!</span>).)*?</span>)([,.;:!?\)\'\"’”\]]+)',
        r'<span class="math-punct">\1\2</span>',
        html,
        flags=re.DOTALL
    )

    if cache is not None:
        cache[h] = html
    return html

def strip_tags(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def main(cache: dict = None, quiet: bool = False, problems_dir=None):
    global PROBLEMS_DIR
    if problems_dir:
        PROBLEMS_DIR = resolve_problems_dir(problems_dir)
    if cache is None:
        cache = load_cache()
    if not quiet:
        print("Parsing LaTeX problem files...")
    years_data = {}
    custom_data = {}
    all_problems = {}

    year_dirs = sorted([d for d in PROBLEMS_DIR.iterdir() if d.is_dir() and re.match(r"^\d{4}$", d.name)], key=lambda p: int(p.name), reverse=True)
    custom_dirs = sorted([d for d in PROBLEMS_DIR.iterdir() if d.is_dir() and not re.match(r"^\d{4}$", d.name)])

    max_problems = 0
    for ydir in year_dirs:
        year = ydir.name
        prob_files = sorted(
            [f for f in ydir.glob("*.tex") if re.match(r"^\d+\.tex$", f.name)],
            key=lambda f: int(f.stem)
        )
        years_data[year] = []
        if len(prob_files) > max_problems:
            max_problems = len(prob_files)

        for pf in prob_files:
            p_num = int(pf.stem)
            p_id = f"{year}/{p_num}"
            meta = parse_problem_file(pf)
            meta["id"] = p_id
            meta["slug"] = f"{year}-{p_num}"
            meta["year"] = year
            meta["problem"] = p_num
            meta["is_custom"] = False
            meta["file"] = pf
            meta["url"] = f"/problems/{year}-{p_num}/"
            years_data[year].append(meta)
            all_problems[p_id] = meta

    for cdir in custom_dirs:
        dir_name = cdir.name
        custom_data[dir_name] = []
        for pf in sorted(cdir.glob("*.tex")):
            name = pf.stem
            p_id = f"{dir_name}/{name}"
            meta = parse_problem_file(pf)
            meta["id"] = p_id
            meta["slug"] = f"{dir_name}-{name}"
            meta["dir"] = dir_name
            meta["name"] = name
            meta["is_custom"] = True
            meta["file"] = pf
            meta["url"] = f"/problems/{dir_name}-{name}/"
            custom_data[dir_name].append(meta)
            all_problems[p_id] = meta

    print(f"Loaded {len(all_problems)} problem definitions. Max problems in any year: {max_problems}")

    # Union-Find deduplication matching preamble.tex
    parent = {pid: pid for pid in all_problems}

    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j

    for pid, meta in all_problems.items():
        if meta["same_as"] and meta["same_as"] in parent:
            union(pid, meta["same_as"])

    clusters_by_root = {}
    for pid in all_problems:
        r = find(pid)
        if r not in clusters_by_root:
            clusters_by_root[r] = []
        clusters_by_root[r].append(all_problems[pid])

    # Build cluster objects
    clusters = []
    total_solutions = 0
    total_drafts = 0

    for root, members in clusters_by_root.items():
        yearly_members = [m for m in members if not m["is_custom"]]
        custom_members = [m for m in members if m["is_custom"]]

        yearly_members.sort(key=lambda m: (int(m["year"]), -m["problem"]), reverse=True)

        # Elect canonical problem:
        # 1. Any member with a solution written on its document (prefer custom if solved, else most recent yearly solved)
        # 2. If none solved: prefer custom, else root/base problem (no same_as), else first member
        solved_custom = [m for m in custom_members if m["has_own_solution"]]
        solved_yearly = [m for m in yearly_members if m["has_own_solution"]]
        if solved_custom:
            canonical = solved_custom[0]
        elif solved_yearly:
            canonical = solved_yearly[0]
        elif custom_members:
            canonical = custom_members[0]
        else:
            base_yearly = [m for m in yearly_members if not m["same_as"]]
            canonical = base_yearly[0] if base_yearly else yearly_members[0]

        cluster_topic = canonical["topic"]
        cluster_title = canonical["title"]
        if not cluster_title:
            for m in members:
                if m["title"]:
                    cluster_title = m["title"]
                    break

        has_sol = False
        is_inc = False
        solution_author = ""
        for m in members:
            if m["has_own_solution"]:
                if m["status"] == "complete":
                    has_sol = True
                    is_inc = False
                    solution_author = m["author"] or solution_author
                    break
                elif m["status"] in ("draft", "incomplete") and not has_sol:
                    has_sol = True
                    is_inc = True
                    solution_author = m["author"] or solution_author

        if has_sol:
            if is_inc:
                total_drafts += 1
            else:
                total_solutions += 1

        cluster = {
            "id": root,
            "canonical": canonical,
            "members": members,
            "yearly_members": yearly_members,
            "custom_members": custom_members,
            "topic": cluster_topic,
            "title": cluster_title,
            "has_solution": has_sol,
            "is_incomplete": is_inc,
            "author": solution_author,
        }
        clusters.append(cluster)

        # Propagate cluster info and variant solutions back to each problem
        for m in members:
            m["cluster"] = cluster
            m["canonical_id"] = canonical["id"]
            m["canonical_url"] = canonical["url"]
            m["is_canonical"] = (m["id"] == canonical["id"])

        for m in members:
            m["variant_solutions"] = [
                {
                    "id": other["id"],
                    "url": other["url"],
                    "title": other["title"] or f"Problem {other['id']}",
                    "status": "draft" if other["is_incomplete"] else "complete",
                    "author": other["author"] or cluster["author"],
                }
                for other in members
                if other["id"] != m["id"] and other["has_own_solution"]
            ]
            m["has_variant_solution"] = len(m["variant_solutions"]) > 0
            m["is_reference"] = m["has_variant_solution"] and not m["has_own_solution"]

    if not quiet:
        print(f"Formed {len(clusters)} distinct clusters ({total_solutions} complete, {total_drafts} drafts).")
        print("Converting LaTeX statements and solutions to HTML via Pandoc...")

    for pid, meta in all_problems.items():
        meta["statement_html"] = convert_latex_to_html(meta["raw_statement"], cache=cache)
        if meta["has_own_solution"]:
            meta["solution_html"] = convert_latex_to_html(meta["raw_solution"], cache=cache)
            meta["solution_author"] = meta["author"] or meta["cluster"]["author"]
            meta["solution_source_file"] = f"problems/{meta['file'].relative_to(PROBLEMS_DIR)}"
        else:
            meta["solution_html"] = ""
            meta["solution_author"] = ""
            meta["solution_source_file"] = ""

    # Sort topics in preferred order
    all_topics = set(c["topic"] for c in clusters)
    def topic_sort_key(t):
        if t in PREFERRED_TOPICS:
            return PREFERRED_TOPICS.index(t)
        return 999
    sorted_topics = sorted(all_topics, key=topic_sort_key)

    # Build matrix JSON
    print("Generating status matrix data...")
    matrix_years = []
    for ydir in year_dirs:
        year = ydir.name
        p_list = []
        for i in range(1, max_problems + 1):
            p_meta = next((m for m in years_data[year] if m["problem"] == i), None)
            if p_meta:
                stat = "none"
                if p_meta["has_own_solution"]:
                    stat = "draft" if p_meta["is_incomplete"] else "complete"
                elif p_meta["has_variant_solution"]:
                    stat = "draft" if p_meta["cluster"]["is_incomplete"] else "complete"
                p_list.append({
                    "problem": i,
                    "id": p_meta["id"],
                    "title": p_meta["title"],
                    "topic": p_meta["topic"],
                    "topic_abbr": TOPIC_INITIALS.get(p_meta["topic"], p_meta["topic"][:3].upper()),
                    "topic_slug": topic_slug(p_meta["topic"]),
                    "status": stat,
                    "is_reference": p_meta["is_reference"],
                    "has_solution": p_meta["has_own_solution"] or p_meta["has_variant_solution"],
                    "has_own_solution": p_meta["has_own_solution"],
                    "has_variant_solution": p_meta["has_variant_solution"],
                    "variant_solutions": p_meta["variant_solutions"],
                    "url": p_meta["url"],
                    "canonical_url": p_meta["canonical_url"],
                })
            else:
                p_list.append(None)
        matrix_years.append({
            "year": year,
            "official_pdf": OFFICIAL_PDF_URLS.get(year, ""),
            "problems": p_list,
        })

    # Topic summaries
    topic_summaries = []
    for t in sorted_topics:
        t_clusters = [c for c in clusters if c["topic"] == t]
        solved_count = sum(1 for c in t_clusters if c["has_solution"] and not c["is_incomplete"])
        draft_count = sum(1 for c in t_clusters if c["is_incomplete"])
        total_cluster_problems = len(t_clusters)
        topic_summaries.append({
            "name": t,
            "abbr": TOPIC_INITIALS.get(t, t[:3].upper()),
            "slug": topic_slug(t),
            "cluster_count": total_cluster_problems,
            "solved_count": solved_count,
            "draft_count": draft_count,
            "unsolved_count": total_cluster_problems - solved_count - draft_count,
        })

    stats_data = {
        "total_problems": len(all_problems),
        "total_clusters": len(clusters),
        "total_solutions": total_solutions,
        "total_drafts": total_drafts,
        "total_unsolved": len(clusters) - total_solutions - total_drafts,
        "total_years": len(year_dirs),
        "year_min": min(int(ydir.name) for ydir in year_dirs),
        "year_max": max(int(ydir.name) for ydir in year_dirs),
    }

    # Search index
    print("Building client-side search index...")
    search_index = []
    for pid, meta in all_problems.items():
        stat = "none"
        if meta["has_own_solution"]:
            stat = "draft" if meta["is_incomplete"] else "complete"
        elif meta["has_variant_solution"]:
            stat = "draft" if meta["cluster"]["is_incomplete"] else "complete"

        plain_stmt = strip_tags(meta["statement_html"])
        search_index.append({
            "id": meta["id"],
            "slug": meta["slug"],
            "title": meta["title"] or f"Problem {meta['id']}",
            "topic": meta["topic"],
            "year": meta.get("year", "Composite"),
            "problem": meta.get("problem", meta.get("name", "")),
            "status": stat,
            "is_reference": meta["is_reference"],
            "has_solution": meta["has_own_solution"] or meta["has_variant_solution"],
            "has_own_solution": meta["has_own_solution"],
            "has_variant_solution": meta["has_variant_solution"],
            "url": meta["url"],
            "statement_snippet": plain_stmt[:240] + ("..." if len(plain_stmt) > 240 else ""),
        })

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    STATIC_DATA_DIR = SITE_DIR / "static" / "data"
    STATIC_DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(DATA_DIR / "status_matrix.json", "w", encoding="utf-8") as f:
        json.dump({
            "max_problems": max_problems,
            "years": matrix_years,
            "topics": topic_summaries,
            "stats": stats_data,
        }, f, indent=2)

    with open(DATA_DIR / "search_index.json", "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2)

    with open(STATIC_DATA_DIR / "search_index.json", "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2)

    with open(DATA_DIR / "stats.json", "w", encoding="utf-8") as f:
        json.dump(stats_data, f, indent=2)

    # Write Hugo content files
    print("Generating Hugo markdown content...")
    problems_content_dir = CONTENT_DIR / "problems"
    topics_content_dir = CONTENT_DIR / "topics"
    years_content_dir = CONTENT_DIR / "years"

    for d in (problems_content_dir, topics_content_dir, years_content_dir):
        d.mkdir(parents=True, exist_ok=True)

    # 1. Individual problem pages
    for pid, meta in all_problems.items():
        cluster = meta["cluster"]
        cluster_members = [
            {"id": m["id"], "url": m["url"], "is_current": (m["id"] == meta["id"])}
            for m in cluster["members"]
        ]
        appearances = [f"{m['year']}/{m['problem']}" for m in cluster["yearly_members"]]
        if not appearances and meta.get("is_custom"):
            appearances = [meta.get("name", "")]

        appearance_links = [
            {"text": f"{m['year']}/{m['problem']}", "url": m["url"]}
            for m in cluster["yearly_members"]
        ]
        if not appearance_links and meta.get("is_custom"):
            appearance_links = [{"text": meta.get("name", ""), "url": meta["url"]}]

        stat = "none"
        if meta["has_own_solution"]:
            stat = "draft" if meta["is_incomplete"] else "complete"
        elif meta["has_variant_solution"]:
            stat = "draft" if cluster["is_incomplete"] else "complete"

        fm = {
            "title": meta["title"] or f"Problem {meta['id']}",
            "slug": meta["slug"],
            "id": meta["id"],
            "problem_id": meta["id"],
            "year": meta.get("year", "Composite"),
            "problem": meta.get("problem", 0),
            "problem_number": meta.get("problem", 0),
            "topic": meta["topic"],
            "topic_slug": topic_slug(meta["topic"]),
            "status": stat,
            "is_incomplete": meta["is_incomplete"],
            "is_reference": meta["is_reference"],
            "has_own_solution": meta["has_own_solution"],
            "has_solution": meta["has_own_solution"] or meta["has_variant_solution"],
            "has_variant_solution": meta["has_variant_solution"],
            "variant_solutions": meta["variant_solutions"],
            "is_canonical": meta["is_canonical"],
            "canonical_id": meta["canonical_id"],
            "canonical_url": meta["canonical_url"],
            "author": meta["author"] or cluster["author"],
            "cluster_members": cluster_members,
            "appearances": appearances,
            "appearance_links": appearance_links,
            "source_file": f"problems/{meta['file'].relative_to(PROBLEMS_DIR)}",
            "url": meta["url"],
            "statement_html": meta["statement_html"],
            "solution_html": meta["solution_html"],
            "raw_statement": meta["raw_statement"],
            "raw_solution": meta["raw_solution"],
        }

        with open(problems_content_dir / f"{meta['slug']}.md", "w", encoding="utf-8") as f:
            f.write(f"---\n{json.dumps(fm, indent=2)}\n---\n")

    # 2. Topic pages
    for topic_info in topic_summaries:
        t_name = topic_info["name"]
        t_slug = topic_info["slug"]
        t_clusters = [c for c in clusters if c["topic"] == t_name]

        def cluster_sort_key(c):
            if c["yearly_members"]:
                m = c["yearly_members"][0]
                return int(m["year"]) * 100 - m["problem"]
            return 0
        t_clusters.sort(key=cluster_sort_key, reverse=True)

        cluster_records = []
        for c in t_clusters:
            can = c["canonical"]
            stat = "none"
            if can["has_own_solution"]:
                stat = "draft" if can["is_incomplete"] else "complete"
            
            appearances = [f"{m['year']}/{m['problem']}" for m in c["yearly_members"]]
            if not appearances and can["is_custom"]:
                appearances = [can["name"]]

            appearance_links = [
                {"text": f"{m['year']}/{m['problem']}", "url": m["url"]}
                for m in c["yearly_members"]
            ]
            if not appearance_links and can["is_custom"]:
                appearance_links = [{"text": can["name"], "url": can["url"]}]

            cluster_records.append({
                "id": c["id"],
                "title": c["title"] or f"Problem {can['id']}",
                "canonical_id": can["id"],
                "canonical_url": can["url"],
                "appearances": appearances,
                "appearance_links": appearance_links,
                "status": stat,
                "has_own_solution": can["has_own_solution"],
                "has_solution": can["has_own_solution"],
                "has_variant_solution": can["has_variant_solution"],
                "variant_solutions": can["variant_solutions"],
                "is_incomplete": can["is_incomplete"],
                "author": can["author"] or c["author"],
                "statement_html": can["statement_html"],
                "solution_html": can["solution_html"],
                "raw_statement": can["raw_statement"],
                "raw_solution": can["raw_solution"],
                "source_file": f"problems/{can['file'].relative_to(PROBLEMS_DIR)}",
            })

        fm = {
            "title": t_name,
            "topic": t_name,
            "topic_slug": t_slug,
            "abbr": topic_info["abbr"],
            "cluster_count": len(cluster_records),
            "solved_count": topic_info["solved_count"],
            "draft_count": topic_info["draft_count"],
            "clusters": cluster_records,
        }

        with open(topics_content_dir / f"{t_slug}.md", "w", encoding="utf-8") as f:
            f.write(f"---\n{json.dumps(fm, indent=2)}\n---\n")

    # 3. Year pages
    for ydir in year_dirs:
        year = ydir.name
        y_problems = sorted(years_data[year], key=lambda m: m["problem"])
        prob_records = []
        for p in y_problems:
            c = p["cluster"]
            stat = "none"
            if p["has_own_solution"]:
                stat = "draft" if p["is_incomplete"] else "complete"
            elif p["has_variant_solution"]:
                stat = "draft" if c["is_incomplete"] else "complete"
            
            appearances = [f"{m['year']}/{m['problem']}" for m in c["yearly_members"]]
            if not appearances and p.get("is_custom"):
                appearances = [p.get("name", "")]

            appearance_links = [
                {"text": f"{m['year']}/{m['problem']}", "url": m["url"]}
                for m in c["yearly_members"]
            ]
            if not appearance_links and p.get("is_custom"):
                appearance_links = [{"text": p.get("name", ""), "url": p["url"]}]

            prob_records.append({
                "problem": p["problem"],
                "id": p["id"],
                "slug": p["slug"],
                "title": p["title"] or f"Problem {p['id']}",
                "topic": p["topic"],
                "topic_abbr": TOPIC_INITIALS.get(p["topic"], p["topic"][:3].upper()),
                "topic_slug": topic_slug(p["topic"]),
                "status": stat,
                "appearances": appearances,
                "appearance_links": appearance_links,
                "has_own_solution": p["has_own_solution"],
                "has_solution": p["has_own_solution"] or p["has_variant_solution"],
                "has_variant_solution": p["has_variant_solution"],
                "variant_solutions": p["variant_solutions"],
                "is_incomplete": p["is_incomplete"],
                "is_reference": p["is_reference"],
                "is_canonical": p["is_canonical"],
                "canonical_id": p["canonical_id"],
                "canonical_url": p["canonical_url"],
                "author": p["author"] or c["author"],
                "statement_html": p["statement_html"],
                "solution_html": p["solution_html"],
                "raw_statement": p["raw_statement"],
                "raw_solution": p["raw_solution"],
                "source_file": f"problems/{p['file'].relative_to(PROBLEMS_DIR)}",
            })

        fm = {
            "title": f"{year} Cryptography Comprehensive Exam",
            "year": year,
            "official_pdf": OFFICIAL_PDF_URLS.get(year, ""),
            "problem_count": len(prob_records),
            "problems": prob_records,
        }

        with open(years_content_dir / f"{year}.md", "w", encoding="utf-8") as f:
            f.write(f"---\n{json.dumps(fm, indent=2)}\n---\n")

    # 4. Section _index.md files (sections suppressed from rendering standalone list pages)
    (TOPICS_DIR := CONTENT_DIR / "topics").mkdir(parents=True, exist_ok=True)
    with open(TOPICS_DIR / "_index.md", "w", encoding="utf-8") as f:
        f.write("---\nbuild:\n  render: never\n  list: never\n---\n")

    (YEARS_DIR := CONTENT_DIR / "years").mkdir(parents=True, exist_ok=True)
    with open(YEARS_DIR / "_index.md", "w", encoding="utf-8") as f:
        f.write("---\nbuild:\n  render: never\n  list: never\n---\n")

    (PROBS_DIR := CONTENT_DIR / "problems").mkdir(parents=True, exist_ok=True)
    with open(PROBS_DIR / "_index.md", "w", encoding="utf-8") as f:
        f.write("---\nbuild:\n  render: never\n  list: never\n---\n")

    # 5. Homepage _index.md
    with open(CONTENT_DIR / "_index.md", "w", encoding="utf-8") as f:
        f.write(f"""---
title: "University of Waterloo Cryptography Comprehensive Exam"
type: "home"
aliases:
  - "/topics/"
  - "/years/"
stats: {json.dumps(stats_data)}
---
""")

    save_cache(cache)
    if not quiet:
        print("Site generation complete!")

def watch_problems(problems_dir=None):
    global PROBLEMS_DIR
    if problems_dir:
        PROBLEMS_DIR = resolve_problems_dir(problems_dir)
    import time
    cache = load_cache()
    print("[Watcher] Initial build with cache...")
    main(cache=cache, quiet=False)
    print("\n[Watcher] Watching problems/ for changes... (Press Ctrl+C to stop)")

    mtimes = {}
    for p in PROBLEMS_DIR.rglob("*.tex"):
        try:
            mtimes[p] = p.stat().st_mtime
        except Exception:
            pass

    try:
        while True:
            time.sleep(0.3)
            changed = False
            current_files = set(PROBLEMS_DIR.rglob("*.tex"))
            if set(mtimes.keys()) != current_files:
                changed = True
                mtimes = {p: p.stat().st_mtime for p in current_files}
            else:
                for p in current_files:
                    try:
                        mtime = p.stat().st_mtime
                        if mtime != mtimes.get(p):
                            mtimes[p] = mtime
                            changed = True
                            print(f"\n[Watcher] Detected change in: {p.relative_to(REPO_ROOT)}")
                    except Exception:
                        pass

            if changed:
                t0 = time.time()
                main(cache=cache, quiet=True)
                save_cache(cache)
                print(f"[Watcher] Content updated in {time.time() - t0:.3f}s -> Hugo will live-reload!")
    except KeyboardInterrupt:
        print("\n[Watcher] Stopped watching.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Hugo content from LaTeX problems")
    parser.add_argument("-w", "--watch", action="store_true", help="Watch problems directory for changes and regenerate automatically")
    parser.add_argument("--math-dir", default=None, help="Path to math repository or problems directory")
    args = parser.parse_args()

    if args.watch:
        watch_problems(problems_dir=args.math_dir)
    else:
        main(problems_dir=args.math_dir)
