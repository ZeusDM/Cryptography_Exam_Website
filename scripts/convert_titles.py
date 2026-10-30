#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"problems/*/*_title.tex")

# helper to decide if a token (without surrounding punctuation) is an all-caps acronym
def is_acronym(word):
    # consider acronyms that have at least 2 chars and are all uppercase letters or digits (allowing hyphens)
    return bool(re.fullmatch(r"[A-Z0-9\-]{2,}", word))

# Known special-casing for common cryptography/proper nouns that lose their intended
# capitalization when naively lowercased. Keyed by lowercase form without surrounding
# punctuation so we can match against tokens after normalization.
EXCEPTIONS = {
    'diffie-hellman': 'Diffie-Hellman',
    'elgamal': 'ElGamal',
    'triple-des': 'Triple-DES',
    'rsa': 'RSA',
    'dsa': 'DSA',
    'des': 'DES',
    'aes': 'AES',
    'md5': 'MD5',
    'sha-1': 'SHA-1',
    'sha-256': 'SHA-256',
}

# convert a full title to sentence case preserving acronyms and LaTeX commands
def sentence_case(title):
    if not title:
        return title
    # preserve leading/trailing whitespace
    leading = re.match(r"^\s*", title).group(0)
    trailing = re.search(r"\s*$", title).group(0)
    core = title.strip()

    # If content is surrounded by code fences (```), remove them
    if core.startswith("```") and core.endswith("```"):
        core = core.strip('`').strip()

    # Tokenize by whitespace but keep punctuation attached so we can restore
    tokens = re.split(r"(\s+)", core)
    new_tokens = []
    for t in tokens:
        if t.isspace():
            new_tokens.append(t)
            continue
        # If token looks like a LaTeX command, keep as-is
        if t.startswith('\\'):
            new_tokens.append(t)
            continue
        # Split leading/trailing punctuation
        m = re.match(r"(^[^\w\\]*)([\w0-9\-']+)([^\w\\]*)$", t)
        if not m:
            # fallback: lower-case
            new_tokens.append(t.lower())
            continue
        pre, coreword, post = m.groups()
        # Handle hyphenated subwords more intelligently (e.g., Triple-DES,
        # Diffie-Hellman). We'll split on hyphens, apply rules per part,
        # then rejoin.
        parts = coreword.split('-')
        new_parts = []
        for i, part in enumerate(parts):
            # If original part is an acronym (all uppercase), preserve it
            if is_acronym(part):
                new_parts.append(part)
                continue
            # If lowercased part matches our exceptions map (either whole token or subpart), use it
            key_whole = coreword.lower()
            key_part = part.lower()
            if key_whole in EXCEPTIONS:
                # whole hyphenated token has a special casing (e.g. triple-des)
                new_parts = EXCEPTIONS[key_whole].split('-')
                break
            if key_part in EXCEPTIONS:
                new_parts.append(EXCEPTIONS[key_part])
                continue
            # If the original part contained any uppercase letter, keep its original form
            if any(ch.isupper() for ch in part):
                new_parts.append(part)
                continue
            # Otherwise lowercase the subpart for now (we'll capitalize the first word of the
            # overall title later)
            new_parts.append(part.lower())

        new_core = '-'.join(new_parts)
        new = pre + new_core + post
        new_tokens.append(new)

    rebuilt = ''.join(new_tokens)
    # Capitalize first alphabetic character of the whole rebuilt string (sentence case)
    def cap_first(s):
        for i, ch in enumerate(s):
            if ch.isalpha():
                return s[:i] + ch.upper() + s[i+1:]
        return s
    rebuilt = cap_first(rebuilt)
    return leading + rebuilt + trailing


def process_file(path: Path):
    text = path.read_text(encoding='utf-8')
    # Some files contain fences like ```tex on first line; preserve those fences but change inner text
    lines = text.splitlines()
    if len(lines) == 0:
        return False
    # Detect code fence block of the form ```... title ... ``` as in existing files
    if lines[0].startswith('```') and lines[-1].startswith('```'):
        inner = '\n'.join(lines[1:-1]).strip('\n')
        new_inner = sentence_case(inner)
        if new_inner.strip() == inner.strip():
            return False
        new_text = lines[0] + '\n' + new_inner + '\n' + lines[-1] + '\n'
        path.write_text(new_text, encoding='utf-8')
        return True
    else:
        # otherwise treat entire file as title text
        new = sentence_case(text)
        if new == text:
            return False
        path.write_text(new, encoding='utf-8')
        return True


def main():
    changed = []
    for p in ROOT.glob('problems/*/*_title.tex'):
        if process_file(p):
            changed.append(str(p))
    print(f"Processed {len(list(ROOT.glob('problems/*/*_title.tex')))} files, changed {len(changed)} files")
    for c in changed[:20]:
        print(c)

if __name__ == '__main__':
    main()
