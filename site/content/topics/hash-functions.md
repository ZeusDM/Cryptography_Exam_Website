---
{
  "title": "Hash Functions",
  "topic": "Hash Functions",
  "topic_slug": "hash-functions",
  "abbr": "HF",
  "cluster_count": 11,
  "solved_count": 0,
  "draft_count": 0,
  "clusters": [
    {
      "id": "2025/1",
      "title": "Hash functions",
      "canonical_id": "2025/1",
      "canonical_url": "problems/2025-1/",
      "appearances": [
        "2025/1"
      ],
      "appearance_links": [
        {
          "text": "2025/1",
          "url": "problems/2025-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(H \\colon \\{0, 1\\}^{\\le \\ell} \\to \\{0,\n1\\}^n\\)</span> be a hash function mapping binary strings of length at\nmost <span class=\"math inline\">\\(\\ell\\)</span>, for some <span\nclass=\"math inline\">\\(\\ell &gt; n\\)</span>, to binary strings of length\n<span class=\"math inline\">\\(n\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Define what it means for <span class=\"math inline\">\\(H\\)</span>\nto be collision resistant.</p></li>\n<li><p>Define what it means for <span class=\"math inline\">\\(H\\)</span>\nto be second-preimage resistant.</p></li>\n<li><p>Prove one of the following statements:</p>\n<ol type=\"i\">\n<li><p>If <span class=\"math inline\">\\(H\\)</span> is collision resistant,\nthen <span class=\"math inline\">\\(H\\)</span> is also second-preimage\nresistant.</p></li>\n<li><p>If <span class=\"math inline\">\\(H\\)</span> is second-preimage\nresistant, then <span class=\"math inline\">\\(H\\)</span> is also collision\nresistant.</p></li>\n</ol></li>\n<li><p>Define <span class=\"math inline\">\\(G \\colon \\{0, 1\\}^{\\le \\ell}\n\\to \\{0, 1\\}^n\\)</span> by <span class=\"math inline\">\\(G(x) =\nH(H(x))\\)</span>. Prove that if <span class=\"math inline\">\\(H\\)</span>\nis collision resistant then <span class=\"math inline\">\\(G\\)</span> is\nalso collision resistant.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let \\(H \\colon \\{0, 1\\}^{\\le \\ell} \\to \\{0, 1\\}^n\\) be a hash function mapping binary strings of length at most \\(\\ell\\), for some \\(\\ell > n\\), to binary strings of length \\(n\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Define what it means for \\(H\\) to be collision resistant.\n\n    \\item Define what it means for \\(H\\) to be second-preimage resistant.\n\n    \\item Prove one of the following statements:\n    \\begin{enumerate}[label=(\\roman*)]\n        \\item If \\(H\\) is collision resistant, then \\(H\\) is also second-preimage resistant.\n        \\item If \\(H\\) is second-preimage resistant, then \\(H\\) is also collision resistant.\n    \\end{enumerate}\n\n    \\item Define \\(G \\colon \\{0, 1\\}^{\\le \\ell} \\to \\{0, 1\\}^n\\) by \\(G(x) = H(H(x))\\). Prove that if \\(H\\) is collision resistant then \\(G\\) is also collision resistant.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2025/1.tex"
    },
    {
      "id": "2020/6",
      "title": "Hash functions",
      "canonical_id": "2020/6",
      "canonical_url": "problems/2020-6/",
      "appearances": [
        "2020/6"
      ],
      "appearance_links": [
        {
          "text": "2020/6",
          "url": "problems/2020-6/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(p\\)</span> be a <span\nclass=\"math inline\">\\(256\\)</span>-bit prime, and let <span\nclass=\"math inline\">\\(E\\)</span> be an elliptic curve defined over <span\nclass=\"math inline\">\\(\\mathbb{Z}_p\\)</span> with <span\nclass=\"math inline\">\\(|E(\\mathbb{Z}_p)| = n\\)</span> a prime. Let <span\nclass=\"math inline\">\\(P, Q \\in E(\\mathbb{Z}_p)\\)</span> be randomly\nselected points, neither of which is the point at infinity; these points\nare fixed and public. Define the hash function <span\nclass=\"math inline\">\\(H : [0, n-1] \\times [0, n-1] \\to\nE(\\mathbb{Z}_p)\\)</span> by <span class=\"math inline\">\\(H((a, b)) = aP +\nbQ\\)</span>. That is, messages are pairs <span class=\"math inline\">\\((a,\nb)\\)</span> of integers in the interval <span class=\"math inline\">\\([0,\nn-1]\\)</span>, and the hash of such a message is the elliptic curve\npoint <span class=\"math inline\">\\(aP + bQ\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Define what it means for <span class=\"math inline\">\\(H\\)</span>\nto be preimage resistant.</p></li>\n<li><p>Define what it means for <span class=\"math inline\">\\(H\\)</span>\nto be collision resistant.</p></li>\n<li><p>Prove, under a reasonable computational assumption (which you\nshould state), that <span class=\"math inline\">\\(H\\)</span> is collision\nresistant.</p></li>\n<li><p>Prove, under a reasonable computational assumption (which you\nshould state), that <span class=\"math inline\">\\(H\\)</span> is preimage\nresistant.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let \\(p\\) be a \\(256\\)-bit prime, and let \\(E\\) be an elliptic curve defined over \\(\\mathbb{Z}_p\\) with \\(|E(\\mathbb{Z}_p)| = n\\) a prime. Let \\(P, Q \\in E(\\mathbb{Z}_p)\\) be randomly selected points, neither of which is the point at infinity; these points are fixed and public.\nDefine the hash function \\(H : [0, n-1] \\times [0, n-1] \\to E(\\mathbb{Z}_p)\\) by \\(H((a, b)) = aP + bQ\\). That is, messages are pairs \\((a, b)\\) of integers in the interval \\([0, n-1]\\), and the hash of such a message is the elliptic curve point \\(aP + bQ\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Define what it means for \\(H\\) to be preimage resistant.\n\n    \\item Define what it means for \\(H\\) to be collision resistant.\n\n    \\item Prove, under a reasonable computational assumption (which you should state), that \\(H\\) is collision resistant.\n\n    \\item Prove, under a reasonable computational assumption (which you should state), that \\(H\\) is preimage resistant.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2020/6.tex"
    },
    {
      "id": "2019/2",
      "title": "Hash functions",
      "canonical_id": "2019/2",
      "canonical_url": "problems/2019-2/",
      "appearances": [
        "2019/2"
      ],
      "appearance_links": [
        {
          "text": "2019/2",
          "url": "problems/2019-2/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Recall that AES is a block cipher with message space <span\nclass=\"math inline\">\\(\\{0,1\\}^{128}\\)</span> and key space <span\nclass=\"math inline\">\\(\\{0,1\\}^{128}\\)</span>. Let <span\nclass=\"math inline\">\\(x\\)</span> and <span\nclass=\"math inline\">\\(y\\)</span> denote bitstrings of length 128. Which\nof the following hash functions <span\nclass=\"math inline\">\\(H_i:\\{0,1\\}^{256}\\rightarrow\\{0,1\\}^{128}\\)</span>,\nif any, are preimage resistant? No justification is needed except that a\nlack of preimage resistance must be justified.</p>\n<ol type=\"i\">\n<li><p><span class=\"math inline\">\\(H_1(x,y) = \\mathrm{AES}_x(y) \\oplus\ny.\\)</span></p></li>\n<li><p><span class=\"math inline\">\\(H_2(x,y) = \\mathrm{AES}_y(x) \\oplus\nx.\\)</span></p></li>\n<li><p><span class=\"math inline\">\\(H_3(x,y) = \\mathrm{AES}_y(x) \\oplus\ny.\\)</span></p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Recall that AES is a block cipher with message space \\(\\{0,1\\}^{128}\\) and key space \\(\\{0,1\\}^{128}\\). Let \\(x\\) and \\(y\\) denote bitstrings of length 128. Which of the following hash functions \\(H_i:\\{0,1\\}^{256}\\rightarrow\\{0,1\\}^{128}\\), if any, are preimage resistant? No justification is needed except that a lack of preimage resistance must be justified.\n\n\\begin{enumerate}[label=(\\roman*)]\n    \\item \\(H_1(x,y) = \\mathrm{AES}_x(y) \\oplus y.\\)\n\n    \\item \\(H_2(x,y) = \\mathrm{AES}_y(x) \\oplus x.\\)\n\n    \\item \\(H_3(x,y) = \\mathrm{AES}_y(x) \\oplus y.\\)\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2019/2.tex"
    },
    {
      "id": "2018/2",
      "title": "Hash functions",
      "canonical_id": "2018/2",
      "canonical_url": "problems/2018-2/",
      "appearances": [
        "2018/2"
      ],
      "appearance_links": [
        {
          "text": "2018/2",
          "url": "problems/2018-2/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(q\\)</span> be a prime, and let <span\nclass=\"math inline\">\\(G\\)</span> be a (multiplicatively written) group\nof order <span class=\"math inline\">\\(q\\)</span>. Let <span\nclass=\"math inline\">\\(g\\)</span> and <span\nclass=\"math inline\">\\(h\\)</span> be randomly selected elements from\n<span class=\"math inline\">\\(G \\setminus \\{1\\}\\)</span>. Consider the\nfunction <span class=\"math inline\">\\(H_{g,h} : \\mathbb{Z}_q \\times\n\\mathbb{Z}_q \\to G\\)</span> defined by <span\nclass=\"math inline\">\\(H_{g,h}:(x,y) \\mapsto g^x h^y\\)</span>. Henceforth\nwe will denote <span class=\"math inline\">\\(H_{g,h}\\)</span> by <span\nclass=\"math inline\">\\(H\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Show that for any <span class=\"math inline\">\\(k \\in G\\)</span>,\nthere are exactly <span class=\"math inline\">\\(q\\)</span> distinct\nsolutions <span class=\"math inline\">\\((x,y) \\in \\mathbb{Z}_q \\times\n\\mathbb{Z}_q\\)</span> to the equation <span class=\"math inline\">\\(g^x\nh^y = k\\)</span>.</p></li>\n<li><p>Prove that if the discrete logarithm problem in <span\nclass=\"math inline\">\\(G\\)</span> is intractable then <span\nclass=\"math inline\">\\(H\\)</span> is collision resistant.</p></li>\n<li><p>Is <span class=\"math inline\">\\(H\\)</span> preimage\nresistant?</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let \\(q\\) be a prime, and let \\(G\\) be a (multiplicatively written) group of order \\(q\\). Let \\(g\\) and \\(h\\) be randomly selected elements from \\(G \\setminus \\{1\\}\\). Consider the function \\(H_{g,h} : \\mathbb{Z}_q \\times \\mathbb{Z}_q \\to G\\) defined by \\(H_{g,h}:(x,y) \\mapsto g^x h^y\\). Henceforth we will denote \\(H_{g,h}\\) by \\(H\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Show that for any \\(k \\in G\\), there are exactly \\(q\\) distinct solutions \\((x,y) \\in \\mathbb{Z}_q \\times \\mathbb{Z}_q\\) to the equation \\(g^x h^y = k\\).\n    \n    \\item Prove that if the discrete logarithm problem in \\(G\\) is intractable then \\(H\\) is collision resistant.\n    \n    \\item Is \\(H\\) preimage resistant?\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2018/2.tex"
    },
    {
      "id": "2017/2",
      "title": "Hash functions",
      "canonical_id": "2017/2",
      "canonical_url": "problems/2017-2/",
      "appearances": [
        "2017/2"
      ],
      "appearance_links": [
        {
          "text": "2017/2",
          "url": "problems/2017-2/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Define what it means for a hash function to be <em>collision\nresistant</em>.</p></li>\n<li><p>Define what it means for a hash function to be <em>preimage\nresistant</em>.</p></li>\n<li><p>Define what it means for a hash function to be\n<em>second-preimage resistant</em>.</p></li>\n<li><p>Let <span class=\"math inline\">\\(G \\colon \\{0,1\\}^{2n} \\to\n\\{0,1\\}^n\\)</span> and <span class=\"math inline\">\\(H \\colon \\{0,1\\}^{2n}\n\\to \\{0,1\\}^n\\)</span> be two hash functions. Define the function <span\nclass=\"math inline\">\\(F\\colon \\{0,1\\}^{2n} \\times \\{0,1\\}^n \\to\n\\{0,1\\}^n\\)</span> by <span class=\"math inline\">\\(F(x,y) = H(G(x),\nG(x))\\)</span>. (Here, the comma \u201c<span\nclass=\"math inline\">\\(,\\)</span>\u201d denotes concatenation.) Prove that if\n<span class=\"math inline\">\\(G\\)</span> and <span\nclass=\"math inline\">\\(H\\)</span> are collision resistant, then <span\nclass=\"math inline\">\\(F\\)</span> is also collision resistant.</p></li>\n<li><p>Suppose that <span class=\"math inline\">\\(f \\colon \\{0,1\\}^{n+r}\n\\to \\{0,1\\}^n\\)</span> is a preimage resistant function. Define the\nfunction <span class=\"math inline\">\\(H\\colon \\{0,1\\}^{2(n+r)} \\to\n\\{0,1\\}^n\\)</span> as follows. Given <span class=\"math inline\">\\(x \\in\n\\{0,1\\}^{2(n+r)}\\)</span>, write <span class=\"math inline\">\\(x = x_L\n\\,\\|\\, x_R\\)</span> where <span class=\"math inline\">\\(x_L, x_R \\in\n\\{0,1\\}^{n+r}\\)</span>. (Here, <span class=\"math inline\">\\(\\|\\)</span>\ndenotes concatenation.) Then define <span class=\"math display\">\\[H(x) =\nf\\big(x_L \\oplus x_R\\big).\\]</span> Prove that <span\nclass=\"math inline\">\\(H\\)</span> is not second-preimage\nresistant.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Define what it means for a hash function to be \\emph{collision resistant}.\n\n    \\item Define what it means for a hash function to be \\emph{preimage resistant}.\n\n    \\item Define what it means for a hash function to be \\emph{second-preimage resistant}.\n\n    \\item Let \\(G \\colon \\{0,1\\}^{2n} \\to \\{0,1\\}^n\\) and \\(H \\colon \\{0,1\\}^{2n} \\to \\{0,1\\}^n\\) be two hash functions.\n    Define the function \\( F\\colon \\{0,1\\}^{2n} \\times \\{0,1\\}^n \\to \\{0,1\\}^n \\) by \\( F(x,y) = H(G(x), G(x)) \\).\n    (Here, the comma ``\\(,\\)'' denotes concatenation.)\n    Prove that if \\(G\\) and \\(H\\) are collision resistant, then \\(F\\) is also collision resistant.\n\n    \\item Suppose that \\(f \\colon \\{0,1\\}^{n+r} \\to \\{0,1\\}^n\\) is a preimage resistant function.\n    Define the function \\( H\\colon \\{0,1\\}^{2(n+r)} \\to \\{0,1\\}^n \\) as follows.\n    Given \\(x \\in \\{0,1\\}^{2(n+r)}\\), write \\(x = x_L \\,\\|\\, x_R\\) where \\(x_L, x_R \\in \\{0,1\\}^{n+r}\\). (Here, \\(\\|\\) denotes concatenation.) Then define\n    \\[\n    H(x) = f\\big(x_L \\oplus x_R\\big).\n    \\]\n    Prove that \\(H\\) is not second-preimage resistant.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2017/2.tex"
    },
    {
      "id": "2016/1",
      "title": "Hash functions",
      "canonical_id": "2016/1",
      "canonical_url": "problems/2016-1/",
      "appearances": [
        "2016/1"
      ],
      "appearance_links": [
        {
          "text": "2016/1",
          "url": "problems/2016-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>In the triangle of the three properties of a hash function:</p>\n<ul>\n<li><p>collision resistant</p></li>\n<li><p>preimage resistant</p></li>\n<li><p>second-preimage resistant</p></li>\n</ul>\n<p>enter six symbols <span class=\"math inline\">\\(\\in \\{\\Rightarrow,\n\\Leftrightarrow\\}\\)</span> to indicate which property implies the other\nand which does not. Prove three out of the six directions.</p>",
      "solution_html": "",
      "raw_statement": "In the triangle of the three properties of a hash function:\n\\begin{itemize}\n  \\item collision resistant\n  \\item preimage resistant\n  \\item second-preimage resistant\n\\end{itemize}\nenter six symbols \\(\\in \\{\\Rightarrow, \\Leftrightarrow\\}\\) to indicate which property implies the other and which does not.\nProve three out of the six directions.",
      "raw_solution": "",
      "source_file": "problems/2016/1.tex"
    },
    {
      "id": "2013/1",
      "title": "Hash functions",
      "canonical_id": "2013/1",
      "canonical_url": "problems/2013-1/",
      "appearances": [
        "2013/1"
      ],
      "appearance_links": [
        {
          "text": "2013/1",
          "url": "problems/2013-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Define what it means for a hash function to be preimage\nresistant.</p></li>\n<li><p>Let <span class=\"math inline\">\\(E\\)</span> be a block cipher with\n80-bit keys and an 80-bit block size. Fix a publicly known 80-bit\ninitialization vector <span class=\"math inline\">\\(\\text{IV}\\)</span>.\nDefine a hash function <span class=\"math inline\">\\(H : \\{0,1\\}^{160}\n\\rightarrow \\{0,1\\}^{80}\\)</span> as follows: <span\nclass=\"math display\">\\[H(m) =\nE_{m_2}\\bigl(E_{m_1}(\\text{IV})\\bigr),\\]</span> where <span\nclass=\"math inline\">\\(m_1\\)</span> (respectively, <span\nclass=\"math inline\">\\(m_2\\)</span>) represents the first (respectively,\nlast) 80 bits of <span class=\"math inline\">\\(m\\)</span>. Give (and\nanalyze) an algorithm to find preimages for <span\nclass=\"math inline\">\\(H\\)</span>. Your algorithm should use no more than\n<span class=\"math inline\">\\(\\approx 2^{40}\\)</span> invocations of <span\nclass=\"math inline\">\\(E\\)</span>.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Define what it means for a hash function to be preimage resistant.\n\n    \\item Let $E$ be a block cipher with 80-bit keys and an 80-bit block size. Fix a publicly known 80-bit initialization vector $\\text{IV}$. Define a hash function $H : \\{0,1\\}^{160} \\rightarrow \\{0,1\\}^{80}$ as follows:\n    \\[\n    H(m) = E_{m_2}\\bigl(E_{m_1}(\\text{IV})\\bigr),\n    \\]\n    where $m_1$ (respectively, $m_2$) represents the first (respectively, last) 80 bits of $m$. Give (and analyze) an algorithm to find preimages for $H$. Your algorithm should use no more than $\\approx 2^{40}$ invocations of $E$.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2013/1.tex"
    },
    {
      "id": "2011/1",
      "title": "Hash functions",
      "canonical_id": "2011/1",
      "canonical_url": "problems/2011-1/",
      "appearances": [
        "2011/1"
      ],
      "appearance_links": [
        {
          "text": "2011/1",
          "url": "problems/2011-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Give an example of a hash function <span\nclass=\"math inline\">\\(H:\\{0,1\\}^{*} \\to \\{0,1\\}^{*}\\)</span> that is\ncollision resistant but not preimage resistant. Justify your\nchoice!</p></li>\n<li><p>Define what it means for a pair of permutations <span\nclass=\"math inline\">\\(f_0,f_1\\)</span> on <span\nclass=\"math inline\">\\(S\\)</span> to be claw-free.</p></li>\n<li><p>Let <span class=\"math-punct\"><span class=\"math inline\">\\(p,q \\equiv 3 \\pmod{4}\\)</span>,</span>\nand let <span class=\"math-punct\"><span class=\"math inline\">\\(n = pq\\)</span>.</span> Let <span\nclass=\"math inline\">\\(S\\)</span> denote the set of squares modulo <span\nclass=\"math inline\">\\(n\\)</span>, coprime with <span\nclass=\"math inline\">\\(n\\)</span>. Let <span\nclass=\"math inline\">\\(a_0,a_1 \\in S\\)</span>, and define the functions\n<span class=\"math inline\">\\(f_0:S \\to S\\)</span> and <span\nclass=\"math inline\">\\(f_1:S \\to S\\)</span> by <span\nclass=\"math display\">\\[f_0(x) = a_0 x^2 \\pmod{n}, \\qquad f_1(x) = a_1\nx^2 \\pmod{n}.\\]</span> Then <span class=\"math inline\">\\(f_0\\)</span> and\n<span class=\"math inline\">\\(f_1\\)</span> are permutations on <span\nclass=\"math inline\">\\(S\\)</span> (you do not need to show this). Show\nthat under the assumption that factoring <span\nclass=\"math inline\">\\(n\\)</span> is computationally infeasible, <span\nclass=\"math inline\">\\(f_0\\)</span> and <span\nclass=\"math inline\">\\(f_1\\)</span> is a claw-free pair of\npermutations.</p></li>\n<li><p>Using <span class=\"math inline\">\\(f_0\\)</span> and <span\nclass=\"math inline\">\\(f_1\\)</span>, construct a collision-free hash\nfunction <span class=\"math display\">\\[H:\\{0,1\\}^{*} \\to S\n.\\]</span></p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Give an example of a hash function \\(H:\\{0,1\\}^{*} \\to \\{0,1\\}^{*}\\) that is collision resistant but not preimage resistant. Justify your choice!\n    \\item Define what it means for a pair of permutations \\(f_0,f_1\\) on \\(S\\) to be claw-free.\n    \\item Let \\(p,q \\equiv 3 \\pmod{4}\\), and let \\(n = pq\\). Let \\(S\\) denote the set of squares modulo \\(n\\), coprime with \\(n\\). Let \\(a_0,a_1 \\in S\\), and define the functions \\(f_0:S \\to S\\) and \\(f_1:S \\to S\\) by\n\\[\nf_0(x) = a_0 x^2 \\pmod{n}, \\qquad f_1(x) = a_1 x^2 \\pmod{n}.\n\\]\nThen \\(f_0\\) and \\(f_1\\) are permutations on \\(S\\) (you do not need to show this). Show that under the assumption that factoring \\(n\\) is computationally infeasible, \\(f_0\\) and \\(f_1\\) is a claw-free pair of permutations.\n    \\item Using \\(f_0\\) and \\(f_1\\), construct a collision-free hash function\n\\[\nH:\\{0,1\\}^{*} \\to S .\n\\]\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2011/1.tex"
    },
    {
      "id": "2007/1",
      "title": "Hash functions",
      "canonical_id": "2007/1",
      "canonical_url": "problems/2007-1/",
      "appearances": [
        "2007/1"
      ],
      "appearance_links": [
        {
          "text": "2007/1",
          "url": "problems/2007-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Is a collision-resistant hash function necessarily preimage\nresistant?</p></li>\n<li><p>Let <span class=\"math inline\">\\((n,e)\\)</span> be an RSA public\nkey, where <span class=\"math inline\">\\(n\\)</span> is 2048 bits in\nlength. The corresponding RSA private key is not known to anyone. Define\na hash function <span class=\"math inline\">\\(H : \\{0,1\\}^* \\to\n[0,n-1]\\)</span> as follows: <span class=\"math-punct\"><span class=\"math inline\">\\(H(m) = m^e\n\\bmod n\\)</span>,</span> where <span class=\"math inline\">\\(m\\)</span> denotes\nthe integer whose binary representation is <span\nclass=\"math inline\">\\(m\\)</span>. Is <span\nclass=\"math inline\">\\(H\\)</span> collision resistant? (Justify your\nanswer.)</p></li>\n<li><p>Let <span class=\"math inline\">\\(IV \\in \\{0,1\\}^n\\)</span> be a\nfixed initialization vector, and let <span class=\"math inline\">\\(f\n\\colon \\{0,1\\}^{n+r} \\to \\{0,1\\}^n\\)</span> be a compression function.\nDefine the hash function <span class=\"math inline\">\\(H\\)</span> as\nfollows: to hash a message <span class=\"math inline\">\\(x\\)</span> of\nbitlength <span class=\"math-punct\"><span class=\"math inline\">\\(b &lt; 2^r\\)</span>,</span> the message\nis first divided into <span class=\"math inline\">\\(r\\)</span>-bit blocks:\n<span class=\"math inline\">\\(\\bar{x} = x_1, x_2, \\ldots, x_t\\)</span>\n(where the last block is padded with 0 bits if necessary). Define <span\nclass=\"math inline\">\\(x_{t+1}\\)</span> to be the <span\nclass=\"math inline\">\\(r\\)</span>-bit binary representation of <span\nclass=\"math inline\">\\(b\\)</span>. Then <span class=\"math inline\">\\(H_0 =\n\\text{IV}\\)</span> and <span class=\"math inline\">\\(H_i = f(H_{i-1},\nx_i)\\)</span> for <span class=\"math-punct\"><span class=\"math inline\">\\(i = 1, 2, \\ldots,\nt\\)</span>.</span> Then <span class=\"math inline\">\\(H(x)\\)</span> is defined to\nbe <span class=\"math-punct\"><span class=\"math inline\">\\(H_{t+1}\\)</span>.</span> Prove that if <span\nclass=\"math inline\">\\(f\\)</span> is collision resistant, then <span\nclass=\"math inline\">\\(H\\)</span> is also collision resistant.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Is a collision-resistant hash function necessarily preimage resistant?\n    \n    \\item Let $(n,e)$ be an RSA public key, where $n$ is 2048 bits in length. The corresponding RSA private key is not known to anyone. Define a hash function $H : \\{0,1\\}^* \\to [0,n-1]$ as follows: $H(m) = m^e \\bmod n$, where $m$ denotes the integer whose binary representation is $m$. Is $H$ collision resistant? (Justify your answer.)\n    \n    \\item Let $IV \\in \\{0,1\\}^n$ be a fixed initialization vector, and let $f \\colon \\{0,1\\}^{n+r} \\to \\{0,1\\}^n$ be a compression function. Define the hash function $H$ as follows: to hash a message $x$ of bitlength $b < 2^r$, the message is first divided into $r$-bit blocks: $\\bar{x} = x_1, x_2, \\ldots, x_t$ (where the last block is padded with 0 bits if necessary). Define $x_{t+1}$ to be the $r$-bit binary representation of $b$. Then $H_0 = \\text{IV}$ and $H_i = f(H_{i-1}, x_i)$ for $i = 1, 2, \\ldots, t$. Then $H(x)$ is defined to be $H_{t+1}$. Prove that if $f$ is collision resistant, then $H$ is also collision resistant.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2007/1.tex"
    },
    {
      "id": "2004/1",
      "title": "Hash functions",
      "canonical_id": "2004/1",
      "canonical_url": "problems/2004-1/",
      "appearances": [
        "2004/1"
      ],
      "appearance_links": [
        {
          "text": "2004/1",
          "url": "problems/2004-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Define what it means for a hash function to be collision\nresistant.</p></li>\n<li><p>Define what it means for a hash function to be second preimage\nresistant.</p></li>\n<li><p>Let E denote the family of encryption functions for the AES block\ncipher where plaintext blocks, ciphertext blocks, and keys are each 128\nbits in length. Define a hash function <span\nclass=\"math inline\">\\(H:\\{0,1\\}^{128}\\to\\{0,1\\}^{128}\\)</span> by <span\nclass=\"math inline\">\\(H(x,y)=E_x(y)\\)</span>. Here, x and y are 128-bit\nblocks, and <span class=\"math inline\">\\(E_x(y)\\)</span> denotes the\nencryption of the plaintext block y using the key x. Is <span\nclass=\"math inline\">\\(H\\)</span> collision resistant? (Justify your\nanswer.)</p></li>\n<li><p>Is the hash function in (c) second preimage resistant? (Justify\nyour answer.)</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Define what it means for a hash function to be collision resistant.\n    \\item Define what it means for a hash function to be second preimage resistant.\n    \\item Let E denote the family of encryption functions for the AES block cipher where plaintext blocks, ciphertext blocks, and keys are each 128 bits in length. Define a hash function \\(H:\\{0,1\\}^{128}\\to\\{0,1\\}^{128}\\) by \\(H(x,y)=E_x(y)\\). Here, x and y are 128-bit blocks, and \\(E_x(y)\\) denotes the encryption of the plaintext block y using the key x. Is \\(H\\) collision resistant? (Justify your answer.)\n    \\item Is the hash function in (c) second preimage resistant? (Justify your answer.)\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2004/1.tex"
    },
    {
      "id": "2002/2",
      "title": "Hash functions",
      "canonical_id": "2002/2",
      "canonical_url": "problems/2002-2/",
      "appearances": [
        "2002/2"
      ],
      "appearance_links": [
        {
          "text": "2002/2",
          "url": "problems/2002-2/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Suppose <span class=\"math inline\">\\(h_1 \\colon \\{0,1\\}^{2m} \\to\n\\{0,1\\}^{m}\\)</span> is a collision resistant hash function.</p>\n<ol type=\"a\">\n<li><p>Define <span class=\"math inline\">\\(h_2 \\colon \\{0,1\\}^{4m} \\to\n\\{0,1\\}^{m}\\)</span> as follows:</p>\n<ol type=\"i\">\n<li><p>Write <span class=\"math inline\">\\(x \\in \\{0,1\\}^{4m}\\)</span> as\n<span class=\"math inline\">\\(x = x_1 \\parallel x_2\\)</span>, where <span\nclass=\"math inline\">\\(x_1, x_2 \\in \\{0,1\\}^{2m}\\)</span>.</p></li>\n<li><p>Define <span class=\"math inline\">\\(h_2(x) = h_1(x_1) \\parallel\nh_1(x_2)\\)</span>.</p></li>\n</ol>\n<p>Prove that <span class=\"math inline\">\\(h_2\\)</span> is collision\nresistant.</p></li>\n<li><p>For an integer <span class=\"math inline\">\\(i \\geq 2\\)</span>,\ndefine a hash function <span class=\"math inline\">\\(h_i \\colon\n\\{0,1\\}^{2^i m} \\to \\{0,1\\}^{m}\\)</span> recursively from <span\nclass=\"math inline\">\\(h_{i-1}\\)</span> as follows:</p>\n<ol type=\"i\">\n<li><p>Write <span class=\"math inline\">\\(x \\in \\{0,1\\}^{2^i m}\\)</span>\nas <span class=\"math inline\">\\(x = x_1 \\parallel x_2\\)</span>, where\n<span class=\"math inline\">\\(x_1, x_2 \\in \\{0,1\\}^{2^{i-1}\nm}\\)</span>.</p></li>\n<li><p>Define <span class=\"math inline\">\\(h_i(x) = h_{i-1}(x_1)\n\\parallel h_{i-1}(x_2)\\)</span>.</p></li>\n</ol>\n<p>Prove that <span class=\"math inline\">\\(h_i\\)</span> is collision\nresistant.</p></li>\n<li><p>Let <span class=\"math inline\">\\(\\gamma\\)</span> be a quadratic\nresidue modulo <span class=\"math inline\">\\(p\\)</span>. Show that the two\nsquare roots of <span class=\"math inline\">\\(\\gamma\\)</span> modulo <span\nclass=\"math inline\">\\(p\\)</span> are <span class=\"math inline\">\\(\\pm\n\\gamma^{(p+1)/4}\\)</span>.</p></li>\n<li><p>Show that <span class=\"math inline\">\\(L_1(\\beta)\\)</span> can be\nefficiently computed given <span class=\"math inline\">\\(p, \\alpha,\n\\beta\\)</span>. Here, <span class=\"math inline\">\\(L_1(\\beta)\\)</span>\ndenotes the least significant bit of the discrete logarithm <span\nclass=\"math inline\">\\(a\\)</span> of <span class=\"math inline\">\\(\\beta =\n\\alpha^a \\pmod{p}\\)</span> (i.e., <span class=\"math inline\">\\(L_1(\\beta)\n= 0\\)</span> if <span class=\"math inline\">\\(a\\)</span> is even, and\n<span class=\"math inline\">\\(L_1(\\beta) = 1\\)</span> if <span\nclass=\"math inline\">\\(a\\)</span> is odd). Let <span\nclass=\"math inline\">\\(L_2(\\beta)\\)</span> denote the second least\nsignificant bit of <span class=\"math inline\">\\(a\\)</span>. That is,\n<span class=\"math inline\">\\(L_2(\\beta) = 0\\)</span> if <span\nclass=\"math inline\">\\(a \\equiv 0\\)</span> or <span\nclass=\"math inline\">\\(1 \\pmod{4}\\)</span>, and <span\nclass=\"math inline\">\\(L_2(\\beta) = 1\\)</span> if <span\nclass=\"math inline\">\\(a \\equiv 2\\)</span> or <span\nclass=\"math inline\">\\(3 \\pmod{4}\\)</span>.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Suppose \\(h_1 \\colon \\{0,1\\}^{2m} \\to \\{0,1\\}^{m}\\) is a collision resistant hash function.\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Define \\(h_2 \\colon \\{0,1\\}^{4m} \\to \\{0,1\\}^{m}\\) as follows:\n    \\begin{enumerate}[label=(\\roman*)]\n        \\item Write \\(x \\in \\{0,1\\}^{4m}\\) as \\(x = x_1 \\parallel x_2\\), where \\(x_1, x_2 \\in \\{0,1\\}^{2m}\\).\n        \\item Define \\(h_2(x) = h_1(x_1) \\parallel h_1(x_2)\\).\n    \\end{enumerate}\n    Prove that \\(h_2\\) is collision resistant.\n    \n    \\item For an integer \\(i \\geq 2\\), define a hash function \\(h_i \\colon \\{0,1\\}^{2^i m} \\to \\{0,1\\}^{m}\\) recursively from \\(h_{i-1}\\) as follows:\n    \\begin{enumerate}[label=(\\roman*)]\n        \\item Write \\(x \\in \\{0,1\\}^{2^i m}\\) as \\(x = x_1 \\parallel x_2\\), where \\(x_1, x_2 \\in \\{0,1\\}^{2^{i-1} m}\\).\n        \\item Define \\(h_i(x) = h_{i-1}(x_1) \\parallel h_{i-1}(x_2)\\).\n    \\end{enumerate}\n    Prove that \\(h_i\\) is collision resistant.\n    \n    \\item Let \\(\\gamma\\) be a quadratic residue modulo \\(p\\). Show that the two square roots of \\(\\gamma\\) modulo \\(p\\) are \\(\\pm \\gamma^{(p+1)/4}\\).\n    \n    \\item Show that \\(L_1(\\beta)\\) can be efficiently computed given \\(p, \\alpha, \\beta\\). Here, \\(L_1(\\beta)\\) denotes the least significant bit of the discrete logarithm \\(a\\) of \\(\\beta = \\alpha^a \\pmod{p}\\) (i.e., \\(L_1(\\beta) = 0\\) if \\(a\\) is even, and \\(L_1(\\beta) = 1\\) if \\(a\\) is odd). Let \\(L_2(\\beta)\\) denote the second least significant bit of \\(a\\). That is, \\(L_2(\\beta) = 0\\) if \\(a \\equiv 0\\) or \\(1 \\pmod{4}\\), and \\(L_2(\\beta) = 1\\) if \\(a \\equiv 2\\) or \\(3 \\pmod{4}\\).\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2002/2.tex"
    }
  ]
}
---
