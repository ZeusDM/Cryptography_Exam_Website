import re
from pathlib import Path
from openai import OpenAI

client = OpenAI()

# -----------------------------------------------------------
# EDITING PROMPT
# -----------------------------------------------------------

def editing_prompt(year, number, title_line, body):
    return f"""
You are editing a LaTeX problem from a mathematics exam.

Rules:
- DO NOT modify the header: % YEAR {year}, PROBLEM {number}
- The line immediately after the header is the *title*. Keep the title exactly as a single line.
- Use \\(...\\) for all inline mathematics.
- Use appropriate display math environments from amsmath (equation, align, gathered, etc.).
- For functions, use \\colon in place of ":".
- For named operators, wrap in \\operatorname{{...}}.
- Use \\mathrm{{...}} or \\mathsf{{...}} for upright mathematical text when appropriate.
- For lists, use enumerate with label=(alph) for alphabetic lists and label=(roman) for roman numeral lists.
- Keep the mathematical meaning EXACT.
- Do not add explanations, commentary, or extra text. Only return the cleaned LaTeX content (title, blank line, body).
- Do not reintroduce the header.
- Do not renumber the problem.

Here is the problem title and body to edit:

TITLE:
{title_line}

BODY:
{body}
""".strip()


# -----------------------------------------------------------
# CORE PROCESSING
# -----------------------------------------------------------

BASE = Path("problems")

for year_dir in sorted(BASE.iterdir()):
    if not year_dir.is_dir():
        continue

    year = year_dir.name
    print(f"Processing year {year}...")

    for tex_path in sorted(year_dir.glob("*.tex")):
        number = tex_path.stem

        with open(tex_path, "r") as f:
            raw = f.read()

        lines = raw.splitlines()

        # HEADER
        header = lines[0].strip()

        # TITLE = line immediately after header
        if len(lines) < 2:
            print(f"  Warning: file {tex_path} has no title line.")
            continue

        title_line = lines[1].rstrip()

        # BODY = everything after the title line
        body = "\n".join(lines[2:]).strip()

        print(f"  Editing {year}/{number}...")

        prompt_text = editing_prompt(year, number, title_line, body)

        resp = client.responses.create(
            model="gpt-5-nano",
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "input_text", "text": prompt_text}
                    ],
                }
            ],
        )

        edited = resp.output_text.strip().splitlines()

        # You should get: first line = edited title
        edited_title = edited[0].rstrip()
        edited_body = "\n".join(edited[1:]).strip()

        # Write back
        with open(tex_path, "w") as f:
            f.write(header + "\n")
            f.write(edited_title + "\n")
            f.write("\n")                     # required blank line
            f.write(edited_body + "\n")

print("Done.")
