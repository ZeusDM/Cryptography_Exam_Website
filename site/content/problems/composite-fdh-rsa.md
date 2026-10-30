---
{
  "title": "RSA signatures",
  "slug": "composite-fdh-rsa",
  "id": "composite/fdh-rsa",
  "problem_id": "composite/fdh-rsa",
  "year": "Composite",
  "problem": 0,
  "problem_number": 0,
  "topic": "Digital Signatures",
  "topic_slug": "digital-signatures",
  "status": "none",
  "is_incomplete": false,
  "is_reference": false,
  "has_own_solution": false,
  "has_solution": false,
  "has_variant_solution": false,
  "variant_solutions": [],
  "is_canonical": true,
  "canonical_id": "composite/fdh-rsa",
  "canonical_url": "/problems/composite-fdh-rsa/",
  "author": "",
  "cluster_members": [
    {
      "id": "2025/4",
      "url": "/problems/2025-4/",
      "is_current": false
    },
    {
      "id": "2017/5",
      "url": "/problems/2017-5/",
      "is_current": false
    },
    {
      "id": "2004/5",
      "url": "/problems/2004-5/",
      "is_current": false
    },
    {
      "id": "composite/fdh-rsa",
      "url": "/problems/composite-fdh-rsa/",
      "is_current": true
    }
  ],
  "appearances": [
    "2025/4",
    "2017/5",
    "2004/5"
  ],
  "appearance_links": [
    {
      "text": "2025/4",
      "url": "/problems/2025-4/"
    },
    {
      "text": "2017/5",
      "url": "/problems/2017-5/"
    },
    {
      "text": "2004/5",
      "url": "/problems/2004-5/"
    }
  ],
  "source_file": "problems/composite/fdh-rsa.tex",
  "url": "/problems/composite-fdh-rsa/",
  "statement_html": "<p>Recall that in the Full-Domain Hash (FDH) RSA signature scheme, an\nentity (Alice) with public key <span class=\"math inline\">\\((n,\ne)\\)</span> and private key <span class=\"math inline\">\\(d\\)</span>\ngenerates a signature <span class=\"math inline\">\\(s\\)</span> on a\nmessage <span class=\"math inline\">\\(m\\)</span> by computing <span\nclass=\"math display\">\\[s \\equiv H(m)^d \\pmod{n}.\\]</span> Here <span\nclass=\"math inline\">\\(H \\colon \\{0, 1\\}^* \\to \\{0, 1, \\dots, n -\n1\\}\\)</span> is a hash function.</p>\n<ol type=\"a\">\n<li><p>Describe how someone can verify Alice\u2019s signature <span\nclass=\"math inline\">\\(s\\)</span> on a message <span\nclass=\"math inline\">\\(m\\)</span>.</p></li>\n<li><p>Show that FDH RSA is insecure against passive adversaries if\n<span class=\"math inline\">\\(H\\)</span> is not preimage\nresistant.</p></li>\n<li><p>Prove that if finding <span class=\"math inline\">\\(e\\)</span>-th\nroots modulo <span class=\"math inline\">\\(n\\)</span> is intractable, and\nif <span class=\"math inline\">\\(H\\)</span> is a random function, then FDH\nRSA is secure (i.e., existentially unforgeable by an adversary who can\nmount an adaptive chosen-message attack).</p></li>\n</ol>",
  "solution_html": "",
  "raw_statement": "Recall that in the Full-Domain Hash (FDH) RSA signature scheme, an entity (Alice) with public key \\((n, e)\\) and private key \\(d\\) generates a signature \\(s\\) on a message \\(m\\) by computing\n\\[\ns \\equiv H(m)^d \\pmod{n}.\n\\]\nHere \\(H \\colon \\{0, 1\\}^* \\to \\{0, 1, \\dots, n - 1\\}\\) is a hash function.\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Describe how someone can verify Alice's signature \\(s\\) on a message \\(m\\).\n\n    \\item Show that FDH RSA is insecure against passive adversaries if \\(H\\) is not preimage resistant.\n\n    \\item Prove that if finding \\(e\\)-th roots modulo \\(n\\) is intractable, and if \\(H\\) is a random function, then FDH RSA is secure (i.e., existentially unforgeable by an adversary who can mount an adaptive chosen-message attack).\n\\end{enumerate}",
  "raw_solution": ""
}
---
