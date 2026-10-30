#!/usr/bin/env python3
import os
import re

def clean_comment_headers(lines):
    cleaned = []
    started = False
    for line in lines:
        if not started:
            if line.strip().startswith("%") or line.strip() == "":
                continue
            started = True
        cleaned.append(line)
    return "".join(cleaned).strip()

def read_single_line_file(path, default=""):
    if not os.path.isfile(path):
        return default
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s and not s.startswith("%"):
                return s
    return default

def migrate():
    problems_dir = "problems"
    year_dirs = sorted([d for d in os.listdir(problems_dir) if re.match(r"^\d{4}$", d)], reverse=True)
    
    total_migrated = 0
    total_solutions = 0

    for year in sorted(year_dirs, key=lambda y: int(y)):
        ydir = os.path.join(problems_dir, year)
        # Find all problem numbers
        files = os.listdir(ydir)
        prob_nums = sorted(list(set(
            int(m.group(1)) for f in files if (m := re.match(r"^(\d+)\.tex$", f))
        )))

        for p in prob_nums:
            p_str = str(p)
            prob_file = os.path.join(ydir, f"{p_str}.tex")
            title_file = os.path.join(ydir, f"{p_str}-title.tex")
            topic_file = os.path.join(ydir, f"{p_str}-topic.tex")
            sol_file = os.path.join(ydir, f"{p_str}-solution.tex")

            title = read_single_line_file(title_file, "")
            topic = read_single_line_file(topic_file, "Unknown")
            if topic == "UNKNOWN" or not topic:
                topic = "Unknown"

            # Read statement
            with open(prob_file, "r", encoding="utf-8") as f:
                statement_content = clean_comment_headers(f.readlines())

            # Read solution if present
            has_sol = os.path.isfile(sol_file)
            solution_body = ""
            status = "none"
            author = ""

            if has_sol:
                with open(sol_file, "r", encoding="utf-8") as f:
                    sol_lines = f.readlines()
                solution_body = clean_comment_headers(sol_lines)
                if "Same as" in solution_body or "hyperref" in solution_body:
                    status = "reference"
                elif "incomplete" in solution_body.lower() or "paddock" in solution_body.lower():
                    status = "draft"
                else:
                    status = "complete"
                
                if year == "2019" and p == 1:
                    author = "Guilherme Zeus Dantas e Moura"
                
                total_solutions += 1

            # Format new unified file
            header_lines = [
                f"% Year: {year}",
                f"% Problem: {p}",
                f"% Title: {title}",
                f"% Topic: {topic}",
                "",
                "\\begin{statement}",
                statement_content,
                "\\end{statement}",
                ""
            ]

            if status != "none" and solution_body:
                header_lines.append(f"% Status: {status}")
                if author:
                    header_lines.append(f"% Author: {author}")
                header_lines.append("")
                header_lines.append("\\begin{solution}")
                header_lines.append(solution_body)
                header_lines.append("\\end{solution}")
            else:
                header_lines.append("% Status: none")

            unified_content = "\n".join(header_lines) + "\n"

            # Write to prob_file
            with open(prob_file, "w", encoding="utf-8") as f:
                f.write(unified_content)

            # Remove obsolete auxiliary files
            if os.path.isfile(title_file):
                os.remove(title_file)
            if os.path.isfile(topic_file):
                os.remove(topic_file)
            if os.path.isfile(sol_file):
                os.remove(sol_file)

            total_migrated += 1

    print(f"Migration complete: {total_migrated} problems processed, {total_solutions} solutions merged.")

if __name__ == "__main__":
    migrate()
