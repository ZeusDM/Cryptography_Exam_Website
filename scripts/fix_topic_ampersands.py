#!/usr/bin/env python3
"""
Replace ampersands (&) with the word 'and' in all problems/*/*_topic.tex files.
Run from repository root: python3 scripts/fix_topic_ampersands.py
"""
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parents[1]
problems_dir = repo_root / 'problems'
if not problems_dir.exists():
    print(f"Problems directory not found at {problems_dir}")
    sys.exit(1)

changed = 0
checked = 0
for topic_path in sorted(problems_dir.glob('*/*_topic.tex')):
    checked += 1
    text = topic_path.read_text(encoding='utf-8')
    if '&' in text:
        new_text = text.replace('&', 'and')
        topic_path.write_text(new_text, encoding='utf-8')
        changed += 1

print(f"Checked {checked} topic files")
print(f"Replaced ampersands in {changed} files")
