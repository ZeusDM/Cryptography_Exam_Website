#!/usr/bin/env python3
"""
Remove the first line from all files matching problems/*/*_title.tex

Creates a .bak copy of each file before editing.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
pattern = ROOT / 'problems'
files = sorted(pattern.glob('*/*_title.tex'))
if not files:
    print('No files found matching problems/*/*_title.tex')
    sys.exit(0)

count = 0
for p in files:
    try:
        text = p.read_text(encoding='utf-8')
    except Exception as e:
        print(f'Failed to read {p}: {e}')
        continue
    lines = text.splitlines(keepends=True)
    if not lines:
        # empty file, skip
        continue
    # backup
    bak = p.with_suffix(p.suffix + '.bak')
    if not bak.exists():
        bak.write_text(text, encoding='utf-8')
    # write without first line
    new_text = ''.join(lines[1:])
    p.write_text(new_text, encoding='utf-8')
    count += 1

print(f'Processed {count} files (first line removed).')
