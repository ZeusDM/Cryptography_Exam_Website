---
{
  "title": "Elliptic Curves",
  "topic": "Elliptic Curves",
  "topic_slug": "elliptic-curves",
  "abbr": "EC",
  "cluster_count": 6,
  "solved_count": 0,
  "draft_count": 0,
  "clusters": [
    {
      "id": "composite/elliptic-cubing",
      "title": "Elliptic curves",
      "canonical_id": "composite/elliptic-cubing",
      "canonical_url": "problems/composite-elliptic-cubing/",
      "appearances": [
        "2025/6",
        "2018/6",
        "2013/6",
        "2003/6"
      ],
      "appearance_links": [
        {
          "text": "2025/6",
          "url": "problems/2025-6/"
        },
        {
          "text": "2018/6",
          "url": "problems/2018-6/"
        },
        {
          "text": "2013/6",
          "url": "problems/2013-6/"
        },
        {
          "text": "2003/6",
          "url": "problems/2003-6/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(q\\)</span> be a power of an odd prime\nsatisfying <span class=\"math inline\">\\(q \\equiv 2 \\pmod{3}\\)</span>.\nConsider the elliptic curve <span class=\"math inline\">\\(E \\colon y^2 =\nx^3 + b\\)</span> defined over <span\nclass=\"math inline\">\\(\\mathbb{F}_q\\)</span> (<span\nclass=\"math inline\">\\(b \\neq 0\\)</span>).</p>\n<ol type=\"a\">\n<li><p>Prove that the mapping <span class=\"math inline\">\\(x \\mapsto\nx^3\\)</span> is a bijection on <span\nclass=\"math inline\">\\(\\mathbb{F}_q\\)</span>.</p></li>\n<li><p>Prove that the number of points in <span\nclass=\"math inline\">\\(E(\\mathbb{F}_q)\\)</span> is <span\nclass=\"math inline\">\\(q + 1\\)</span>.</p></li>\n<li><p>Prove that <span class=\"math inline\">\\(E(\\mathbb{F}_q)\\)</span>\nis cyclic.</p></li>\n<li><p>Let <span class=\"math inline\">\\(R = (x_R, y_R)\\)</span> be a\npoint in <span class=\"math inline\">\\(E(\\mathbb{F}_q)\\)</span>. Given\n<span class=\"math inline\">\\(y_R\\)</span>, explain how to compute <span\nclass=\"math inline\">\\(x_R\\)</span> efficiently.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let \\(q\\) be a power of an odd prime satisfying \\(q \\equiv 2 \\pmod{3}\\). Consider the elliptic curve \\(E \\colon y^2 = x^3 + b\\) defined over \\(\\mathbb{F}_q\\) (\\(b \\neq 0\\)).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Prove that the mapping \\(x \\mapsto x^3\\) is a bijection on \\(\\mathbb{F}_q\\).\n\n    \\item Prove that the number of points in \\(E(\\mathbb{F}_q)\\) is \\(q + 1\\).\n\n    \\item Prove that \\(E(\\mathbb{F}_q)\\) is cyclic.\n\n    \\item Let \\(R = (x_R, y_R)\\) be a point in \\(E(\\mathbb{F}_q)\\). Given \\(y_R\\), explain how to compute \\(x_R\\) efficiently.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/composite/elliptic-cubing.tex"
    },
    {
      "id": "composite/elliptic-point-counting",
      "title": "Elliptic curves",
      "canonical_id": "composite/elliptic-point-counting",
      "canonical_url": "problems/composite-elliptic-point-counting/",
      "appearances": [
        "2019/5",
        "2017/7"
      ],
      "appearance_links": [
        {
          "text": "2019/5",
          "url": "problems/2019-5/"
        },
        {
          "text": "2017/7",
          "url": "problems/2017-7/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(E \\colon y^2 = x^3 + a x + b\\)</span>\nbe an elliptic curve defined over <span\nclass=\"math inline\">\\(\\mathbb{Z}_p\\)</span>, where <span\nclass=\"math inline\">\\(p &gt; 3\\)</span> is prime.</p>\n<ol type=\"a\">\n<li><p>Prove the formula <span class=\"math display\">\\[\\#E(\\mathbb{Z}_p)\n= p + 1 + \\sum_{x=0}^{p-1} \\left( \\frac{x^3 + a x + b}{p}\n\\right),\\]</span> where the expression inside the summation is the\nLegendre symbol.</p></li>\n<li><p>Suppose that <span class=\"math inline\">\\(x^3 + a x + b\\)</span>\nsplits into three distinct linear factors modulo <span\nclass=\"math inline\">\\(p\\)</span>. Show that <span\nclass=\"math inline\">\\(E(\\mathbb{Z}_p)\\)</span> is not cyclic.</p></li>\n<li><p>If furthermore <span class=\"math inline\">\\(b = 0\\)</span> and\n<span class=\"math inline\">\\(p \\equiv 3 \\pmod{4}\\)</span>, show that\n<span class=\"math inline\">\\(\\#E(\\mathbb{Z}_p) = p + 1\\)</span>.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let \\(E \\colon y^2 = x^3 + a x + b\\) be an elliptic curve defined over \\(\\mathbb{Z}_p\\), where \\(p > 3\\) is prime.\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Prove the formula\n    \\[\n    \\#E(\\mathbb{Z}_p) = p + 1 + \\sum_{x=0}^{p-1} \\left( \\frac{x^3 + a x + b}{p} \\right),\n    \\]\n    where the expression inside the summation is the Legendre symbol.\n\n    \\item Suppose that \\(x^3 + a x + b\\) splits into three distinct linear factors modulo \\(p\\). Show that \\(E(\\mathbb{Z}_p)\\) is not cyclic.\n\n    \\item If furthermore \\(b = 0\\) and \\(p \\equiv 3 \\pmod{4}\\), show that \\(\\#E(\\mathbb{Z}_p) = p + 1\\).\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/composite/elliptic-point-counting.tex"
    },
    {
      "id": "2011/6",
      "title": "Elliptic curves",
      "canonical_id": "2011/6",
      "canonical_url": "problems/2011-6/",
      "appearances": [
        "2011/6"
      ],
      "appearance_links": [
        {
          "text": "2011/6",
          "url": "problems/2011-6/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Consider the Kobitz (Koblitz) curve defined over <span\nclass=\"math inline\">\\(\\mathbb{F}_2\\)</span>: <span\nclass=\"math display\">\\[E:\\; y^2 + x y = x^3 + x^2 + 1 .\\]</span></p>\n<ol type=\"a\">\n<li><p>Show that #<span class=\"math inline\">\\(E(\\mathbb{F}_2^r)\\)</span>\nis even for all <span class=\"math-punct\"><span class=\"math inline\">\\(r \\ge 1\\)</span>.</span></p></li>\n<li><p>Show that if <span class=\"math inline\">\\(r &gt; 4\\)</span> and\n<span class=\"math inline\">\\(\\#E(\\mathbb{F}_{2^r}) = 2p\\)</span> where\n<span class=\"math inline\">\\(p\\)</span> is a prime number, then <span\nclass=\"math inline\">\\(r\\)</span> must be prime.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Consider the Kobitz (Koblitz) curve defined over \\(\\mathbb{F}_2\\):\n\\[\nE:\\; y^2 + x y = x^3 + x^2 + 1 .\n\\]\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Show that \\#\\(E(\\mathbb{F}_2^r)\\) is even for all \\(r \\ge 1\\).\n    \\item Show that if \\(r > 4\\) and \\(\\#E(\\mathbb{F}_{2^r}) = 2p\\) where \\(p\\) is a prime number, then \\(r\\) must be prime.\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2011/6.tex"
    },
    {
      "id": "2007/5",
      "title": "Weil pairing",
      "canonical_id": "2007/5",
      "canonical_url": "problems/2007-5/",
      "appearances": [
        "2007/5"
      ],
      "appearance_links": [
        {
          "text": "2007/5",
          "url": "problems/2007-5/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(E\\)</span> be an elliptic curve over\na field, and suppose <span class=\"math inline\">\\(P,Q\\in E[n]\\)</span>\nfor some <span class=\"math inline\">\\(n&gt;0\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Give the formula for the Weil pairing <span\nclass=\"math inline\">\\(e(P,Q)\\)</span> of <span\nclass=\"math inline\">\\(P\\)</span> and <span\nclass=\"math inline\">\\(Q\\)</span>.</p></li>\n<li><p>Prove that the choice of divisors in the formula does not affect\nthe value of <span class=\"math inline\">\\(e(P,Q)\\)</span>. You may assume\nWeil reciprocity.</p></li>\n<li><p>Prove that the Weil pairing is bilinear.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let $E$ be an elliptic curve over a field, and suppose $P,Q\\in E[n]$ for some $n>0$.\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Give the formula for the Weil pairing $e(P,Q)$ of $P$ and $Q$.\n    \\item Prove that the choice of divisors in the formula does not affect the value of $e(P,Q)$. You may assume Weil reciprocity.\n    \\item Prove that the Weil pairing is bilinear.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2007/5.tex"
    },
    {
      "id": "2007/6",
      "title": "Embedding degree",
      "canonical_id": "2007/6",
      "canonical_url": "problems/2007-6/",
      "appearances": [
        "2007/6"
      ],
      "appearance_links": [
        {
          "text": "2007/6",
          "url": "problems/2007-6/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(E\\)</span> be an elliptic curve\ndefined over <span class=\"math-punct\"><span class=\"math inline\">\\(\\mathbb{F}_q\\)</span>,</span> and\ndenote by <span class=\"math inline\">\\(n\\)</span> the largest prime\nfactor of <span class=\"math-punct\"><span class=\"math inline\">\\(\\#E(\\mathbb{F}_q)\\)</span>.</span> Recall\nthat the embedding degree of <span class=\"math inline\">\\(E\\)</span> is\nby definition equal to the multiplicative order of <span\nclass=\"math inline\">\\(q\\)</span> in <span\nclass=\"math inline\">\\((\\mathbb{Z}/n\\mathbb{Z})^*\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Let <span class=\"math inline\">\\(k\\)</span> be an integer. Prove\nthat the embedding degree of <span class=\"math inline\">\\(E\\)</span>\ndivides <span class=\"math inline\">\\(k\\)</span> if and only if <span\nclass=\"math inline\">\\(n \\mid (q^k - 1)\\)</span>, where <span\nclass=\"math inline\">\\(t\\)</span> is the trace of <span\nclass=\"math inline\">\\(E\\)</span>.</p></li>\n<li><p>Suppose <span class=\"math inline\">\\(q = p^2\\)</span> and <span\nclass=\"math inline\">\\(t = p\\)</span> where <span\nclass=\"math inline\">\\(p\\)</span> is prime. Determine the embedding\ndegree of <span class=\"math-punct\"><span class=\"math inline\">\\(E\\)</span>.</span></p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let $E$ be an elliptic curve defined over $\\mathbb{F}_q$, and denote by $n$ the largest prime factor of $\\#E(\\mathbb{F}_q)$. Recall that the embedding degree of $E$ is by definition equal to the multiplicative order of $q$ in $(\\mathbb{Z}/n\\mathbb{Z})^*$.\n\n\\begin{enumerate}[label=(\\alph*)]\n\\item Let $k$ be an integer. Prove that the embedding degree of $E$ divides $k$ if and only if $n \\mid (q^k - 1)$, where $t$ is the trace of $E$.\n\n\\item Suppose $q = p^2$ and $t = p$ where $p$ is prime. Determine the embedding degree of $E$.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2007/6.tex"
    },
    {
      "id": "2004/6",
      "title": "Elliptic curves and finite fields",
      "canonical_id": "2004/6",
      "canonical_url": "problems/2004-6/",
      "appearances": [
        "2004/6"
      ],
      "appearance_links": [
        {
          "text": "2004/6",
          "url": "problems/2004-6/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Recall that the Trace function <span\nclass=\"math inline\">\\(\\mathrm{Tr} : \\mathbb{F}_{2^m} \\to\n\\mathbb{F}_2\\)</span> is defined by <span\nclass=\"math inline\">\\(\\mathrm{Tr}(\\alpha) = \\sum_{i=0}^{m-1}\n\\alpha^{2^i}\\)</span>. Prove that exactly half of the elements in <span\nclass=\"math inline\">\\(\\mathbb{F}_{2^m}\\)</span> have trace 0 (and the\nother half have trace 1).</p></li>\n<li><p>Let <span class=\"math-punct\"><span class=\"math inline\">\\(\\alpha \\in\n\\mathbb{F}_{2^m}\\)</span>.</span> Prove that the equation <span\nclass=\"math inline\">\\(x^2 + x = \\alpha\\)</span> has a solution <span\nclass=\"math inline\">\\(x \\in \\mathbb{F}_{2^m}\\)</span> if and only if\n<span class=\"math-punct\"><span class=\"math inline\">\\(\\mathrm{Tr}(\\alpha) = 0\\)</span>.</span></p></li>\n<li><p>Let <span class=\"math inline\">\\(E:\\ y^2 + y = x^3\\)</span> be an\nelliptic curve over <span\nclass=\"math inline\">\\(\\mathbb{F}_{2^m}\\)</span> where <span\nclass=\"math inline\">\\(m\\)</span> is an odd positive integer. Prove that\n<span class=\"math-punct\"><span class=\"math inline\">\\(|E(\\mathbb{F}_{2^m})| = 2^m +\n1\\)</span>.</span></p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Recall that the Trace function \\(\\mathrm{Tr} : \\mathbb{F}_{2^m} \\to \\mathbb{F}_2\\) is defined by \\(\\mathrm{Tr}(\\alpha) = \\sum_{i=0}^{m-1} \\alpha^{2^i}\\). Prove that exactly half of the elements in \\(\\mathbb{F}_{2^m}\\) have trace 0 (and the other half have trace 1).\n    \\item Let \\(\\alpha \\in \\mathbb{F}_{2^m}\\). Prove that the equation \\(x^2 + x = \\alpha\\) has a solution \\(x \\in \\mathbb{F}_{2^m}\\) if and only if \\(\\mathrm{Tr}(\\alpha) = 0\\).\n    \\item Let \\(E:\\ y^2 + y = x^3\\) be an elliptic curve over \\(\\mathbb{F}_{2^m}\\) where \\(m\\) is an odd positive integer. Prove that \\(|E(\\mathbb{F}_{2^m})| = 2^m + 1\\).\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2004/6.tex"
    }
  ]
}
---
