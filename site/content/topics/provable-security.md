---
{
  "title": "Provable Security",
  "topic": "Provable Security",
  "topic_slug": "provable-security",
  "abbr": "PS",
  "cluster_count": 5,
  "solved_count": 0,
  "draft_count": 0,
  "clusters": [
    {
      "id": "2020/1",
      "title": "Shannon's theory",
      "canonical_id": "2020/1",
      "canonical_url": "problems/2020-1/",
      "appearances": [
        "2020/1"
      ],
      "appearance_links": [
        {
          "text": "2020/1",
          "url": "problems/2020-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Define what it means for a symmetric-key encryption scheme to\nhave perfect secrecy.</p></li>\n<li><p>Suppose that a symmetric-key encryption scheme with encryption\nfunction <span class=\"math inline\">\\(E \\colon \\mathcal{K} \\times\n\\mathcal{M} \\to \\mathcal{C}\\)</span> satisfies <span\nclass=\"math inline\">\\(|\\mathcal{K}| = |\\mathcal{C}| =\n|\\mathcal{M}|\\)</span>. Prove that, if the encryption scheme has perfect\nsecrecy, then every key is used with equal probability <span\nclass=\"math inline\">\\(1/|\\mathcal{K}|\\)</span>, and for every message\n<span class=\"math inline\">\\(x \\in \\mathcal{M}\\)</span> and ciphertext\n<span class=\"math inline\">\\(y \\in \\mathcal{C}\\)</span>, there is a\nunique key <span class=\"math inline\">\\(k\\)</span> such that <span\nclass=\"math inline\">\\(E(k, x) = y\\)</span>.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Define what it means for a symmetric-key encryption scheme to have perfect secrecy.\n\n    \\item Suppose that a symmetric-key encryption scheme with encryption function \\(E \\colon \\mathcal{K} \\times \\mathcal{M} \\to \\mathcal{C}\\) satisfies \\(|\\mathcal{K}| = |\\mathcal{C}| = |\\mathcal{M}|\\). Prove that, if the encryption scheme has perfect secrecy, then every key is used with equal probability \\(1/|\\mathcal{K}|\\), and for every message \\(x \\in \\mathcal{M}\\) and ciphertext \\(y \\in \\mathcal{C}\\), there is a unique key \\(k\\) such that \\(E(k, x) = y\\).\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2020/1.tex"
    },
    {
      "id": "2019/6",
      "title": "Provable security",
      "canonical_id": "2019/6",
      "canonical_url": "problems/2019-6/",
      "appearances": [
        "2019/6"
      ],
      "appearance_links": [
        {
          "text": "2019/6",
          "url": "problems/2019-6/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>The Boneh\u2013Franklin cryptosystem is defined as follows.</p>\n<dl>\n<dt>Public parameters:</dt>\n<dd>\n<p>A cryptographic pairing <span class=\"math inline\">\\(e: G \\times G\n\\rightarrow GT\\)</span>, and two elements <span\nclass=\"math inline\">\\(g,h \\in G\\)</span>, each of which generates the\ncyclic group <span class=\"math inline\">\\(G\\)</span>.</p>\n</dd>\n<dt>Key generation:</dt>\n<dd>\n<p>Choose <span class=\"math inline\">\\(\\alpha \\in \\mathbb{Z}\\)</span>.\nThe public key is <span class=\"math inline\">\\(g^\\alpha\\)</span>. The\nprivate key is <span class=\"math inline\">\\(h^\\alpha\\)</span>.</p>\n</dd>\n<dt>Encryption:</dt>\n<dd>\n<p>Given <span class=\"math inline\">\\(m \\in \\{0,1\\}^k\\)</span>, the\nencryption of <span class=\"math inline\">\\(m\\)</span> is <span\nclass=\"math inline\">\\((g^r, e(g^\\alpha, h^r) \\oplus m)\\)</span> for\nrandom <span class=\"math inline\">\\(r \\in \\mathbb{Z}\\)</span>. Here <span\nclass=\"math inline\">\\(k\\)</span> is the number of bits used to represent\nan element of <span class=\"math inline\">\\(GT\\)</span>.</p>\n</dd>\n<dt>Decryption:</dt>\n<dd>\n<p>Given a ciphertext <span class=\"math inline\">\\((c_1,c_2)\\)</span>,\nthe plaintext is <span class=\"math inline\">\\(c_2 \\oplus e(c_1,\nh^\\alpha)\\)</span>.</p>\n</dd>\n</dl>\n<ol type=\"a\">\n<li><p>Show that the Boneh\u2013Franklin scheme is <strong>OW-CPA</strong>\nunder the Bilinear Diffie\u2013Hellman (BDH) assumption: Given <span\nclass=\"math inline\">\\(g, g^\\alpha, g^\\beta\\)</span>, and <span\nclass=\"math inline\">\\(h\\)</span>, it is infeasible to compute <span\nclass=\"math inline\">\\(e(g^\\alpha, h^\\beta)\\)</span> from the\nciphertext.</p></li>\n<li><p>Show that the Boneh\u2013Franklin scheme is <strong>IND-CPA</strong>\nunder the Decisional Bilinear Diffie\u2013Hellman (DBDH) assumption.</p></li>\n</ol>\n<div class=\"center\">\n<table>\n<thead>\n<tr>\n<th style=\"text-align: left;\"><span\nclass=\"math inline\">\\(\\text{OW-CPA}_{\\text{Enc}}^{\\mathcal{A}}\\)</span></th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(1\\colon \\quad\n(\\mathsf{pk, sk}) \\leftarrow_{\\$}\n\\mathsf{KGen}(1^{\\lambda})\\)</span></td>\n</tr>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(2\\colon \\quad\nm \\leftarrow_{\\$} M\\)</span></td>\n</tr>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(3\\colon \\quad\nc \\leftarrow_{\\$} \\mathsf{Enc}(\\mathsf{pk}, m)\\)</span></td>\n</tr>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(4\\colon \\quad\nm&#39; \\leftarrow_{\\$} \\mathcal{A}(1^{\\lambda}, \\mathsf{pk},\nc)\\)</span></td>\n</tr>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(5\\colon \\quad\n\\mathbf{return} \\ m \\stackrel{?}{=} m&#39;\\)</span></td>\n</tr>\n</tbody>\n</table>\n<table>\n<thead>\n<tr>\n<th style=\"text-align: left;\"><span\nclass=\"math inline\">\\(\\text{IND-CPA}_{\\text{Enc}}^{\\mathcal{A}}\\)</span></th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(1\\colon \\quad\n(\\mathsf{pk, sk}) \\leftarrow_{\\$}\n\\mathsf{KGen}(1^{\\lambda})\\)</span></td>\n</tr>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(2\\colon \\quad\nb \\leftarrow_{\\$} \\{0, 1\\}\\)</span></td>\n</tr>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(3\\colon \\quad\n(m_0, m_1) \\leftarrow_{\\$} \\mathcal{A}(1^{\\lambda},\n\\mathsf{pk})\\)</span></td>\n</tr>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(4\\colon \\quad\nc \\leftarrow_{\\$} \\mathsf{Enc}(\\mathsf{pk}, m_b)\\)</span></td>\n</tr>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(5\\colon \\quad\nb&#39; \\leftarrow_{\\$} \\mathcal{A}(1^{\\lambda}, \\mathsf{pk},\nc)\\)</span></td>\n</tr>\n<tr>\n<td style=\"text-align: left;\"><span class=\"math inline\">\\(6\\colon \\quad\n\\mathbf{return} \\ b \\stackrel{?}{=} b&#39;\\)</span></td>\n</tr>\n</tbody>\n</table>\n<p>Figure: OW-CPA and IND-CPA definitions.</p>\n</div>",
      "solution_html": "",
      "raw_statement": "The Boneh\u2013Franklin cryptosystem is defined as follows.\n\n\\begin{description}\n    \\item[Public parameters:] A cryptographic pairing \\(e: G \\times G \\rightarrow GT\\), and two elements \\(g,h \\in G\\), each of which generates the cyclic group \\(G\\).\n\n    \\item[Key generation:] Choose \\(\\alpha \\in \\mathbb{Z}\\). The public key is \\(g^\\alpha\\). The private key is \\(h^\\alpha\\).\n\n    \\item[Encryption:] Given \\(m \\in \\{0,1\\}^k\\), the encryption of \\(m\\) is \\((g^r, e(g^\\alpha, h^r) \\oplus m)\\) for random \\(r \\in \\mathbb{Z}\\). Here \\(k\\) is the number of bits used to represent an element of \\(GT\\).\n\n    \\item[Decryption:] Given a ciphertext \\((c_1,c_2)\\), the plaintext is \\(c_2 \\oplus e(c_1, h^\\alpha)\\). \n\\end{description}\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Show that the Boneh\u2013Franklin scheme is \\textbf{OW-CPA} under the Bilinear Diffie\u2013Hellman (BDH) assumption: Given \\(g, g^\\alpha, g^\\beta\\), and \\(h\\), it is infeasible to compute \\(e(g^\\alpha, h^\\beta)\\) from the ciphertext.\n\n    \\item Show that the Boneh\u2013Franklin scheme is \\textbf{IND-CPA} under the Decisional Bilinear Diffie\u2013Hellman (DBDH) assumption.\n\\end{enumerate}\n\n\\begin{center}\n% OW-CPA Game\n\\begin{tabular}[t]{l}\n    \\toprule\n    $\\text{OW-CPA}_{\\text{Enc}}^{\\mathcal{A}}$ \\\\\n    \\midrule\n    $1\\colon \\quad (\\mathsf{pk, sk}) \\leftarrow_{\\$} \\mathsf{KGen}(1^{\\lambda})$ \\\\\n    $2\\colon \\quad m \\leftarrow_{\\$} M$ \\\\\n    $3\\colon \\quad c \\leftarrow_{\\$} \\mathsf{Enc}(\\mathsf{pk}, m)$ \\\\\n    $4\\colon \\quad m' \\leftarrow_{\\$} \\mathcal{A}(1^{\\lambda}, \\mathsf{pk}, c)$ \\\\\n    $5\\colon \\quad \\mathbf{return} \\ m \\stackrel{?}{=} m'$ \\\\\n    \\bottomrule\n\\end{tabular}\n\\quad\n% IND-CPA Game\n\\begin{tabular}[t]{l}\n    \\toprule\n    $\\text{IND-CPA}_{\\text{Enc}}^{\\mathcal{A}}$ \\\\\n    \\midrule\n    $1\\colon \\quad (\\mathsf{pk, sk}) \\leftarrow_{\\$} \\mathsf{KGen}(1^{\\lambda})$ \\\\\n    $2\\colon \\quad b \\leftarrow_{\\$} \\{0, 1\\}$ \\\\\n    $3\\colon \\quad (m_0, m_1) \\leftarrow_{\\$} \\mathcal{A}(1^{\\lambda}, \\mathsf{pk})$ \\\\\n    $4\\colon \\quad c \\leftarrow_{\\$} \\mathsf{Enc}(\\mathsf{pk}, m_b)$ \\\\\n    $5\\colon \\quad b' \\leftarrow_{\\$} \\mathcal{A}(1^{\\lambda}, \\mathsf{pk}, c)$ \\\\\n    $6\\colon \\quad \\mathbf{return} \\ b \\stackrel{?}{=} b'$ \\\\\n    \\bottomrule\n\\end{tabular}\n\nFigure: OW-CPA and IND-CPA definitions.\n\\end{center}",
      "raw_solution": "",
      "source_file": "problems/2019/6.tex"
    },
    {
      "id": "2016/8",
      "title": "Provable security",
      "canonical_id": "2016/8",
      "canonical_url": "problems/2016-8/",
      "appearances": [
        "2016/8"
      ],
      "appearance_links": [
        {
          "text": "2016/8",
          "url": "problems/2016-8/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Consider the Zheng-Sebberry public-key encryption scheme (1993):</p>\n<p>Public parameters: A cyclic group <span\nclass=\"math inline\">\\(G\\)</span>, a generator <span\nclass=\"math inline\">\\(g\\)</span> of <span\nclass=\"math inline\">\\(G\\)</span>, and two random oracles <span\nclass=\"math display\">\\[H_1: \\{0,1\\}^t \\rightarrow \\{0,1\\}^n,\\qquad\nH_2: G \\rightarrow \\{0,1\\}^{t+n}.\\]</span></p>\n<p>Key generation: Choose a private key <span class=\"math inline\">\\(x\n\\in \\mathbb{Z}\\)</span>. The corresponding public key is <span\nclass=\"math inline\">\\(h = g^x\\)</span>.</p>\n<p>Encryption: To encrypt <span class=\"math inline\">\\(m \\in\n\\{0,1\\}^t\\)</span>, choose <span class=\"math inline\">\\(y \\in\n\\mathbb{Z}\\)</span> and compute <span class=\"math display\">\\[Y =\ng^y,\\qquad\nc = H_2(h^y) \\oplus (m \\,\\|\\, H_1(m)).\\]</span> The ciphertext is <span\nclass=\"math inline\">\\((Y, c)\\)</span>.</p>\n<p>Decryption: Compute <span class=\"math inline\">\\(c \\oplus\nH_2(Y^x)\\)</span>. If the leftmost <span\nclass=\"math inline\">\\(t\\)</span> bits of the result map to the rightmost\n<span class=\"math inline\">\\(n\\)</span> bits under <span\nclass=\"math inline\">\\(H_1\\)</span>, then output the leftmost <span\nclass=\"math inline\">\\(t\\)</span> bits; otherwise output NULL.</p>\n<p>Show that the Zheng-Sebberry scheme is not IND-CCA2. (IND-CCA2 means\n\u201cindistinguishable against adaptive chosen-ciphertext attack\u201d. In this\nattack, the adversary selects two plaintexts <span\nclass=\"math inline\">\\(m_0, m_1\\)</span>, is then given the encryption\n<span class=\"math inline\">\\(c\\)</span> of <span\nclass=\"math inline\">\\(m_b\\)</span> (where <span class=\"math inline\">\\(b\n\\in \\{0,1\\}\\)</span>), and has to determine <span\nclass=\"math inline\">\\(b\\)</span> with probability significantly greater\nthan <span class=\"math inline\">\\(1/2\\)</span>. The adversary is also\ngiven access to a decryption oracle to which it can present any\nciphertext for decryption except for the challenge ciphertext <span\nclass=\"math inline\">\\(c\\)</span> itself.)</p>",
      "solution_html": "",
      "raw_statement": "Consider the Zheng-Sebberry public-key encryption scheme (1993):\n\nPublic parameters: A cyclic group \\(G\\), a generator \\(g\\) of \\(G\\), and two random oracles\n\\[\nH_1: \\{0,1\\}^t \\rightarrow \\{0,1\\}^n,\\qquad\nH_2: G \\rightarrow \\{0,1\\}^{t+n}.\n\\]\n\nKey generation: Choose a private key \\(x \\in \\mathbb{Z}\\). The corresponding public key is \\(h = g^x\\).\n\nEncryption: To encrypt \\(m \\in \\{0,1\\}^t\\), choose \\(y \\in \\mathbb{Z}\\) and compute\n\\[\nY = g^y,\\qquad\nc = H_2(h^y) \\oplus (m \\,\\|\\, H_1(m)).\n\\]\nThe ciphertext is \\((Y, c)\\).\n\nDecryption: Compute \\(c \\oplus H_2(Y^x)\\). If the leftmost \\(t\\) bits of the result map to the rightmost \\(n\\) bits under \\(H_1\\), then output the leftmost \\(t\\) bits; otherwise output NULL.\n\nShow that the Zheng-Sebberry scheme is not IND-CCA2.\n(IND-CCA2 means \u201cindistinguishable against adaptive chosen-ciphertext attack\u201d. In this attack, the adversary selects two plaintexts \\(m_0, m_1\\), is then given the encryption \\(c\\) of \\(m_b\\) (where \\(b \\in \\{0,1\\}\\)), and has to determine \\(b\\) with probability significantly greater than \\(1/2\\). The adversary is also given access to a decryption oracle to which it can present any ciphertext for decryption except for the challenge ciphertext \\(c\\) itself.)",
      "raw_solution": "",
      "source_file": "problems/2016/8.tex"
    },
    {
      "id": "2013/4",
      "title": "Provable security",
      "canonical_id": "2013/4",
      "canonical_url": "problems/2013-4/",
      "appearances": [
        "2013/4"
      ],
      "appearance_links": [
        {
          "text": "2013/4",
          "url": "problems/2013-4/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(p\\)</span> be a large prime, and let\n<span class=\"math inline\">\\(q\\)</span> be a large prime divisor of <span\nclass=\"math inline\">\\(p-1\\)</span>. Let <span\nclass=\"math inline\">\\(q\\)</span> be an element of order <span\nclass=\"math inline\">\\(q\\)</span> in <span\nclass=\"math inline\">\\(\\mathbb{Z}_p^*\\)</span>, and let <span\nclass=\"math inline\">\\(G\\)</span> denote the subgroup of <span\nclass=\"math inline\">\\(\\mathbb{Z}_p^*\\)</span> generated by <span\nclass=\"math inline\">\\(g\\)</span>. We consider the ElGamal encryption\nscheme in the group <span class=\"math-punct\"><span class=\"math inline\">\\(G\\)</span>,</span> which is\ndefined as follows:</p>\n<p>Setup: Public parameters <span class=\"math inline\">\\(p, q, g\\)</span>\nare chosen.</p>\n<p>Key generation: Choose <span class=\"math inline\">\\(x \\in\n\\mathbb{Z}_q^*\\)</span> at random. The public key is <span\nclass=\"math inline\">\\(g^x\\)</span> and the private key is <span\nclass=\"math inline\">\\(x\\)</span>.</p>\n<p>Encryption: The message <span class=\"math inline\">\\(m \\in G\\)</span>\nand a public key <span class=\"math-punct\"><span class=\"math inline\">\\(g^x\\)</span>,</span> choose a\nrandom integer <span class=\"math inline\">\\(r\\)</span> and output the\nciphertext <span class=\"math-punct\"><span class=\"math inline\">\\(c = (g^x, m g^{xr})\\)</span>.</span></p>\n<p>Decryption: Given a ciphertext <span class=\"math-punct\"><span class=\"math inline\">\\(c = (\\rho,\n\\sigma)\\)</span>,</span> output <span class=\"math-punct\"><span class=\"math inline\">\\(m = \\sigma /\n\\rho^x\\)</span>.</span></p>\n<ol type=\"a\">\n<li><p>It is conjectured that the Decision Diffie-Hellman (DDH)\nassumption holds in the group <span class=\"math-punct\"><span class=\"math inline\">\\(G\\)</span>.</span>\nAssuming this conjecture, prove that the ElGamal encryption scheme is\nIND-CPA secure. (Recall that IND-CPA means \u201cindistinguishable against\nchosen-plaintext attacks\u201d.)</p></li>\n<li><p>Suppose that, in the encryption function defined above, the\nmessage space is taken to be <span\nclass=\"math inline\">\\(\\mathbb{Z}_p^*\\)</span> instead of <span\nclass=\"math inline\">\\(G\\)</span>. Show that the resulting encryption\nscheme is not IND-CPA secure.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let \\(p\\) be a large prime, and let \\(q\\) be a large prime divisor of \\(p-1\\). Let \\(q\\) be an element of order \\(q\\) in \\(\\mathbb{Z}_p^*\\), and let \\(G\\) denote the subgroup of \\(\\mathbb{Z}_p^*\\) generated by \\(g\\). We consider the ElGamal encryption scheme in the group \\(G\\), which is defined as follows:\n\nSetup: Public parameters \\(p, q, g\\) are chosen.\n\nKey generation: Choose \\(x \\in \\mathbb{Z}_q^*\\) at random. The public key is \\(g^x\\) and the private key is \\(x\\).\n\nEncryption: The message \\(m \\in G\\) and a public key \\(g^x\\), choose a random integer \\(r\\) and output the ciphertext \\(c = (g^x, m g^{xr})\\).\n\nDecryption: Given a ciphertext \\(c = (\\rho, \\sigma)\\), output \\(m = \\sigma / \\rho^x\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item It is conjectured that the Decision Diffie-Hellman (DDH) assumption holds in the group \\(G\\). Assuming this conjecture, prove that the ElGamal encryption scheme is IND-CPA secure. (Recall that IND-CPA means \u201cindistinguishable against chosen-plaintext attacks\u201d.)\n    \\item Suppose that, in the encryption function defined above, the message space is taken to be \\(\\mathbb{Z}_p^*\\) instead of \\(G\\). Show that the resulting encryption scheme is not IND-CPA secure.\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2013/4.tex"
    },
    {
      "id": "2011/4",
      "title": "Provable security",
      "canonical_id": "2011/4",
      "canonical_url": "problems/2011-4/",
      "appearances": [
        "2011/4"
      ],
      "appearance_links": [
        {
          "text": "2011/4",
          "url": "problems/2011-4/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>The Blum-Goldwasser public key cryptosystem is given as follows.</p>\n<p>- Key generation: Choose distinct primes <span\nclass=\"math inline\">\\(p\\)</span> and <span\nclass=\"math inline\">\\(q\\)</span> congruent to <span\nclass=\"math inline\">\\(3 \\pmod{4}\\)</span>. The public key is <span\nclass=\"math inline\">\\(n = pq\\)</span> and the private key is <span\nclass=\"math inline\">\\((p,q)\\)</span>. - Encryption: A message <span\nclass=\"math inline\">\\(m\\)</span> consists of a single bit. To encrypt\n<span class=\"math inline\">\\(m\\)</span>, choose a random <span\nclass=\"math inline\">\\(x \\in (\\mathbb{Z}/n\\mathbb{Z})^{\\times 2}\\)</span>\n(the quadratic residues modulo <span class=\"math inline\">\\(n\\)</span>)\nand compute <span class=\"math display\">\\[i)\\ b = \\text{LSB}(x), \\quad\n  ii)\\ c = b \\oplus m, \\quad\n  iii)\\ y = x^2 \\pmod{n}.\\]</span> The ciphertext is <span\nclass=\"math inline\">\\((c,y)\\)</span>.</p>\n<p>Prove that the cryptosystem is IND-CPA. State any necessary\nassumptions.</p>",
      "solution_html": "",
      "raw_statement": "The Blum-Goldwasser public key cryptosystem is given as follows.\n\n- Key generation: Choose distinct primes \\(p\\) and \\(q\\) congruent to \\(3 \\pmod{4}\\). The public key is \\(n = pq\\) and the private key is \\((p,q)\\).\n- Encryption: A message \\(m\\) consists of a single bit. To encrypt \\(m\\), choose a random \\(x \\in (\\mathbb{Z}/n\\mathbb{Z})^{\\times 2}\\) (the quadratic residues modulo \\(n\\)) and compute\n  \\[\n  i)\\ b = \\text{LSB}(x), \\quad\n  ii)\\ c = b \\oplus m, \\quad\n  iii)\\ y = x^2 \\pmod{n}.\n  \\]\n  The ciphertext is \\((c,y)\\).\n\nProve that the cryptosystem is IND-CPA. State any necessary assumptions.",
      "raw_solution": "",
      "source_file": "problems/2011/4.tex"
    }
  ]
}
---
