---
{
  "title": "Symmetric-Key Cryptography",
  "topic": "Symmetric-Key Cryptography",
  "topic_slug": "symmetric-key-cryptography",
  "abbr": "SKC",
  "cluster_count": 10,
  "solved_count": 0,
  "draft_count": 0,
  "clusters": [
    {
      "id": "2025/2",
      "title": "MAC schemes",
      "canonical_id": "2025/2",
      "canonical_url": "/problems/2025-2/",
      "appearances": [
        "2025/2"
      ],
      "appearance_links": [
        {
          "text": "2025/2",
          "url": "/problems/2025-2/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Let <span class=\"math inline\">\\(E\\)</span> denote the family of\nencryption functions for a block cipher where plaintext blocks,\nciphertext blocks, and keys are each 128 bits in length. Let <span\nclass=\"math inline\">\\(H \\colon \\{0, 1\\}^* \\to \\{0, 1\\}^{128}\\)</span> be\na hash function. Define a MAC scheme <span\nclass=\"math inline\">\\(\\mathrm{MAC}_k \\colon \\{0, 1\\}^{3072} \\to \\{0,\n1\\}^{128}\\)</span> by <span class=\"math inline\">\\(\\mathrm{MAC}_k(m) =\nE_k(H(m))\\)</span>. Here, <span class=\"math inline\">\\(k\\)</span> is a\n128-bit secret key. Is this MAC scheme secure? (Explain)</p></li>\n<li><p>Consider the following MAC scheme for authenticating fixed-length\nmessages from <span class=\"math inline\">\\(\\{0, 1\\}^{256}\\)</span>. For\neach <span class=\"math inline\">\\(i\\)</span>, <span\nclass=\"math inline\">\\(1 \\le i \\le 128\\)</span>, let <span\nclass=\"math inline\">\\(S_i\\)</span> be a fixed subset of <span\nclass=\"math inline\">\\(\\{1, 2, 3, \\dots, 255, 256\\}\\)</span>. The key\nspace is <span class=\"math inline\">\\(\\{0, 1\\}^{128}\\)</span>. To\nauthenticate a message <span class=\"math inline\">\\(m\\)</span> with key\n<span class=\"math inline\">\\(k\\)</span>, one first forms the 128-bit\nstring <span class=\"math inline\">\\(b = b_1 b_2 \\cdots b_{128}\\)</span>\nwhere <span class=\"math inline\">\\(b_i\\)</span> is the sum modulo 2 of\nthe bits of <span class=\"math inline\">\\(m\\)</span> indexed by the\nelements of <span class=\"math inline\">\\(S_i\\)</span>, and then\nAES-encrypts <span class=\"math inline\">\\(b\\)</span> with key <span\nclass=\"math inline\">\\(k\\)</span>. The resulting ciphertext <span\nclass=\"math inline\">\\(c\\)</span> is the tag on <span\nclass=\"math inline\">\\(m\\)</span>.</p>\n<p>Show how a passive adversary who is given a single valid message/tag\npair can easily produce new valid message/tag pairs.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Let \\(E\\) denote the family of encryption functions for a block cipher where plaintext blocks, ciphertext blocks, and keys are each 128 bits in length. Let \\(H \\colon \\{0, 1\\}^* \\to \\{0, 1\\}^{128}\\) be a hash function. Define a MAC scheme \\(\\mathrm{MAC}_k \\colon \\{0, 1\\}^{3072} \\to \\{0, 1\\}^{128}\\) by \\(\\mathrm{MAC}_k(m) = E_k(H(m))\\). Here, \\(k\\) is a 128-bit secret key. Is this MAC scheme secure? (Explain)\n\n    \\item Consider the following MAC scheme for authenticating fixed-length messages from \\(\\{0, 1\\}^{256}\\). For each \\(i\\), \\(1 \\le i \\le 128\\), let \\(S_i\\) be a fixed subset of \\(\\{1, 2, 3, \\dots, 255, 256\\}\\). The key space is \\(\\{0, 1\\}^{128}\\). To authenticate a message \\(m\\) with key \\(k\\), one first forms the 128-bit string \\(b = b_1 b_2 \\cdots b_{128}\\) where \\(b_i\\) is the sum modulo 2 of the bits of \\(m\\) indexed by the elements of \\(S_i\\), and then AES-encrypts \\(b\\) with key \\(k\\). The resulting ciphertext \\(c\\) is the tag on \\(m\\).\n\n    Show how a passive adversary who is given a single valid message/tag pair can easily produce new valid message/tag pairs.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2025/2.tex"
    },
    {
      "id": "2020/2",
      "title": "Authenticated encryption",
      "canonical_id": "2020/2",
      "canonical_url": "/problems/2020-2/",
      "appearances": [
        "2020/2"
      ],
      "appearance_links": [
        {
          "text": "2020/2",
          "url": "/problems/2020-2/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(E \\colon \\mathcal{K} \\times\n\\mathcal{M} \\to \\mathcal{C}\\)</span> and <span class=\"math inline\">\\(D\n\\colon \\mathcal{K} \\times \\mathcal{C} \\to \\mathcal{M}\\)</span> be the\nencryption and decryption functions for a symmetric-key encryption\nscheme, and let <span class=\"math inline\">\\(\\mathrm{MAC} \\colon\n\\mathcal{K} \\times \\mathcal{M} \\to \\mathcal{T}\\)</span> be a message\nauthentication code. Consider the following two candidate constructions\nfor an authenticated encryption scheme, which aims to simultaneously\nprovide confidentiality and integrity:</p>\n<ol type=\"i\">\n<li><p>Split <span class=\"math inline\">\\(k\\)</span> into two keys <span\nclass=\"math inline\">\\(k_1, k_2\\)</span>. Compute <span\nclass=\"math inline\">\\(c \\leftarrow E(k_1, m)\\)</span> and <span\nclass=\"math inline\">\\(t \\leftarrow \\mathrm{MAC}(k_2, c)\\)</span>. Return\n<span class=\"math inline\">\\((c, t)\\)</span>.</p></li>\n<li><p>Split <span class=\"math inline\">\\(k\\)</span> into two keys <span\nclass=\"math inline\">\\(k_1, k_2\\)</span>. Compute <span\nclass=\"math inline\">\\(c \\leftarrow E(k_1, m)\\)</span> and <span\nclass=\"math inline\">\\(t \\leftarrow \\mathrm{MAC}(k_2, m)\\)</span>. Return\n<span class=\"math inline\">\\((c, t)\\)</span>.</p></li>\n</ol>\n<p>Assume that <span class=\"math inline\">\\((E, D)\\)</span> constitute a\nsecure encryption scheme, and <span\nclass=\"math inline\">\\(\\mathrm{MAC}\\)</span> is a secure message\nauthentication code. For each of (i) and (ii), is the candidate\nconstruction guaranteed to provide both confidentiality and integrity?\nIf not, give a counterexample. If so, give an argument to that\neffect.</p>",
      "solution_html": "",
      "raw_statement": "Let \\(E \\colon \\mathcal{K} \\times \\mathcal{M} \\to \\mathcal{C}\\) and \\(D \\colon \\mathcal{K} \\times \\mathcal{C} \\to \\mathcal{M}\\) be the encryption and decryption functions for a symmetric-key encryption scheme, and let \\(\\mathrm{MAC} \\colon \\mathcal{K} \\times \\mathcal{M} \\to \\mathcal{T}\\) be a message authentication code. Consider the following two candidate constructions for an authenticated encryption scheme, which aims to simultaneously provide confidentiality and integrity:\n\n\\begin{enumerate}[label=(\\roman*)]\n    \\item Split \\(k\\) into two keys \\(k_1, k_2\\). Compute \\(c \\leftarrow E(k_1, m)\\) and \\(t \\leftarrow \\mathrm{MAC}(k_2, c)\\). Return \\((c, t)\\).\n\n    \\item Split \\(k\\) into two keys \\(k_1, k_2\\). Compute \\(c \\leftarrow E(k_1, m)\\) and \\(t \\leftarrow \\mathrm{MAC}(k_2, m)\\). Return \\((c, t)\\).\n\\end{enumerate}\n\nAssume that \\((E, D)\\) constitute a secure encryption scheme, and \\(\\mathrm{MAC}\\) is a secure message authentication code.\nFor each of (i) and (ii), is the candidate construction guaranteed to provide both confidentiality and integrity?\nIf not, give a counterexample.\nIf so, give an argument to that effect.",
      "raw_solution": "",
      "source_file": "problems/2020/2.tex"
    },
    {
      "id": "composite/key-whitening",
      "title": "Key whitening and DES-X",
      "canonical_id": "composite/key-whitening",
      "canonical_url": "/problems/composite-key-whitening/",
      "appearances": [
        "2019/3",
        "2017/1"
      ],
      "appearance_links": [
        {
          "text": "2019/3",
          "url": "/problems/2019-3/"
        },
        {
          "text": "2017/1",
          "url": "/problems/2017-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>The original DES block cipher is limited to a 56-bit key and 64-bit\nplaintext/ciphertext blocks. The DES-X block cipher, proposed by Ron\nRivest, uses a 184-bit key <span class=\"math inline\">\\((k, k_1,\nk_2)\\)</span> where <span class=\"math inline\">\\(k \\in\n\\{0,1\\}^{56}\\)</span> and <span class=\"math inline\">\\(k_1, k_2 \\in\n\\{0,1\\}^{64}\\)</span>. The encryption of a plaintext <span\nclass=\"math inline\">\\(m \\in \\{0,1\\}^{64}\\)</span> is given by <span\nclass=\"math display\">\\[E(m) = \\mathrm{DES}_{k}(m \\oplus k_1) \\oplus\nk_2,\\]</span> where <span\nclass=\"math inline\">\\(\\mathrm{DES}_{k}(m)\\)</span> denotes the\nDES-encryption of a 64-bit plaintext block <span\nclass=\"math inline\">\\(m\\)</span> with 56-bit secret key <span\nclass=\"math inline\">\\(k\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Describe the decryption procedure.</p></li>\n<li><p>Suppose that the XOR with <span\nclass=\"math inline\">\\(k_1\\)</span> is omitted, i.e., <span\nclass=\"math display\">\\[E(m) = \\mathrm{DES}_{k}(m) \\oplus k_2,\\]</span>\nwhere the key <span class=\"math inline\">\\((k, k_2)\\)</span> is now 120\nbits. Describe an attack that recovers the secret key using roughly\n<span class=\"math inline\">\\(2^{56}\\)</span> DES operations.</p></li>\n<li><p>Suppose that the XOR with <span\nclass=\"math inline\">\\(k_2\\)</span> is omitted, i.e., <span\nclass=\"math display\">\\[E(m) = \\mathrm{DES}_{k}(m \\oplus k_1),\\]</span>\nwhere the key <span class=\"math inline\">\\((k, k_1)\\)</span> is now 120\nbits. Describe an attack that recovers the secret key using roughly\n<span class=\"math inline\">\\(2^{56}\\)</span> DES operations.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "The original DES block cipher is limited to a 56-bit key and 64-bit plaintext/ciphertext blocks. The DES-X block cipher, proposed by Ron Rivest, uses a 184-bit key \\((k, k_1, k_2)\\) where \\(k \\in \\{0,1\\}^{56}\\) and \\(k_1, k_2 \\in \\{0,1\\}^{64}\\). The encryption of a plaintext \\(m \\in \\{0,1\\}^{64}\\) is given by\n\\[\nE(m) = \\mathrm{DES}_{k}(m \\oplus k_1) \\oplus k_2,\n\\]\nwhere \\(\\mathrm{DES}_{k}(m)\\) denotes the DES-encryption of a 64-bit plaintext block \\(m\\) with 56-bit secret key \\(k\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Describe the decryption procedure.\n\n    \\item Suppose that the XOR with \\(k_1\\) is omitted, i.e.,\n    \\[\n    E(m) = \\mathrm{DES}_{k}(m) \\oplus k_2,\n    \\]\n    where the key \\((k, k_2)\\) is now 120 bits. Describe an attack that recovers the secret key using roughly \\(2^{56}\\) DES operations.\n\n    \\item Suppose that the XOR with \\(k_2\\) is omitted, i.e.,\n    \\[\n    E(m) = \\mathrm{DES}_{k}(m \\oplus k_1),\n    \\]\n    where the key \\((k, k_1)\\) is now 120 bits. Describe an attack that recovers the secret key using roughly \\(2^{56}\\) DES operations.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/composite/key-whitening.tex"
    },
    {
      "id": "2018/1",
      "title": "Block ciphers",
      "canonical_id": "2018/1",
      "canonical_url": "/problems/2018-1/",
      "appearances": [
        "2018/1"
      ],
      "appearance_links": [
        {
          "text": "2018/1",
          "url": "/problems/2018-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Recall that DES is a block cipher with key space <span\nclass=\"math inline\">\\(K = \\{0,1\\}^{56}\\)</span>, plaintext space <span\nclass=\"math inline\">\\(M = \\{0,1\\}^{64}\\)</span>, and ciphertext space\n<span class=\"math inline\">\\(C = \\{0,1\\}^{64}\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Let <span class=\"math inline\">\\(\\overline{m}\\)</span> denote the\nbitwise complement of a bit string <span\nclass=\"math inline\">\\(m\\)</span> (i.e., <span\nclass=\"math inline\">\\(\\overline{m} = m \\oplus 11\\ldots 1\\)</span>). By\nexamining the description of DES, one can see that if <span\nclass=\"math inline\">\\(c = \\mathrm{DES}_k(m)\\)</span> then <span\nclass=\"math inline\">\\(\\overline{c} =\n\\mathrm{DES}_{\\overline{k}}(\\overline{m})\\)</span>. Can you use this\nproperty of DES to (slightly) improve the running time of exhaustive key\nsearch under a chosen-plaintext attack?</p></li>\n<li><p>Recall that Triple-DES has key space <span\nclass=\"math inline\">\\(K = \\{0,1\\}^{168}\\)</span>. A plaintext <span\nclass=\"math inline\">\\(m \\in \\{0,1\\}^{64}\\)</span> is encrypted under key\n<span class=\"math inline\">\\(k = (k_1,k_2,k_3)\\)</span> (where <span\nclass=\"math inline\">\\(k_1, k_2, k_3 \\in \\{0,1\\}^{56}\\)</span>) as\nfollows: <span class=\"math display\">\\[E_k(m) =\nDES_{k_3}(DES_{k_2}(DES_{k_1}(m))).\\]</span> Describe a known-plaintext\nattack on Triple-DES that is significantly faster than exhaustive key\nsearch. Estimate the time and space requirements of your\nattack.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Recall that DES is a block cipher with key space \\(K = \\{0,1\\}^{56}\\), plaintext space \\(M = \\{0,1\\}^{64}\\), and ciphertext space \\(C = \\{0,1\\}^{64}\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Let \\(\\overline{m}\\) denote the bitwise complement of a bit string \\(m\\) (i.e., \\(\\overline{m} = m \\oplus 11\\ldots 1\\)). By examining the description of DES, one can see that if \\(c = \\mathrm{DES}_k(m)\\) then \\(\\overline{c} = \\mathrm{DES}_{\\overline{k}}(\\overline{m})\\). Can you use this property of DES to (slightly) improve the running time of exhaustive key search under a chosen-plaintext attack?\n\n    \\item Recall that Triple-DES has key space \\(K = \\{0,1\\}^{168}\\). A plaintext \\(m \\in \\{0,1\\}^{64}\\) is encrypted under key \\(k = (k_1,k_2,k_3)\\) (where \\(k_1, k_2, k_3 \\in \\{0,1\\}^{56}\\)) as follows:\n    \\[\n    E_k(m) = DES_{k_3}(DES_{k_2}(DES_{k_1}(m))).\n    \\]\n    Describe a known-plaintext attack on Triple-DES that is significantly faster than exhaustive key search. Estimate the time and space requirements of your attack.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2018/1.tex"
    },
    {
      "id": "2016/6",
      "title": "Message authentication codes",
      "canonical_id": "2016/6",
      "canonical_url": "/problems/2016-6/",
      "appearances": [
        "2016/6"
      ],
      "appearance_links": [
        {
          "text": "2016/6",
          "url": "/problems/2016-6/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Recall the definition of CBC-MAC:</p>\n<ol type=\"a\">\n<li><p>Is CBC-MAC with one-block inputs existentially unforgeable under\na chosen-message attack (EUF-CMA)?</p></li>\n<li><p>Is CBC-MAC with variable-length inputs existentially unforgeable\nunder a chosen-message attack (EUF-CMA)?</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Recall the definition of CBC-MAC:\n\n% Algorithm 1 CBC-MAC\n% Input: An \\(n\\)-block message \\(x = x_1 \\lVert \\cdots \\lVert x_n\\) and a secret key \\(k\\).\n% \\begin{aligned}\n% &1: \\text{IV} \\leftarrow 0^n \\\\\n% &2: y_0 \\leftarrow \\text{IV} \\\\\n% &3: \\text{for } i \\leftarrow 1 \\text{ to } n \\text{ do} \\\\\n% &4: \\quad y_i \\leftarrow \\text{Encrypt}(k, y_{i-1} \\oplus x_i) \\\\\n% &5: \\text{end for}\n% \\end{aligned}\n% Output: \\(y_n\\)\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Is CBC-MAC with one-block inputs existentially unforgeable under a chosen-message attack (EUF-CMA)?  \n    \\item Is CBC-MAC with variable-length inputs existentially unforgeable under a chosen-message attack (EUF-CMA)?\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2016/6.tex"
    },
    {
      "id": "2013/2",
      "title": "Block ciphers",
      "canonical_id": "2013/2",
      "canonical_url": "/problems/2013-2/",
      "appearances": [
        "2013/2"
      ],
      "appearance_links": [
        {
          "text": "2013/2",
          "url": "/problems/2013-2/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Recall that the CBC block cipher mode of operation encrypts a message\n<span class=\"math inline\">\\(m_1 m_2 \\cdots m_n\\)</span> to the\nciphertext <span class=\"math inline\">\\(c_0 c_1 c_2 \\cdots c_n\\)</span>\nwhere <span class=\"math inline\">\\(c_0\\)</span> is chosen at random\nand</p>\n<p><span class=\"math display\">\\[c_i = E_k(m_i \\oplus\nc_{i-1}).\\]</span></p>\n<ol type=\"a\">\n<li><p>Explain how decryption is performed with CBC.</p></li>\n<li><p>We define a new block cipher mode of operation known as UBC\n(Useless Block Chaining), with</p>\n<p><span class=\"math display\">\\[c_i = E_k(m_i) \\oplus\nc_{i-1}.\\]</span></p>\n<p>Show that UBC is, in fact, useless.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Recall that the CBC block cipher mode of operation encrypts a message \\(m_1 m_2 \\cdots m_n\\) to the ciphertext \\(c_0 c_1 c_2 \\cdots c_n\\) where \\(c_0\\) is chosen at random and\n\n\\[\nc_i = E_k(m_i \\oplus c_{i-1}).\n\\]\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Explain how decryption is performed with CBC.\n    \\item We define a new block cipher mode of operation known as UBC (Useless Block Chaining), with\n\n\\[\nc_i = E_k(m_i) \\oplus c_{i-1}.\n\\]\n\nShow that UBC is, in fact, useless.\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2013/2.tex"
    },
    {
      "id": "2011/2",
      "title": "Block ciphers",
      "canonical_id": "2011/2",
      "canonical_url": "/problems/2011-2/",
      "appearances": [
        "2011/2"
      ],
      "appearance_links": [
        {
          "text": "2011/2",
          "url": "/problems/2011-2/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Recall that a Feistel cipher has a round function of the following\nform <span class=\"math display\">\\[L_i^t = R_i^{t-1}, \\qquad\nR_i^t = L_i^{t-1} \\oplus f(R_i^{t-1}, K_i).\\]</span> The plaintext is\n<span class=\"math inline\">\\(L^0 \\,||\\, R^0\\)</span> and the ciphertext\nis <span class=\"math-punct\"><span class=\"math inline\">\\(L^n \\,||\\, R^n\\)</span>.</span></p>\n<ol type=\"a\">\n<li><p>What properties does <span class=\"math inline\">\\(f\\)</span> need\nto satisfy in order for encryption to be invertible? Justify.</p></li>\n<li><p>Describe the decryption algorithm.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Recall that a Feistel cipher has a round function of the following form\n\\[\nL_i^t = R_i^{t-1}, \\qquad\nR_i^t = L_i^{t-1} \\oplus f(R_i^{t-1}, K_i).\n\\]\nThe plaintext is \\(L^0 \\,||\\, R^0\\) and the ciphertext is \\(L^n \\,||\\, R^n\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item What properties does \\(f\\) need to satisfy in order for encryption to be invertible? Justify.\n    \\item Describe the decryption algorithm.\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2011/2.tex"
    },
    {
      "id": "2011/5",
      "title": "Pseudo-random bit generators",
      "canonical_id": "2011/5",
      "canonical_url": "/problems/2011-5/",
      "appearances": [
        "2011/5"
      ],
      "appearance_links": [
        {
          "text": "2011/5",
          "url": "/problems/2011-5/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\((n,e)\\)</span> be an RSA public key,\nand let <span class=\"math inline\">\\(d\\)</span> be the corresponding RSA\nprivate key. Let <span class=\"math inline\">\\(f:\\mathbb{Z}_n \\to\n\\mathbb{Z}_n\\)</span> be defined by <span class=\"math-punct\"><span class=\"math inline\">\\(f(x) =\nx^e \\bmod n\\)</span>.</span> Let <span class=\"math display\">\\[B(x) =\n\\begin{cases}\n1, &amp; \\text{if } x^d \\bmod n \\text{ is odd},\\\\\n0, &amp; \\text{if } x^d \\bmod n \\text{ is even}.\n\\end{cases}\\]</span></p>\n<p>Clearly, <span class=\"math inline\">\\(B(x)\\)</span> is easy to compute\ngiven <span class=\"math inline\">\\(x\\)</span> and <span\nclass=\"math inline\">\\(f^{-1}(x)\\)</span> (since <span\nclass=\"math inline\">\\(f^{-1}(x) = x^d \\bmod n\\)</span>). It can be shown\n(and you may assume) that <span class=\"math inline\">\\(B(x)\\)</span> is\nhard to compute given only <span class=\"math-punct\"><span class=\"math inline\">\\(x\\)</span>.</span></p>\n<ol type=\"a\">\n<li><p>Define (informally) what it means for a PRBG <span\nclass=\"math inline\">\\(G\\)</span> to pass the next bit test.</p></li>\n<li><p>Describe a cryptographically secure PRBG <span\nclass=\"math inline\">\\(G\\)</span> which takes as seed random <span\nclass=\"math inline\">\\(x_0 \\in \\mathbb{Z}_n\\)</span> and uses <span\nclass=\"math inline\">\\(f\\)</span> and <span\nclass=\"math inline\">\\(B\\)</span> above.</p></li>\n<li><p>Prove that the generator <span class=\"math inline\">\\(G\\)</span>\npasses the next bit test.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let \\((n,e)\\) be an RSA public key, and let \\(d\\) be the corresponding RSA private key.\nLet \\(f:\\mathbb{Z}_n \\to \\mathbb{Z}_n\\) be defined by \\(f(x) = x^e \\bmod n\\).\nLet\n\\[\nB(x) =\n\\begin{cases}\n1, & \\text{if } x^d \\bmod n \\text{ is odd},\\\\\n0, & \\text{if } x^d \\bmod n \\text{ is even}.\n\\end{cases}\n\\]\n\nClearly, \\(B(x)\\) is easy to compute given \\(x\\) and \\(f^{-1}(x)\\) (since \\(f^{-1}(x) = x^d \\bmod n\\)). It can be shown (and you may assume) that \\(B(x)\\) is hard to compute given only \\(x\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Define (informally) what it means for a PRBG \\(G\\) to pass the next bit test.\n    \\item Describe a cryptographically secure PRBG \\(G\\) which takes as seed random \\(x_0 \\in \\mathbb{Z}_n\\) and uses \\(f\\) and \\(B\\) above.\n    \\item Prove that the generator \\(G\\) passes the next bit test.\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2011/5.tex"
    },
    {
      "id": "2003/1",
      "title": "Chosen-plaintext attack on two-key Triple-DES",
      "canonical_id": "2003/1",
      "canonical_url": "/problems/2003-1/",
      "appearances": [
        "2003/1"
      ],
      "appearance_links": [
        {
          "text": "2003/1",
          "url": "/problems/2003-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Recall that DES is a block cipher with key space <span\nclass=\"math inline\">\\(K = \\{0, 1\\}^{56}\\)</span>, plaintext space <span\nclass=\"math inline\">\\(M = \\{0, 1\\}^{64}\\)</span>, and ciphertext space\n<span class=\"math inline\">\\(C = \\{0, 1\\}^{64}\\)</span>. Encryption for\n<em>two-key Triple-DES</em> is defined as follows: <span\nclass=\"math display\">\\[E_k(m) =\n\\mathrm{DES}_{k_1}(\\mathrm{DES}_{k_2}^{-1}(\\mathrm{DES}_{k_1}(m))),\\]</span>\nwhere <span class=\"math inline\">\\(k = (k_1, k_2)\\)</span>, and <span\nclass=\"math inline\">\\(k_1, k_2 \\in_R \\{0, 1\\}^{56}\\)</span> is the\nsecret key. Design a <em>chosen-plaintext</em> attack on two-key\nTriple-DES that takes <em>roughly</em> <span\nclass=\"math inline\">\\(2^{56}\\)</span> steps. (A step is a DES encryption\nor decryption operation.) Provide an explanation of why your attack\nworks, and a careful estimate of its space and time requirements. (Hint:\nyour attack may need a <em>lot</em> of chosen plaintext/ciphertext\npairs.)</p>",
      "solution_html": "",
      "raw_statement": "Recall that DES is a block cipher with key space \\(K = \\{0, 1\\}^{56}\\), plaintext space \\(M = \\{0, 1\\}^{64}\\), and ciphertext space \\(C = \\{0, 1\\}^{64}\\). Encryption for \\emph{two-key Triple-DES} is defined as follows:\n\\[\nE_k(m) = \\mathrm{DES}_{k_1}(\\mathrm{DES}_{k_2}^{-1}(\\mathrm{DES}_{k_1}(m))),\n\\]\nwhere \\(k = (k_1, k_2)\\), and \\(k_1, k_2 \\in_R \\{0, 1\\}^{56}\\) is the secret key. Design a \\emph{chosen-plaintext} attack on two-key Triple-DES that takes \\emph{roughly} \\(2^{56}\\) steps. (A step is a DES encryption or decryption operation.) Provide an explanation of why your attack works, and a careful estimate of its space and time requirements. (Hint: your attack may need a \\emph{lot} of chosen plaintext/ciphertext pairs.)",
      "raw_solution": "",
      "source_file": "problems/2003/1.tex"
    },
    {
      "id": "2002/1",
      "title": "Attempts to strengthen DES against exhaustive key search attacks",
      "canonical_id": "2002/1",
      "canonical_url": "/problems/2002-1/",
      "appearances": [
        "2002/1"
      ],
      "appearance_links": [
        {
          "text": "2002/1",
          "url": "/problems/2002-1/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Recall that DES is a symmetric-key encryption scheme with a 56-bit\nkey, and 64-bit plaintext and ciphertext blocks. Consider the following\nproposal for a new symmetric-key encryption scheme based on DES. The\nsecret key for the new scheme is <span class=\"math-punct\"><span class=\"math inline\">\\(k = (k_1,\nk_2)\\)</span>,</span> where <span class=\"math inline\">\\(k_1 \\in\n\\{0,1\\}^{56}\\)</span> and <span class=\"math inline\">\\(k_2 \\in\n\\{0,1\\}^{64}\\)</span> (so <span class=\"math inline\">\\(k\\)</span> is a\n<span class=\"math inline\">\\(120\\)</span>-bit key). Let <span\nclass=\"math inline\">\\(m \\in \\{0,1\\}^{64}\\)</span> be a plaintext\nmessage. Then encryption is defined as follows: <span\nclass=\"math display\">\\[E_k(m) = \\mathrm{DES}_{k_1}(m \\oplus\nk_2).\\]</span></p>\n<ol type=\"a\">\n<li><p>Show how this encryption scheme can be totally broken\u2014that is,\nthe secret key <span class=\"math inline\">\\(k\\)</span> can be\nrecovered\u2014by a known-plaintext attack using <em>roughly</em> <span\nclass=\"math inline\">\\(2^{56}\\)</span> DES encryption/decryption\noperations. Your attack should have little space requirements. You may\nassume that you have a moderate number of plaintext-ciphertext pairs\n<span class=\"math-punct\"><span class=\"math inline\">\\((m_i, c_i = E_k(m_i))\\)</span>.</span> Briefly\njustify why the number of such pairs you use is sufficient to uniquely\ndetermine the key with high probability.</p></li>\n<li><p>Is the encryption scheme with encryption function <span\nclass=\"math inline\">\\(E_k(m) = \\text{DES}_{k_1}(m \\oplus k_2) \\oplus\nk_2\\)</span> any more secure than DES? [Briefly justify your\nanswer.]</p></li>\n<li><p>Is the encryption scheme with encryption function <span\nclass=\"math inline\">\\(E_k(m) = \\text{DES}_{k_1}(m \\oplus k_2) \\oplus\nk_3\\)</span> any more secure than DES? (Here, <span\nclass=\"math inline\">\\(k = (k_1, k_2, k_3)\\)</span> where <span\nclass=\"math inline\">\\(k_1 \\in \\{0,1\\}^{56}\\)</span> and <span\nclass=\"math inline\">\\(k_2, k_3 \\in \\{0,1\\}^{64}\\)</span>.) [Briefly\njustify your answer.]</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Recall that DES is a symmetric-key encryption scheme with a 56-bit key, and 64-bit plaintext and ciphertext blocks.\nConsider the following proposal for a new symmetric-key encryption scheme based on DES.\nThe secret key for the new scheme is \\(k = (k_1, k_2)\\), where \\(k_1 \\in \\{0,1\\}^{56}\\) and \\(k_2 \\in \\{0,1\\}^{64}\\) (so \\(k\\) is a \\(120\\)-bit key).\nLet \\(m \\in \\{0,1\\}^{64}\\) be a plaintext message. Then encryption is defined as follows:\n\\[ E_k(m) = \\mathrm{DES}_{k_1}(m \\oplus k_2).  \\]\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Show how this encryption scheme can be totally broken---that is, the secret key $k$ can be recovered---by a known-plaintext attack using \\emph{roughly} $2^{56}$ DES encryption/decryption operations.\n    Your attack should have little space requirements.\n    You may assume that you have a moderate number of plaintext-ciphertext pairs $(m_i, c_i = E_k(m_i))$.\n    Briefly justify why the number of such pairs you use is sufficient to uniquely determine the key with high probability.\n\n    \\item Is the encryption scheme with encryption function \\(E_k(m) = \\text{DES}_{k_1}(m \\oplus k_2) \\oplus k_2\\) any more secure than DES?\n    [Briefly justify your answer.]\n\n    \\item Is the encryption scheme with encryption function \\(E_k(m) = \\text{DES}_{k_1}(m \\oplus k_2) \\oplus k_3\\) any more secure than DES?\n    (Here, \\(k = (k_1, k_2, k_3)\\) where \\(k_1 \\in \\{0,1\\}^{56}\\) and \\(k_2, k_3 \\in \\{0,1\\}^{64}\\).)\n    [Briefly justify your answer.]\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2002/1.tex"
    }
  ]
}
---
