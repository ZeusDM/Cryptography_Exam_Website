---
{
  "title": "RSA Cryptosystem",
  "topic": "RSA Cryptosystem",
  "topic_slug": "rsa-cryptosystem",
  "abbr": "RSA",
  "cluster_count": 7,
  "solved_count": 0,
  "draft_count": 0,
  "clusters": [
    {
      "id": "2020/4",
      "title": "Integer factorization",
      "canonical_id": "2020/4",
      "canonical_url": "/problems/2020-4/",
      "appearances": [
        "2020/4",
        "2017/4"
      ],
      "appearance_links": [
        {
          "text": "2020/4",
          "url": "/problems/2020-4/"
        },
        {
          "text": "2017/4",
          "url": "/problems/2017-4/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Describe the <em>random squares method</em> for factoring a\nnumber <span class=\"math inline\">\\(n\\)</span> that is not a prime or a\nprime power. You are not expected to analyze the running time of the\nalgorithm. (Note: In Stinson\u2019s book, the algorithm is called \u201cDixon\u2019s\nrandom squares algorithm\u201d. In Koblitnz\u2019s book, the algorithm is called\n\u201cFactor base algorithm\u201d.)</p></li>\n<li><p>Explain the trade-off that dictates the optimal size of the\nfactor base.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Describe the \\emph{random squares method} for factoring a number \\(n\\) that is not a prime or a prime power. You are not expected to analyze the running time of the algorithm.\n    (Note: In Stinson's book, the algorithm is called ``Dixon's random squares algorithm''. In Koblitnz's book, the algorithm is called ``Factor base algorithm''.)\n\n    \\item Explain the trade-off that dictates the optimal size of the factor base.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2020/4.tex"
    },
    {
      "id": "2019/4",
      "title": "Cryptanalysis of RSA",
      "canonical_id": "2019/4",
      "canonical_url": "/problems/2019-4/",
      "appearances": [
        "2019/4"
      ],
      "appearance_links": [
        {
          "text": "2019/4",
          "url": "/problems/2019-4/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Suppose that Alice and Bob agree to generate and share a common RSA\nmodulus <span class=\"math inline\">\\(n = pq\\)</span> for use in RSA\nencryption. Alice chooses an encryption exponent <span\nclass=\"math inline\">\\(e_a\\)</span> and the corresponding decryption\nexponent <span class=\"math inline\">\\(d_a\\)</span>, and Bob chooses an\nencryption exponent <span class=\"math inline\">\\(e_b\\)</span> and the\ncorresponding decryption exponent <span\nclass=\"math inline\">\\(d_b\\)</span>. Suppose furthermore <span\nclass=\"math inline\">\\(\\gcd(e_a,e_b)=1\\)</span>. Show that an adversary\nwho acquires a pair of ciphertexts <span class=\"math inline\">\\(c_a\n\\equiv m^{e_a} \\pmod{n}\\)</span> and <span class=\"math inline\">\\(c_b\n\\equiv m^{e_b} \\pmod{n}\\)</span> corresponding to a single message <span\nclass=\"math inline\">\\(m\\)</span> encrypted to Alice and Bob respectively\ncan recover the plaintext message <span class=\"math inline\">\\(m\\)</span>\nefficiently.</p>",
      "solution_html": "",
      "raw_statement": "Suppose that Alice and Bob agree to generate and share a common RSA modulus \\(n = pq\\) for use in RSA encryption. Alice chooses an encryption exponent \\(e_a\\) and the corresponding decryption exponent \\(d_a\\), and Bob chooses an encryption exponent \\(e_b\\) and the corresponding decryption exponent \\(d_b\\). Suppose furthermore \\(\\gcd(e_a,e_b)=1\\). Show that an adversary who acquires a pair of ciphertexts\n\\( c_a \\equiv m^{e_a} \\pmod{n}\\) and \\(c_b \\equiv m^{e_b} \\pmod{n} \\)\ncorresponding to a single message \\(m\\) encrypted to Alice and Bob respectively can recover the plaintext message \\(m\\) efficiently.",
      "raw_solution": "",
      "source_file": "problems/2019/4.tex"
    },
    {
      "id": "2018/5",
      "title": "RSA",
      "canonical_id": "2018/5",
      "canonical_url": "/problems/2018-5/",
      "appearances": [
        "2018/5"
      ],
      "appearance_links": [
        {
          "text": "2018/5",
          "url": "/problems/2018-5/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Suppose that Alice\u2019s RSA public key is <span\nclass=\"math inline\">\\((n = 143, e = 7)\\)</span>. Determine her private\nkey <span class=\"math inline\">\\(d\\)</span>.</p></li>\n<li><p>Let <span class=\"math inline\">\\((n,e)\\)</span> be an RSA public\nkey, where <span class=\"math inline\">\\(n = pq\\)</span>, and <span\nclass=\"math inline\">\\(e\\)</span> is an integer with <span\nclass=\"math inline\">\\(1 &lt; e &lt; \\phi(n)\\)</span> and <span\nclass=\"math inline\">\\(\\gcd(e, \\phi(n)) = 1\\)</span>. It is known that\nthe number of plaintexts <span class=\"math inline\">\\(m \\in [0,\nn-1]\\)</span> satisfying <span class=\"math inline\">\\(m^e \\equiv m \\pmod\nn\\)</span> is <span class=\"math display\">\\[[1 + \\gcd(e-1, p-1)] \\cdot [1\n+ \\gcd(e-1, q-1)].\\]</span> Such a plaintext message <span\nclass=\"math inline\">\\(m\\)</span> is called an <em>unconcealed\nmessage</em> since its RSA cyphertext is equal to <span\nclass=\"math inline\">\\(m\\)</span> itself. Prove that there is at least\none value of <span class=\"math inline\">\\(e\\)</span>, <span\nclass=\"math inline\">\\(1 &lt; e &lt; \\phi(n)\\)</span>, <span\nclass=\"math inline\">\\(\\gcd(e, \\phi(n)) = 1\\)</span>, such that <span\nclass=\"math inline\">\\(m^e \\equiv m \\pmod n\\)</span> for all <span\nclass=\"math inline\">\\(m \\in [0, n-1]\\)</span>.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Suppose that Alice's RSA public key is \\((n = 143, e = 7)\\). Determine her private key \\(d\\).\n    \n    \\item Let \\((n,e)\\) be an RSA public key, where \\(n = pq\\), and \\(e\\) is an integer with \\(1 < e < \\phi(n)\\) and \\(\\gcd(e, \\phi(n)) = 1\\). It is known that the number of plaintexts \\(m \\in [0, n-1]\\) satisfying \\(m^e \\equiv m \\pmod n\\) is\n    \\[\n    [1 + \\gcd(e-1, p-1)] \\cdot [1 + \\gcd(e-1, q-1)].\n    \\]\n    Such a plaintext message \\(m\\) is called an \\emph{unconcealed message} since its RSA cyphertext is equal to \\(m\\) itself.\n    Prove that there is at least one value of \\(e\\), \\(1 < e < \\phi(n)\\), \\(\\gcd(e, \\phi(n)) = 1\\), such that \\(m^e \\equiv m \\pmod n\\) for all \\(m \\in [0, n-1]\\).\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2018/5.tex"
    },
    {
      "id": "2016/4",
      "title": "RSA",
      "canonical_id": "2016/4",
      "canonical_url": "/problems/2016-4/",
      "appearances": [
        "2016/4"
      ],
      "appearance_links": [
        {
          "text": "2016/4",
          "url": "/problems/2016-4/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Suppose that textbook RSA is used to encrypt a random 56-bit DES key\n<span class=\"math inline\">\\(k\\)</span> without padding; that is, the\nvalue of <span class=\"math inline\">\\(k\\)</span> as an integer is used as\nan RSA plaintext. Given the corresponding RSA ciphertext, give a\n(classical) algorithm that, with high probability, recovers the key\n<span class=\"math inline\">\\(k\\)</span> in substantially fewer than <span\nclass=\"math inline\">\\(2^{56}\\)</span> operations. Hint: Use the fact\nthat a random integer 56-bit integer factors into a product of two\nintegers less than <span class=\"math inline\">\\(2^{29}\\)</span> with high\nprobability.</p>",
      "solution_html": "",
      "raw_statement": "Suppose that textbook RSA is used to encrypt a random 56-bit DES key \\(k\\) without padding; that is, the value of \\(k\\) as an integer is used as an RSA plaintext. Given the corresponding RSA ciphertext, give a (classical) algorithm that, with high probability, recovers the key \\(k\\) in substantially fewer than \\(2^{56}\\) operations.\nHint: Use the fact that a random integer 56-bit integer factors into a product of two integers less than \\(2^{29}\\) with high probability.",
      "raw_solution": "",
      "source_file": "problems/2016/4.tex"
    },
    {
      "id": "2013/5",
      "title": "RSA",
      "canonical_id": "2013/5",
      "canonical_url": "/problems/2013-5/",
      "appearances": [
        "2013/5"
      ],
      "appearance_links": [
        {
          "text": "2013/5",
          "url": "/problems/2013-5/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Alice has a corrupted copy of Bob\u2019s RSA public key <span\nclass=\"math inline\">\\((n, e)\\)</span>, in which one bit of the public\nexponent <span class=\"math inline\">\\(e\\)</span> is wrong. Alice encrypts\na message <span class=\"math inline\">\\(m\\)</span> under the textbook RSA\nscheme using this corrupted public key, and sends the resulting\nciphertext <span class=\"math inline\">\\(c_1\\)</span> to Bob. Later, Alice\nobtains a correct copy of Bob\u2019s RSA public key, and sends an encryption\n<span class=\"math inline\">\\(c_2\\)</span> of the same message <span\nclass=\"math inline\">\\(m\\)</span> under textbook RSA using the correct\nkey. An adversary, who knows Bob\u2019s public key, obtains both <span\nclass=\"math inline\">\\(c_1\\)</span> and <span\nclass=\"math inline\">\\(c_2\\)</span>. Show how the adversary can obtain\n<span class=\"math inline\">\\(m\\)</span>.</p>",
      "solution_html": "",
      "raw_statement": "Alice has a corrupted copy of Bob\u2019s RSA public key \\((n, e)\\), in which one bit of the public exponent \\(e\\) is wrong. Alice encrypts a message \\(m\\) under the textbook RSA scheme using this corrupted public key, and sends the resulting ciphertext \\(c_1\\) to Bob. Later, Alice obtains a correct copy of Bob\u2019s RSA public key, and sends an encryption \\(c_2\\) of the same message \\(m\\) under textbook RSA using the correct key. An adversary, who knows Bob\u2019s public key, obtains both \\(c_1\\) and \\(c_2\\). Show how the adversary can obtain \\(m\\).",
      "raw_solution": "",
      "source_file": "problems/2013/5.tex"
    },
    {
      "id": "2003/3",
      "title": "Partial key-exposure in RSA",
      "canonical_id": "2003/3",
      "canonical_url": "/problems/2003-3/",
      "appearances": [
        "2003/3"
      ],
      "appearance_links": [
        {
          "text": "2003/3",
          "url": "/problems/2003-3/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>This exercise shows that if the encryption exponent in RSA is <span\nclass=\"math inline\">\\(e = 3\\)</span>, then the left half of the bits of\n<span class=\"math inline\">\\(d\\)</span> can be very easily computed.\n(More precisely, the possible values for the left half of the bits can\nbe narrowed to one or two.)</p>\n<p>Let <span class=\"math inline\">\\(n = pq\\)</span> where <span\nclass=\"math inline\">\\(p\\)</span> and <span\nclass=\"math inline\">\\(q\\)</span> are primes with <span\nclass=\"math inline\">\\(5 \\le p &lt; q &lt; 2p\\)</span>. Let integers\n<span class=\"math inline\">\\(e\\)</span> and <span\nclass=\"math inline\">\\(d\\)</span> satisfy <span class=\"math inline\">\\(1\n&lt; e, d &lt; \\phi(n)\\)</span> and <span class=\"math inline\">\\(ed\n\\equiv 1 \\pmod{\\phi(n)}\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Prove that there exists an integer <span\nclass=\"math inline\">\\(k\\)</span> satisfying <span\nclass=\"math inline\">\\(ed - k\\phi(n) = 1\\)</span> and <span\nclass=\"math inline\">\\(1 \\le k &lt; e\\)</span>.</p></li>\n<li><p>Let <span class=\"math inline\">\\(\\hat{d} = \\lfloor \\frac{kn+1}{e}\n\\rfloor\\)</span>. Prove that <span class=\"math inline\">\\(|\\hat{d} - d|\n&lt; 3\\sqrt{n}\\)</span>.</p></li>\n<li><p>Prove that if <span class=\"math inline\">\\(e = 3\\)</span> then\n<span class=\"math inline\">\\(k = 2\\)</span>.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "This exercise shows that if the encryption exponent in RSA is \\(e = 3\\), then the left half of the bits of \\(d\\) can be very easily computed. (More precisely, the possible values for the left half of the bits can be narrowed to one or two.)\n\nLet \\(n = pq\\) where \\(p\\) and \\(q\\) are primes with \\(5 \\le p < q < 2p\\). Let integers \\(e\\) and \\(d\\) satisfy \\(1 < e, d < \\phi(n)\\) and \\(ed \\equiv 1 \\pmod{\\phi(n)}\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Prove that there exists an integer \\(k\\) satisfying \\(ed - k\\phi(n) = 1\\) and \\(1 \\le k < e\\).\n\n    \\item Let \\(\\hat{d} = \\lfloor \\frac{kn+1}{e} \\rfloor\\). Prove that \\(|\\hat{d} - d| < 3\\sqrt{n}\\).\n\n    \\item Prove that if \\(e = 3\\) then \\(k = 2\\).\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2003/3.tex"
    },
    {
      "id": "2002/4",
      "title": "Speeding up RSA decryption",
      "canonical_id": "2002/4",
      "canonical_url": "/problems/2002-4/",
      "appearances": [
        "2002/4"
      ],
      "appearance_links": [
        {
          "text": "2002/4",
          "url": "/problems/2002-4/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\((n, e)\\)</span> be Alice\u2019s RSA public\nkey, and let <span class=\"math inline\">\\(d\\)</span> be her corresponding\nprivate key. Recall that the RSA encryption operation is <span\nclass=\"math inline\">\\(c = m^e \\bmod n\\)</span>, while the RSA decryption\noperation is <span class=\"math-punct\"><span class=\"math inline\">\\(m = c^d \\bmod n\\)</span>.</span> One\nway to speed up RSA decryption is to precompute <span\nclass=\"math inline\">\\(d_p = d \\bmod (p - 1)\\)</span> and <span\nclass=\"math inline\">\\(d_q = d \\bmod (q - 1)\\)</span>. Then decryption of\na ciphertext <span class=\"math inline\">\\(c\\)</span> can be performed by\ncomputing <span class=\"math inline\">\\(m_p = c^{d_p} \\bmod p\\)</span> and\n<span class=\"math-punct\"><span class=\"math inline\">\\(m_q = c^{d_q} \\bmod q\\)</span>,</span> and then\nfinding <span class=\"math-punct\"><span class=\"math inline\">\\(m\\)</span>,</span> <span\nclass=\"math inline\">\\(0 \\le m \\le n - 1\\)</span>, such that <span\nclass=\"math inline\">\\(m \\equiv m_p \\pmod p\\)</span> and <span\nclass=\"math inline\">\\(m \\equiv m_q \\pmod q\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Describe a procedure (i.e., a formula) that Alice can use to\ncompute <span class=\"math inline\">\\(m\\)</span> efficiently, given <span\nclass=\"math inline\">\\(m_p\\)</span> and <span\nclass=\"math inline\">\\(m_q\\)</span>.</p></li>\n<li><p>Prove that <span class=\"math inline\">\\(m\\)</span> is the correct\ndecryption of <span class=\"math-punct\"><span class=\"math inline\">\\(c\\)</span>.</span> That is, prove\nthat <span class=\"math-punct\"><span class=\"math inline\">\\(m \\equiv c^d\n\\pmod{n}\\)</span>.</span></p></li>\n<li><p>Briefly justify the assertion that this method of decryption can\nspeed up RSA decryption by approximately 75</p></li>\n<li><p>Devise an algorithm which, on input <span\nclass=\"math inline\">\\(n\\)</span> and <span\nclass=\"math inline\">\\(e\\)</span>, factors <span\nclass=\"math inline\">\\(n\\)</span> in <span\nclass=\"math inline\">\\(O(\\min(d_p, d_q))\\)</span> steps. (A \u201cstep\u201d is any\noperation whose running time is polynomial in <span\nclass=\"math inline\">\\(\\log n\\)</span>.) State any assumptions you may\nmake. [This exercise shows that Alice should not try to speed up\ndecryption by selecting <span class=\"math inline\">\\(d\\)</span> so that\n<span class=\"math inline\">\\(d_p\\)</span> and <span\nclass=\"math inline\">\\(d_q\\)</span> are too small.]</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let \\((n, e)\\) be Alice's RSA public key, and let \\(d\\) be her corresponding private key. Recall that the RSA encryption operation is \\(c = m^e \\bmod n\\), while the RSA decryption operation is \\(m = c^d \\bmod n\\). One way to speed up RSA decryption is to precompute \\(d_p = d \\bmod (p - 1)\\) and \\(d_q = d \\bmod (q - 1)\\). Then decryption of a ciphertext \\(c\\) can be performed by computing \\(m_p = c^{d_p} \\bmod p\\) and \\(m_q = c^{d_q} \\bmod q\\), and then finding \\(m\\), \\(0 \\le m \\le n - 1\\), such that\n\\(m \\equiv m_p \\pmod p\\) and \\(m \\equiv m_q \\pmod q\\).\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Describe a procedure (i.e., a formula) that Alice can use to compute \\(m\\) efficiently, given \\(m_p\\) and \\(m_q\\).\n    \\item Prove that \\(m\\) is the correct decryption of \\(c\\). That is, prove that \\(m \\equiv c^d \\pmod{n}\\).\n    \\item Briefly justify the assertion that this method of decryption can speed up RSA decryption by approximately 75%, given that a modular exponentiation operation modulo \\(n\\) can be done in \\(O((\\log n)^3)\\) bit operations and given that \\(p \\approx q\\).\n    \\item Devise an algorithm which, on input \\(n\\) and \\(e\\), factors \\(n\\) in \\(O(\\min(d_p, d_q))\\) steps. (A \u201cstep\u201d is any operation whose running time is polynomial in \\(\\log n\\).) State any assumptions you may make. [This exercise shows that Alice should not try to speed up decryption by selecting \\(d\\) so that \\(d_p\\) and \\(d_q\\) are too small.]\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2002/4.tex"
    }
  ]
}
---
