#!/usr/bin/env python3
"""
Scan `problems/*/*_title.tex` and create `*_topic.tex` files containing the topic name
according to the `crypto_curriculum` mapping.

Usage: from repository root run `python3 scripts/assign_topics.py`
"""
import os
from pathlib import Path

crypto_curriculum = {
    "Mathematical Foundations & Number Theory": [
        "Elementary number theory",
        "Integer factorization",
        "Carmichael numbers",
        "Primality testing",
        "Number-theoretic algorithms"
    ],
    "Symmetric-Key Cryptography": [
        "Block ciphers",
        "Symmetric-key encryption",
        "Attempts to strengthen DES against exhaustive key search attacks",
        "Chosen-plaintext attack on two-key Triple-DES",
        "Pseudo-random bit generators"
    ],
    "Hash Functions and Data Integrity": [
        "Hash functions",
        "Message authentication codes",
        "Authenticated encryption"
    ],
    "RSA Cryptosystem": [
        "RSA",
        "Cryptanalysis of RSA",
        "Partial key-exposure in RSA",
        "Speeding up RSA decryption"
    ],
    "Discrete Logarithm and Key Agreement": [
        "Discrete logarithm problem",
        "Bit security of the discrete logarithm problem",
        "Security of the basic ElGamal public-key encryption scheme",
        "Diffie-Hellman problem",
        "Discrete algorithm and Diffie-Hellman problems",
        "Discrete logarithm and Diffie-Hellman problems"
    ],
    "Elliptic Curve Cryptography": [
        "Elliptic curves",
        "Elliptic curves and finite fields",
        "Embedding degree",
        "Weil pairing"
    ],
    "Digital Signatures and Identification": [
        "Signature schemes",
        "RSA signatures",
        "ECDSA",
        "Hash functions and DSA",
        "Fault analysis attack on the RSA signature scheme",
        "Duplicate signatures",
        "Identification schemes"
    ],
    "Provable Security and Theory": [
        "Provable security",
        "Shannon's theory"
    ]
}

# Build reverse lookups
title_to_topic = {}
lower_to_topic = {}
for topic, titles in crypto_curriculum.items():
    for t in titles:
        title_to_topic[t] = topic
        lower_to_topic[t.lower()] = topic


def normalize_title(s: str) -> str:
    """Return a cleaned first meaningful line from the file content."""
    if s is None:
        return ""
    lines = [ln.strip() for ln in s.splitlines()]
    # take first non-empty, non-comment line
    for ln in lines:
        if not ln:
            continue
        if ln.lstrip().startswith('%'):
            continue
        # strip surrounding braces if present
        ln2 = ln
        if ln2.startswith('{') and ln2.endswith('}'):
            ln2 = ln2[1:-1].strip()
        return ln2
    return ""


def main():
    repo_root = Path(__file__).resolve().parents[1]
    problems_dir = repo_root / 'problems'
    if not problems_dir.exists():
        print(f"Problems directory not found at {problems_dir}")
        return 1

    processed = 0
    assigned = 0
    unknown = 0
    created = 0

    for year_dir in sorted(problems_dir.iterdir()):
        if not year_dir.is_dir():
            continue
        for title_path in sorted(year_dir.glob('*_title.tex')):
            processed += 1
            raw = title_path.read_text(encoding='utf-8')
            title = normalize_title(raw)
            topic = None
            # exact match first
            if title in title_to_topic:
                topic = title_to_topic[title]
            else:
                # try lowercased match
                tl = title.lower()
                if tl in lower_to_topic:
                    topic = lower_to_topic[tl]

            topic_fname = title_path.with_name(title_path.name.replace('_title.tex', '_topic.tex'))

            if topic is None:
                unknown += 1
                content = "UNKNOWN\n"
            else:
                assigned += 1
                content = f"{topic}\n"

            # write (overwrite if exists)
            topic_path = topic_fname
            topic_path.write_text(content, encoding='utf-8')
            created += 1

    print(f"Processed {processed} title files")
    print(f"Assigned topics: {assigned}")
    print(f"Unknown titles: {unknown}")
    print(f"Created/Overwritten topic files: {created}")
    print("Done. Review `*_topic.tex` files under `problems/` for correctness.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
