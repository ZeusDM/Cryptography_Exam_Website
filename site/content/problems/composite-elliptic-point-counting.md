---
{
  "title": "Elliptic curves",
  "slug": "composite-elliptic-point-counting",
  "id": "composite/elliptic-point-counting",
  "problem_id": "composite/elliptic-point-counting",
  "year": "Composite",
  "problem": 0,
  "problem_number": 0,
  "topic": "Elliptic Curves",
  "topic_slug": "elliptic-curves",
  "status": "none",
  "is_incomplete": false,
  "is_reference": false,
  "has_own_solution": false,
  "has_solution": false,
  "has_variant_solution": false,
  "variant_solutions": [],
  "is_canonical": true,
  "canonical_id": "composite/elliptic-point-counting",
  "canonical_url": "/problems/composite-elliptic-point-counting/",
  "author": "",
  "cluster_members": [
    {
      "id": "2019/5",
      "url": "/problems/2019-5/",
      "is_current": false
    },
    {
      "id": "2017/7",
      "url": "/problems/2017-7/",
      "is_current": false
    },
    {
      "id": "composite/elliptic-point-counting",
      "url": "/problems/composite-elliptic-point-counting/",
      "is_current": true
    }
  ],
  "appearances": [
    "2019/5",
    "2017/7"
  ],
  "appearance_links": [
    {
      "text": "2019/5",
      "url": "/problems/2019-5/"
    },
    {
      "text": "2017/7",
      "url": "/problems/2017-7/"
    }
  ],
  "source_file": "problems/composite/elliptic-point-counting.tex",
  "url": "/problems/composite-elliptic-point-counting/",
  "statement_html": "<p>Let <span class=\"math inline\">\\(E \\colon y^2 = x^3 + a x + b\\)</span>\nbe an elliptic curve defined over <span\nclass=\"math inline\">\\(\\mathbb{Z}_p\\)</span>, where <span\nclass=\"math inline\">\\(p &gt; 3\\)</span> is prime.</p>\n<ol type=\"a\">\n<li><p>Prove the formula <span class=\"math display\">\\[\\#E(\\mathbb{Z}_p)\n= p + 1 + \\sum_{x=0}^{p-1} \\left( \\frac{x^3 + a x + b}{p}\n\\right),\\]</span> where the expression inside the summation is the\nLegendre symbol.</p></li>\n<li><p>Suppose that <span class=\"math inline\">\\(x^3 + a x + b\\)</span>\nsplits into three distinct linear factors modulo <span\nclass=\"math inline\">\\(p\\)</span>. Show that <span\nclass=\"math inline\">\\(E(\\mathbb{Z}_p)\\)</span> is not cyclic.</p></li>\n<li><p>If furthermore <span class=\"math inline\">\\(b = 0\\)</span> and\n<span class=\"math inline\">\\(p \\equiv 3 \\pmod{4}\\)</span>, show that\n<span class=\"math inline\">\\(\\#E(\\mathbb{Z}_p) = p + 1\\)</span>.</p></li>\n</ol>",
  "solution_html": "",
  "raw_statement": "Let \\(E \\colon y^2 = x^3 + a x + b\\) be an elliptic curve defined over \\(\\mathbb{Z}_p\\), where \\(p > 3\\) is prime.\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Prove the formula\n    \\[\n    \\#E(\\mathbb{Z}_p) = p + 1 + \\sum_{x=0}^{p-1} \\left( \\frac{x^3 + a x + b}{p} \\right),\n    \\]\n    where the expression inside the summation is the Legendre symbol.\n\n    \\item Suppose that \\(x^3 + a x + b\\) splits into three distinct linear factors modulo \\(p\\). Show that \\(E(\\mathbb{Z}_p)\\) is not cyclic.\n\n    \\item If furthermore \\(b = 0\\) and \\(p \\equiv 3 \\pmod{4}\\), show that \\(\\#E(\\mathbb{Z}_p) = p + 1\\).\n\\end{enumerate}",
  "raw_solution": ""
}
---
