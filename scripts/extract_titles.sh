#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<EOF
Usage: $0 [--dry-run] [--backup] [--overwrite] [--use-ed] [--dir DIR]

For each file matching DIR/YYYY/X.tex (default DIR=problems):
  - write lines 1 and 2 to DIR/YYYY/X_title.tex
  - remove line 2 from the original file

Options:
  --dry-run    Show what would be done but don't modify files
  --backup     Create a backup copy of each modified file as FILE.bak
  --overwrite  Overwrite existing _title.tex files
  --use-ed     Use ed to delete line 2 instead of awk (optional)
  --dir DIR    Base directory (default: problems)
  -h, --help   Show this help message
EOF
}

DRY_RUN=false
BACKUP=false
OVERWRITE=false
USE_ED=false
DIR="problems"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=true; shift;;
    --backup) BACKUP=true; shift;;
    --overwrite) OVERWRITE=true; shift;;
    --use-ed) USE_ED=true; shift;;
    --dir) DIR="$2"; shift 2;;
    -h|--help) usage; exit 0;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2;;
  esac
done

if [[ ! -d "$DIR" ]]; then
  echo "Directory '$DIR' does not exist." >&2
  exit 2
fi

find "$DIR" -type f -name '*.tex' ! -name '*_title.tex' -print0 |
while IFS= read -r -d '' file; do
  # Skip if the file is already a title file
  base_noext="${file%.tex}"
  title_file="${base_noext}_title.tex"

  # Count lines (0 if empty)
  nlines=$(wc -l < "$file" 2>/dev/null || echo 0)

  if [[ -e "$title_file" && "$OVERWRITE" != true ]]; then
    echo "Skipping '$file' -> '$title_file' exists (use --overwrite to replace)"
    continue
  fi

  if [[ "$nlines" -eq 0 ]]; then
    echo "Skipping empty file: $file"
    continue
  fi

  if [[ "$DRY_RUN" == true ]]; then
    echo "Would create: $title_file  (lines 1-2 from $file)"
    if [[ "$nlines" -ge 2 ]]; then
      echo "Would remove line 2 from: $file"
    else
      echo "Would not remove line 2 from: $file  (file has <2 lines)"
    fi
    continue
  fi

  # Make optional backup
  if [[ "$BACKUP" == true ]]; then
    cp -- "$file" "$file.bak"
  fi

  # Write first two lines (or all lines if fewer than 2) to the title file
  if [[ "$nlines" -ge 2 ]]; then
    head -n 2 -- "$file" > "$title_file"
  else
    # file has 1 line
    head -n 1 -- "$file" > "$title_file"
  fi

  # Remove line 2 from the original if it exists
  if [[ "$nlines" -ge 2 ]]; then
    if [[ "$USE_ED" == true ]]; then
      # Use ed in a safe way (single-line invocation)
      printf $'2\nw\nq\n' | ed -s -- "$file"
    else
  tmpfile=$(mktemp)
  # Some awk implementations don't accept '--' as an option terminator,
  # so pass the filename directly.
  awk 'NR!=2{print}' "$file" > "$tmpfile"
      mv -- "$tmpfile" "$file"
    fi
    echo "Processed: $file -> $title_file (removed line 2)"
  else
    echo "Processed: $file -> $title_file (no line 2 to remove)"
  fi
done

echo "Done."
