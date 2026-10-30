import os
import re
import base64
import subprocess
from pathlib import Path
from openai import OpenAI

client = OpenAI()

#############################################
# Prompt template
#############################################

def prompt_for_year(year: str) -> str:
    return f"""
You will receive scanned images from an exam written in the year {year}.

Your task:
- Extract every problem from the pages (after the title page).
- Return ONLY the LaTeX problem statements.
- Each problem MUST begin with a header of the form:
% YEAR {year}, PROBLEM X
- After this header, write the full problem statement with no problem number inside the text.
- Use \\(...\\) for inline math.
- Use amsmath environments for display math (equation, align, gathered, etc.).
- Assume amsmath and amsfonts are already loaded.
- Merge multi-page problems into a single continuous problem.
- Do NOT include explanations, commentary, or anything outside the problem statements.
""".strip()


#############################################
# Helper functions
#############################################

def encode_image(path: Path) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def extract_year(filename: str) -> str:
    m = re.match(r"(\d{4})\.pdf$", filename)
    if not m:
        raise ValueError(f"Invalid filename format: {filename}")
    return m.group(1)


#############################################
# Main processing
#############################################

ORIGINAL = Path("original")
PROBLEMS = Path("problems")
PROBLEMS.mkdir(exist_ok=True)

pdf_files = sorted([f for f in ORIGINAL.iterdir() if f.name.endswith(".pdf")])

for pdf in pdf_files:
    year = extract_year(pdf.name)
    print(f"Processing {year}...")

    outdir = ORIGINAL / f"tmp_{year}"
    outdir.mkdir(exist_ok=True)

    ###########################################################
    # Step 1: Convert PDF pages to high-quality PNG images
    ###########################################################
    print(f"[{year}] Converting PDF pages with ImageMagick...")

    cmd = [
        "magick",
        "-density", "300",
        str(pdf),
        "-alpha", "remove",
        "-alpha", "off",
        "-background", "white",
        str(outdir / "%03d.png"),
    ]
    subprocess.run(cmd, check=True)

    pages = sorted(outdir.glob("*.png"))
    if len(pages) <= 1:
        print(f"[{year}] Warning: PDF seems to have only one page.")
        continue

    # Skip the title page (page 1)
    content_pages = pages[1:]

    ###########################################################
    # Step 2: Encode images and call the API
    ###########################################################

    print(f"[{year}] Encoding images...")
    encoded_images = [
        {
            "type": "input_image",
            "image_url": f"data:image/png;base64,{encode_image(p)}"
        }
        for p in content_pages
    ]

    prompt_text = prompt_for_year(year)

    print(f"[{year}] Sending images to OpenAI API...")
    resp = client.responses.create(
        model="gpt-5-nano",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt_text},
                    *encoded_images
                ],
            }
        ],
    )

    full_text = resp.output_text

    ###########################################################
    # Step 3: Split into problems
    ###########################################################

    print(f"[{year}] Parsing problems...")

    pattern = r"(% YEAR " + year + r", PROBLEM \d+)"
    blocks = re.split(pattern, full_text)
    # blocks = ["", "% YEAR YYYY, PROBLEM 1", "<content>", "% YEAR YYYY, PROBLEM 2", "<content>", ...]

    problems_dir = PROBLEMS / year
    problems_dir.mkdir(parents=True, exist_ok=True)

    # Iterate pairs (header, body)
    for i in range(1, len(blocks), 2):
        header = blocks[i].strip()
        body = blocks[i+1].strip()

        # Extract problem number
        m = re.match(r"% YEAR " + year + r", PROBLEM (\d+)", header)
        if not m:
            continue
        number = int(m.group(1))

        outpath = problems_dir / f"{number}.tex"
        print(f"[{year}] Writing problem {number} -> {outpath}")

        with open(outpath, "w") as f:
            f.write(header + "\n")
            f.write(body + "\n")

    ###########################################################
    # Step 4: Optional cleanup
    ###########################################################

    print(f"[{year}] Cleaning up temporary images...")
    for p in pages:
        p.unlink()
    outdir.rmdir()

print("Done.")
