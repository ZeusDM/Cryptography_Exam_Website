---
{
  "title": "Digital Signatures",
  "topic": "Digital Signatures",
  "topic_slug": "digital-signatures",
  "abbr": "DS",
  "cluster_count": 7,
  "solved_count": 0,
  "draft_count": 0,
  "clusters": [
    {
      "id": "composite/fdh-rsa",
      "title": "RSA signatures",
      "canonical_id": "composite/fdh-rsa",
      "canonical_url": "/problems/composite-fdh-rsa/",
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
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Recall that in the Full-Domain Hash (FDH) RSA signature scheme, an\nentity (Alice) with public key <span class=\"math inline\">\\((n,\ne)\\)</span> and private key <span class=\"math inline\">\\(d\\)</span>\ngenerates a signature <span class=\"math inline\">\\(s\\)</span> on a\nmessage <span class=\"math inline\">\\(m\\)</span> by computing <span\nclass=\"math display\">\\[s \\equiv H(m)^d \\pmod{n}.\\]</span> Here <span\nclass=\"math inline\">\\(H \\colon \\{0, 1\\}^* \\to \\{0, 1, \\dots, n -\n1\\}\\)</span> is a hash function.</p>\n<ol type=\"a\">\n<li><p>Describe how someone can verify Alice\u2019s signature <span\nclass=\"math inline\">\\(s\\)</span> on a message <span\nclass=\"math inline\">\\(m\\)</span>.</p></li>\n<li><p>Show that FDH RSA is insecure against passive adversaries if\n<span class=\"math inline\">\\(H\\)</span> is not preimage\nresistant.</p></li>\n<li><p>Prove that if finding <span class=\"math inline\">\\(e\\)</span>-th\nroots modulo <span class=\"math inline\">\\(n\\)</span> is intractable, and\nif <span class=\"math inline\">\\(H\\)</span> is a random function, then FDH\nRSA is secure (i.e., existentially unforgeable by an adversary who can\nmount an adaptive chosen-message attack).</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Recall that in the Full-Domain Hash (FDH) RSA signature scheme, an entity (Alice) with public key \\((n, e)\\) and private key \\(d\\) generates a signature \\(s\\) on a message \\(m\\) by computing\n\\[\ns \\equiv H(m)^d \\pmod{n}.\n\\]\nHere \\(H \\colon \\{0, 1\\}^* \\to \\{0, 1, \\dots, n - 1\\}\\) is a hash function.\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Describe how someone can verify Alice's signature \\(s\\) on a message \\(m\\).\n\n    \\item Show that FDH RSA is insecure against passive adversaries if \\(H\\) is not preimage resistant.\n\n    \\item Prove that if finding \\(e\\)-th roots modulo \\(n\\) is intractable, and if \\(H\\) is a random function, then FDH RSA is secure (i.e., existentially unforgeable by an adversary who can mount an adaptive chosen-message attack).\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/composite/fdh-rsa.tex"
    },
    {
      "id": "2020/7",
      "title": "Signature schemes",
      "canonical_id": "2020/7",
      "canonical_url": "/problems/2020-7/",
      "appearances": [
        "2020/7"
      ],
      "appearance_links": [
        {
          "text": "2020/7",
          "url": "/problems/2020-7/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<ol type=\"a\">\n<li><p>Define what it means for a signature scheme to be\nsecure.</p></li>\n</ol>\n<p>In the basic (textbook) RSA signature scheme, the public key is a\npair <span class=\"math inline\">\\((n, e)\\)</span> and the secret key is a\npair <span class=\"math inline\">\\((n, d)\\)</span>. The signature on a\nmessage <span class=\"math inline\">\\(m \\in \\mathbb{Z}_n\\)</span> is <span\nclass=\"math inline\">\\(s \\equiv m^d \\pmod{n}\\)</span>, and verification\nis done by checking if <span class=\"math inline\">\\(s^e \\equiv m\n\\pmod{n}\\)</span>.</p>\n<ol type=\"a\">\n<li><p>Show how to come up with some valid message/signature pairs under\na key-only attack on the basic RSA signature scheme.</p></li>\n<li><p>Show how to come with a forgery for any given message <span\nclass=\"math inline\">\\(m\\)</span> under a chosen-message attack on the\nbasic RSA signature scheme, wherein the adversary is allowed to obtain\nsignatures for at most two messages (neither of which is equal to <span\nclass=\"math inline\">\\(m\\)</span>).</p></li>\n<li><p>One way of building a secure RSA-based signature scheme is to\nsign <span class=\"math inline\">\\(H(m)\\)</span> using a \u201cfull-domain hash\nfunction <span class=\"math inline\">\\(H\\)</span>\u201d. The security proof for\nRSA-FDH is \u201cin the random oracle model\u201d. Briefly explain what the random\noracle model is.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "\\begin{enumerate}[label=(\\alph*)]\n    \\item Define what it means for a signature scheme to be secure.\n\\end{enumerate}\n\nIn the basic (textbook) RSA signature scheme, the public key is a pair \\((n, e)\\) and the secret key is a pair \\((n, d)\\). The signature on a message \\(m \\in \\mathbb{Z}_n\\) is \\(s \\equiv m^d \\pmod{n}\\), and verification is done by checking if \\(s^e \\equiv m \\pmod{n}\\).\n\n\\begin{enumerate}[label=(\\alph*), resume]\n    \\item Show how to come up with some valid message/signature pairs under a key-only attack on the basic RSA signature scheme.\n\n    \\item Show how to come with a forgery for any given message \\(m\\) under a chosen-message attack on the basic RSA signature scheme, wherein the adversary is allowed to obtain signatures for at most two messages (neither of which is equal to \\(m\\)).\n\n    \\item One way of building a secure RSA-based signature scheme is to sign \\(H(m)\\) using a ``full-domain hash function \\(H\\)''. The security proof for RSA-FDH is ``in the random oracle model''. Briefly explain what the random oracle model is.\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2020/7.tex"
    },
    {
      "id": "2018/7",
      "title": "ECDSA",
      "canonical_id": "2018/7",
      "canonical_url": "/problems/2018-7/",
      "appearances": [
        "2018/7"
      ],
      "appearance_links": [
        {
          "text": "2018/7",
          "url": "/problems/2018-7/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Recall the ECDSA signature scheme. The domain parameters consist of a\n256-bit prime <span class=\"math inline\">\\(p\\)</span>, an elliptic curve\n<span class=\"math inline\">\\(E\\)</span> defined over <span\nclass=\"math inline\">\\(\\mathbb{Z}_p\\)</span> with prime <span\nclass=\"math inline\">\\(n = \\#E(\\mathbb{Z}_p)\\)</span>, and a point <span\nclass=\"math inline\">\\(P \\in E(\\mathbb{Z}_p)\\)</span> with <span\nclass=\"math inline\">\\(P \\neq \\infty\\)</span>. Alice\u2019s private key is\n<span class=\"math inline\">\\(a \\in_R [1, n-1]\\)</span> and her public key\nis <span class=\"math inline\">\\(A = aP\\)</span>. To sign a message <span\nclass=\"math inline\">\\(M \\in \\{0,1\\}^*\\)</span>, Alice does the\nfollowing:</p>\n<ol type=\"i\">\n<li><p>Select a per-message secret <span class=\"math inline\">\\(k \\in_R\n[1, n-1]\\)</span>.</p></li>\n<li><p>Compute <span class=\"math inline\">\\(m =\n\\mathrm{SHA256}(M)\\)</span>.</p></li>\n<li><p>Compute <span class=\"math inline\">\\(R = kP\\)</span>. Let <span\nclass=\"math inline\">\\(r = x(R) \\bmod n\\)</span> and check that <span\nclass=\"math inline\">\\(r \\neq 0\\)</span>.</p></li>\n<li><p>Compute <span class=\"math inline\">\\(s = k^{-1}(m + ar) \\bmod\nn\\)</span>, and check that <span class=\"math inline\">\\(s \\neq\n0\\)</span>.</p></li>\n<li><p>Alice\u2019s signature on <span class=\"math inline\">\\(M\\)</span> is\n<span class=\"math inline\">\\((r, s)\\)</span>.</p></li>\n</ol>\n<p>To verify Alice\u2019s signature <span class=\"math inline\">\\((r,\ns)\\)</span> on <span class=\"math inline\">\\(M\\)</span>, Bob does the\nfollowing:</p>\n<ol type=\"i\">\n<li><p>Obtain an authentic copy of Alice\u2019s public key <span\nclass=\"math inline\">\\(A\\)</span>.</p></li>\n<li><p>Check that <span class=\"math inline\">\\(1 \\le r, s \\le\nn-1\\)</span>.</p></li>\n<li><p>Compute <span class=\"math inline\">\\(m =\n\\mathrm{SHA256}(M)\\)</span>.</p></li>\n<li><p>Compute <span class=\"math inline\">\\(u_1 = m s^{-1} \\bmod\nn\\)</span> and <span class=\"math inline\">\\(u_2 = r s^{-1} \\bmod\nn\\)</span>.</p></li>\n<li><p>Compute <span class=\"math inline\">\\(V = u_1 P + u_2 A\\)</span>\nand let <span class=\"math inline\">\\(v = x(V) \\bmod n\\)</span>.</p></li>\n<li><p>Accept if and only if <span class=\"math inline\">\\(v =\nr\\)</span>.</p></li>\n</ol>\n<ol type=\"a\">\n<li><p>Define what it means for a signature scheme to be\nsecure.</p></li>\n<li><p>Suppose now that an adversary knows a message <span\nclass=\"math inline\">\\(M\\)</span> such that <span\nclass=\"math inline\">\\(\\mathrm{SHA256}(M) = 0\\)</span>. Show that the\nadversary can efficiently compute a valid signature for <span\nclass=\"math inline\">\\(M\\)</span>. (The adversary knows the domain\nparameters and Alice\u2019s public key <span\nclass=\"math inline\">\\(A\\)</span>, but does not have access to a signing\noracle.)</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Recall the ECDSA signature scheme. The domain parameters consist of a 256-bit prime \\(p\\), an elliptic curve \\(E\\) defined over \\(\\mathbb{Z}_p\\) with prime \\(n = \\#E(\\mathbb{Z}_p)\\), and a point \\(P \\in E(\\mathbb{Z}_p)\\) with \\(P \\neq \\infty\\). Alice's private key is \\(a \\in_R [1, n-1]\\) and her public key is \\(A = aP\\). To sign a message \\(M \\in \\{0,1\\}^*\\), Alice does the following:\n\\begin{enumerate}[label=(\\roman*), noitemsep]\n    \\item Select a per-message secret \\(k \\in_R [1, n-1]\\).\n    \\item Compute \\(m = \\mathrm{SHA256}(M)\\).\n    \\item Compute \\(R = kP\\). Let \\(r = x(R) \\bmod n\\) and check that \\(r \\neq 0\\).\n    \\item Compute \\(s = k^{-1}(m + ar) \\bmod n\\), and check that \\(s \\neq 0\\).\n    \\item Alice's signature on \\(M\\) is \\((r, s)\\).\n\\end{enumerate}\n\nTo verify Alice's signature \\((r, s)\\) on \\(M\\), Bob does the following:\n\\begin{enumerate}[label=(\\roman*), noitemsep]\n    \\item Obtain an authentic copy of Alice's public key \\(A\\).\n    \\item Check that \\(1 \\le r, s \\le n-1\\).\n    \\item Compute \\(m = \\mathrm{SHA256}(M)\\).\n    \\item Compute \\(u_1 = m s^{-1} \\bmod n\\) and \\(u_2 = r s^{-1} \\bmod n\\).\n    \\item Compute \\(V = u_1 P + u_2 A\\) and let \\(v = x(V) \\bmod n\\).\n    \\item Accept if and only if \\(v = r\\).\n\\end{enumerate}\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Define what it means for a signature scheme to be secure.\n    \n    \\item Suppose now that an adversary knows a message \\(M\\) such that \\(\\mathrm{SHA256}(M) = 0\\). Show that the adversary can efficiently compute a valid signature for \\(M\\).\n    (The adversary knows the domain parameters and Alice's public key \\(A\\), but does not have access to a signing oracle.)\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2018/7.tex"
    },
    {
      "id": "2016/7",
      "title": "Identification schemes",
      "canonical_id": "2016/7",
      "canonical_url": "/problems/2016-7/",
      "appearances": [
        "2016/7"
      ],
      "appearance_links": [
        {
          "text": "2016/7",
          "url": "/problems/2016-7/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Let <span class=\"math inline\">\\(G\\)</span> be a cyclic group of prime\norder <span class=\"math inline\">\\(p\\)</span> with generator <span\nclass=\"math inline\">\\(g\\)</span>. Suppose the verifier is given <span\nclass=\"math inline\">\\(\\beta = g^\\alpha\\)</span> for some randomly\nselected <span class=\"math-punct\"><span class=\"math inline\">\\(\\alpha \\in \\mathbb{Z}_p\\)</span>.</span>\nConsider the zero-knowledge proof of knowledge of <span\nclass=\"math inline\">\\(\\alpha\\)</span> in Figure 1.</p>\n<p>Figure 1: Zero-knowledge proof of knowledge of <span\nclass=\"math inline\">\\(\\alpha\\)</span></p>\n<ol type=\"a\">\n<li><p>Show that the proof is zero-knowledge for an honest\nverifier.</p></li>\n<li><p>Show that a cheating prover can succeed with probability <span\nclass=\"math inline\">\\(1/2\\)</span>.</p></li>\n<li><p>Describe how to modify the protocol so that the prover\u2019s cheating\nprobability is reduced to negligible levels.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Let \\(G\\) be a cyclic group of prime order \\(p\\) with generator \\(g\\). Suppose the verifier is given \\(\\beta = g^\\alpha\\) for some randomly selected \\(\\alpha \\in \\mathbb{Z}_p\\). Consider the zero-knowledge proof of knowledge of \\(\\alpha\\) in Figure 1.\n\nFigure 1: Zero-knowledge proof of knowledge of \\(\\alpha\\)\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Show that the proof is zero-knowledge for an honest verifier.  \n    \\item Show that a cheating prover can succeed with probability \\(1/2\\).  \n    \\item Describe how to modify the protocol so that the prover\u2019s cheating probability is reduced to negligible levels.\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2016/7.tex"
    },
    {
      "id": "2004/4",
      "title": "Fault analysis attack on the RSA signature scheme",
      "canonical_id": "2004/4",
      "canonical_url": "/problems/2004-4/",
      "appearances": [
        "2004/4"
      ],
      "appearance_links": [
        {
          "text": "2004/4",
          "url": "/problems/2004-4/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>Suppose that a smart card is using the Chinese Remainder Theorem for\nRSA signature generation. That is, if <span class=\"math inline\">\\((n,\ne)\\)</span> is the RSA public key and <span\nclass=\"math inline\">\\(d\\)</span> is the corresponding private key, then\nsigning a message <span class=\"math inline\">\\(m\\)</span> is performed as\nfollows:</p>\n<p>i) Compute <span class=\"math-punct\"><span class=\"math inline\">\\(M = H(m)\\)</span>.</span></p>\n<p>ii) Compute <span class=\"math inline\">\\(s_p \\equiv M^{d_p}\n\\pmod{p}\\)</span> and <span class=\"math-punct\"><span class=\"math inline\">\\(s_q \\equiv M^{d_q}\n\\pmod{q}\\)</span>,</span> where <span class=\"math inline\">\\(d_p = d \\bmod\n(p-1)\\)</span> and <span class=\"math-punct\"><span class=\"math inline\">\\(d_q = d \\bmod\n(q-1)\\)</span>.</span></p>\n<p>iii) Find <span class=\"math-punct\"><span class=\"math inline\">\\(s\\)</span>,</span> <span\nclass=\"math inline\">\\(0 \\le s \\le n-1\\)</span>, such that <span\nclass=\"math display\">\\[s \\equiv s_p \\pmod{p}, \\qquad s \\equiv s_q\n\\pmod{q}.\\]</span></p>\n<ol type=\"a\">\n<li><p>Prove that <span class=\"math inline\">\\(s\\)</span> is the correct\nsignature of <span class=\"math inline\">\\(m\\)</span> (that is, prove that\n<span class=\"math-punct\"><span class=\"math inline\">\\(s \\equiv H(m)^d \\pmod{n}\\)</span>).</span></p></li>\n<li><p>Explain why it might be advantageous to compute <span\nclass=\"math inline\">\\(s\\)</span> using the procedure described above\ninstead of computing <span class=\"math inline\">\\(s = H(m)^d \\bmod\nn\\)</span> directly using the repeated square-and-multiply\nalgorithm.</p></li>\n<li><p>Suppose now that an adversary can somehow induce the smart card\nto compute <span class=\"math inline\">\\(s_p\\)</span> incorrectly (and\n<span class=\"math inline\">\\(s_q\\)</span> correctly) while signing a\nmessage. Let <span class=\"math inline\">\\(s&#39;\\)</span> be a resulting\n(incorrect) signature on <span class=\"math-punct\"><span class=\"math inline\">\\(m\\)</span>.</span> Suppose\nthat the adversary has access to the public key <span\nclass=\"math inline\">\\((n, e)\\)</span> and also the signed message <span\nclass=\"math inline\">\\((m, s&#39;)\\)</span>. Show how the adversary can\nefficiently factor <span class=\"math-punct\"><span class=\"math inline\">\\(n\\)</span>.</span></p></li>\n<li><p>Suggest a (realistic and practical) method for preventing this\nattack.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "Suppose that a smart card is using the Chinese Remainder Theorem for RSA signature generation. That is, if \\((n, e)\\) is the RSA public key and \\(d\\) is the corresponding private key, then signing a message \\(m\\) is performed as follows:\n\ni) Compute \\(M = H(m)\\).\n\nii) Compute \\(s_p \\equiv M^{d_p} \\pmod{p}\\) and \\(s_q \\equiv M^{d_q} \\pmod{q}\\), where \\(d_p = d \\bmod (p-1)\\) and \\(d_q = d \\bmod (q-1)\\).\n\niii) Find \\(s\\), \\(0 \\le s \\le n-1\\), such that\n\\[\ns \\equiv s_p \\pmod{p}, \\qquad s \\equiv s_q \\pmod{q}.\n\\]\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Prove that \\(s\\) is the correct signature of \\(m\\) (that is, prove that \\(s \\equiv H(m)^d \\pmod{n}\\)).\n    \\item Explain why it might be advantageous to compute \\(s\\) using the procedure described above instead of computing \\(s = H(m)^d \\bmod n\\) directly using the repeated square-and-multiply algorithm.\n    \\item Suppose now that an adversary can somehow induce the smart card to compute \\(s_p\\) incorrectly (and \\(s_q\\) correctly) while signing a message. Let \\(s'\\) be a resulting (incorrect) signature on \\(m\\). Suppose that the adversary has access to the public key \\((n, e)\\) and also the signed message \\((m, s')\\). Show how the adversary can efficiently factor \\(n\\).\n    \\item Suggest a (realistic and practical) method for preventing this attack.\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2004/4.tex"
    },
    {
      "id": "2002/6",
      "title": "Hash functions and DSA",
      "canonical_id": "2002/6",
      "canonical_url": "/problems/2002-6/",
      "appearances": [
        "2002/6"
      ],
      "appearance_links": [
        {
          "text": "2002/6",
          "url": "/problems/2002-6/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>We recall the DSA signature scheme. The system parameters consist of\na 1024-bit prime <span class=\"math-punct\"><span class=\"math inline\">\\(p\\)</span>,</span> a 160-bit prime\ndivisor <span class=\"math inline\">\\(q\\)</span> of <span\nclass=\"math inline\">\\(p-1\\)</span>, and an element <span\nclass=\"math inline\">\\(g \\in \\mathbb{Z}_p^*\\)</span> of order <span\nclass=\"math inline\">\\(q\\)</span>. SHA-1 is a 160-bit hash function.\nAlice\u2019s private key is <span class=\"math-punct\"><span class=\"math inline\">\\(a \\in\n\\mathbb{Z}_p^*\\)</span>,</span> while her public key is <span\nclass=\"math inline\">\\(h = g^a \\bmod p\\)</span>. To sign a message <span\nclass=\"math inline\">\\(M \\in \\{0,1\\}^*\\)</span>, Alice does the\nfollowing:</p>\n<p>1) Choose a per-message secret number <span\nclass=\"math inline\">\\(k\\)</span> with <span class=\"math inline\">\\(1 \\le\nk \\le q-1\\)</span> and compute <span class=\"math-punct\"><span class=\"math inline\">\\(r \\equiv (g^k\n\\bmod p) \\bmod q\\)</span>.</span> If <span class=\"math-punct\"><span class=\"math inline\">\\(r =\n0\\)</span>,</span> choose another <span class=\"math-punct\"><span class=\"math inline\">\\(k\\)</span>.</span></p>\n<p>2) Compute <span class=\"math-punct\"><span class=\"math inline\">\\(s \\equiv\nk^{-1}(\\mathrm{SHA-1}(M) + a r) \\pmod{q}\\)</span>.</span> If <span\nclass=\"math inline\">\\(s = 0\\)</span>, choose another <span\nclass=\"math inline\">\\(k\\)</span>.</p>\n<p>The signature on <span class=\"math inline\">\\(M\\)</span> is the pair\n<span class=\"math-punct\"><span class=\"math inline\">\\((r, s)\\)</span>.</span></p>\n<p>To verify a signature <span class=\"math inline\">\\((r, s)\\)</span> on\n<span class=\"math-punct\"><span class=\"math inline\">\\(M\\)</span>,</span> Bob does the following:</p>\n<p>(i) Obtain an authentic copy of Alice\u2019s public key <span\nclass=\"math inline\">\\(h\\)</span>.</p>\n<p>(ii) Compute <span class=\"math-punct\"><span class=\"math inline\">\\(m =\n\\mathrm{SHA-1}(M)\\)</span>.</span></p>\n<p>(iii) Check that <span class=\"math-punct\"><span class=\"math inline\">\\(1 \\le r, s \\le\nq-1\\)</span>.</span></p>\n<p>(iv) Compute <span class=\"math inline\">\\(u_1 = m s^{-1} \\bmod\nq\\)</span> and <span class=\"math-punct\"><span class=\"math inline\">\\(u_2 = r s^{-1} \\bmod\nq\\)</span>.</span></p>\n<p>(v) Accept if <span class=\"math-punct\"><span class=\"math inline\">\\(r \\equiv (g^{u_1} h^{u_2})\n\\bmod p \\bmod q\\)</span>.</span> (Otherwise reject.)</p>\n<p>Recall that a signature scheme is secure if it is existentially\nunforgeable by chosen-message attacks. It is insecure if it is not\nsecure.</p>\n<ol type=\"a\">\n<li><p>Define what it means for SHA-1 to be preimage resistant.</p></li>\n<li><p>Define what it means for SHA-1 to be 2nd preimage\nresistant.</p></li>\n<li><p>Define what it means for SHA-1 to be collision\nresistant.</p></li>\n<li><p>Prove that DSA is insecure if SHA-1 is not preimage\nresistant.</p></li>\n<li><p>Prove that DSA is insecure if SHA-1 is not 2nd preimage\nresistant.</p></li>\n<li><p>Prove that DSA is insecure if SHA-1 is not collision\nresistant.</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "We recall the DSA signature scheme. The system parameters consist of a 1024-bit prime \\(p\\), a 160-bit prime divisor \\(q\\) of \\(p-1\\), and an element \\(g \\in \\mathbb{Z}_p^*\\) of order \\(q\\). SHA-1 is a 160-bit hash function. Alice's private key is \\(a \\in \\mathbb{Z}_p^*\\), while her public key is \\(h = g^a \\bmod p\\). To sign a message \\(M \\in \\{0,1\\}^*\\), Alice does the following:\n\n1) Choose a per-message secret number \\(k\\) with \\(1 \\le k \\le q-1\\) and compute\n\\(r \\equiv (g^k \\bmod p) \\bmod q\\). If \\(r = 0\\), choose another \\(k\\).\n\n2) Compute \\(s \\equiv k^{-1}(\\mathrm{SHA-1}(M) + a r) \\pmod{q}\\). If \\(s = 0\\), choose another \\(k\\).\n\nThe signature on \\(M\\) is the pair \\((r, s)\\).\n\nTo verify a signature \\((r, s)\\) on \\(M\\), Bob does the following:\n\n(i) Obtain an authentic copy of Alice's public key \\(h\\).\n\n(ii) Compute \\(m = \\mathrm{SHA-1}(M)\\).\n\n(iii) Check that \\(1 \\le r, s \\le q-1\\).\n\n(iv) Compute \\(u_1 = m s^{-1} \\bmod q\\) and \\(u_2 = r s^{-1} \\bmod q\\).\n\n(v) Accept if \\(r \\equiv (g^{u_1} h^{u_2}) \\bmod p \\bmod q\\). (Otherwise reject.)\n\nRecall that a signature scheme is secure if it is existentially unforgeable by chosen-message attacks. It is insecure if it is not secure.\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Define what it means for SHA-1 to be preimage resistant.\n    \\item Define what it means for SHA-1 to be 2nd preimage resistant.\n    \\item Define what it means for SHA-1 to be collision resistant.\n    \\item Prove that DSA is insecure if SHA-1 is not preimage resistant.\n    \\item Prove that DSA is insecure if SHA-1 is not 2nd preimage resistant.\n    \\item Prove that DSA is insecure if SHA-1 is not collision resistant.\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2002/6.tex"
    },
    {
      "id": "2002/7",
      "title": "Duplicate signatures",
      "canonical_id": "2002/7",
      "canonical_url": "/problems/2002-7/",
      "appearances": [
        "2002/7"
      ],
      "appearance_links": [
        {
          "text": "2002/7",
          "url": "/problems/2002-7/"
        }
      ],
      "status": "none",
      "has_own_solution": false,
      "has_solution": false,
      "has_variant_solution": false,
      "variant_solutions": [],
      "is_incomplete": false,
      "author": "",
      "statement_html": "<p>The Elliptic Curve Digital Signature Algorithm (ECDSA) is as follows:\nLet <span class=\"math inline\">\\(p\\)</span> be a prime, and let <span\nclass=\"math inline\">\\(E\\)</span> be an elliptic curve defined over <span\nclass=\"math inline\">\\(\\mathbb{F}_p\\)</span>. Let <span\nclass=\"math inline\">\\(A\\)</span> be a point on <span\nclass=\"math inline\">\\(E\\)</span> having prime order <span\nclass=\"math inline\">\\(q\\)</span>, such that the Discrete Logarithm\nproblem in <span class=\"math inline\">\\(\\langle A \\rangle\\)</span> is\ninfeasible. Let <span class=\"math inline\">\\(\\mathcal{P} =\n\\{0,1\\}^*\\)</span> denote the set of messages. Define the public\nparameters <span class=\"math-punct\"><span class=\"math inline\">\\(\\mathcal{K} = \\{(p,q,E,A,m,B) : B\n= mA\\}\\)</span>,</span> where <span class=\"math-punct\"><span class=\"math inline\">\\(0 \\le m \\le\nq-1\\)</span>.</span> The values <span class=\"math inline\">\\(p, q, E, A\\)</span>\nand <span class=\"math inline\">\\(B\\)</span> are the public key, and <span\nclass=\"math inline\">\\(m\\)</span> is the private key.</p>\n<p>The signature for a message <span class=\"math inline\">\\(x \\in\n\\mathcal{P}\\)</span> is computed as follows: For <span\nclass=\"math inline\">\\(K = (p,q,E,A,m,B)\\)</span>, and for a (secret)\nrandom number <span class=\"math-punct\"><span class=\"math inline\">\\(k\\)</span>,</span> <span\nclass=\"math inline\">\\(1 \\le k \\le q-1\\)</span>, define <span\nclass=\"math display\">\\[sig_K(x,k) = (r,s),\\]</span> where <span\nclass=\"math inline\">\\(kA = (u,v)\\)</span> and <span\nclass=\"math inline\">\\(r = u \\bmod q\\)</span>, <span\nclass=\"math inline\">\\(s = k^{-1}(\\mathrm{SHA-1}(x) + m r) \\bmod\nq\\)</span>.</p>\n<p>(If either <span class=\"math inline\">\\(r=0\\)</span> or <span\nclass=\"math inline\">\\(s=0\\)</span>, a new random value of <span\nclass=\"math inline\">\\(k\\)</span> should be chosen.)</p>\n<p>To verify A\u2019s signature <span class=\"math inline\">\\((r,s)\\)</span> on\n<span class=\"math-punct\"><span class=\"math inline\">\\(M\\)</span>,</span> Bob does the following:</p>\n<p>(i) Obtain an authentic copy of Alice\u2019s public key <span\nclass=\"math inline\">\\(h\\)</span>.</p>\n<p>(ii) Compute <span class=\"math-punct\"><span class=\"math inline\">\\(m =\n\\mathrm{SHA-1}(M)\\)</span>.</span></p>\n<p>(iii) Check that <span class=\"math-punct\"><span class=\"math inline\">\\(1 \\le r, s \\le\nq-1\\)</span>.</span></p>\n<p>(iv) Compute <span class=\"math inline\">\\(u_1 = m s^{-1} \\bmod\nq\\)</span> and <span class=\"math-punct\"><span class=\"math inline\">\\(u_2 = r s^{-1} \\bmod\nq\\)</span>.</span></p>\n<p>(v) Accept iff <span class=\"math inline\">\\(r = (h u_1 + B\nu_2)\\!\\restriction_q\\)</span> (i.e., the <span\nclass=\"math inline\">\\(x\\)</span>-coordinate modulo <span\nclass=\"math inline\">\\(q\\)</span> of the point <span\nclass=\"math inline\">\\(u_1 A + u_2 B\\)</span>).</p>\n<p>Recall that a signature scheme is secure if it is existentially\nforgeable, etc.</p>\n<ol type=\"a\">\n<li><p>Suppose that two messages <span class=\"math inline\">\\(x\\)</span>\nand <span class=\"math inline\">\\(x&#39;\\)</span> are signed with the same\n<span class=\"math inline\">\\(k\\)</span> under the same key, producing\nsignatures <span class=\"math inline\">\\((r,s)\\)</span> and <span\nclass=\"math inline\">\\((r&#39;,s&#39;)\\)</span>. Show that if SHA-1 is\nused as the hash, then <span class=\"math inline\">\\(x \\neq\nx&#39;\\)</span> can still yield the same signature <span\nclass=\"math inline\">\\((r,s)\\)</span> with non-negligible probability.\nExplain how this leads to an attack on the ECDSA signature\nscheme.</p></li>\n<li><p>Suppose that two messages <span class=\"math inline\">\\(x\\)</span>\nand <span class=\"math inline\">\\(x&#39;\\)</span> are said to have\nduplicate ECDSA signatures if <span\nclass=\"math inline\">\\(\\mathrm{SHA\\text{-}1}(x) \\neq\n\\mathrm{SHA\\text{-}1}(x&#39;)\\)</span> but <span\nclass=\"math inline\">\\(\\mathrm{sig}_K(x,k) =\n\\mathrm{sig}_K(x&#39;,k&#39;)\\)</span> for some integers <span\nclass=\"math inline\">\\(k, k&#39;\\)</span> for some key parameters.\nSuppose the public key parameters <span class=\"math inline\">\\(p, q,\nE\\)</span> and <span class=\"math inline\">\\(A\\)</span> are fixed. Given\nany two messages <span class=\"math inline\">\\(x\\)</span> and <span\nclass=\"math inline\">\\(x&#39;\\)</span> such that <span\nclass=\"math inline\">\\(\\mathrm{SHA\\text{-}1}(x) \\neq\n\\mathrm{SHA\\text{-}1}(x&#39;)\\)</span>, show that it is possible for\nAlice to choose a private key <span class=\"math inline\">\\(m\\)</span>\n(and hence a corresponding public key <span\nclass=\"math inline\">\\(B\\)</span>) so that <span\nclass=\"math inline\">\\(x\\)</span> and <span\nclass=\"math inline\">\\(x&#39;\\)</span> have duplicate ECDSA signatures\nunder the key <span class=\"math inline\">\\(p, q, E, A, m\\)</span> and\n<span class=\"math-punct\"><span class=\"math inline\">\\(B\\)</span>.</span></p></li>\n<li><p>Suppose that Alice, say, signs message <span\nclass=\"math inline\">\\(x\\)</span> with signature <span\nclass=\"math inline\">\\((r,s)\\)</span>, and then later claims that she\nreally signed the message <span class=\"math-punct\"><span class=\"math inline\">\\(x&#39;\\)</span>,</span>\nwhere <span class=\"math inline\">\\((r,s)\\)</span> is also a signature on\n<span class=\"math-punct\"><span class=\"math inline\">\\(x&#39;\\)</span>.</span> Show that an adversary can\nnow easily compute Alice\u2019s secret key.</p></li>\n<li><p>We have shown that Alice can choose her private key in such a way\nthat she can later construct duplicate signatures on two messages <span\nclass=\"math inline\">\\(x\\)</span> and <span\nclass=\"math inline\">\\(x&#39;\\)</span>. Does this property mean that the\nECDSA is \u201cinsecure\u201d? (Discuss.)</p></li>\n</ol>",
      "solution_html": "",
      "raw_statement": "The Elliptic Curve Digital Signature Algorithm (ECDSA) is as follows: Let \\(p\\) be a prime, and let \\(E\\) be an elliptic curve defined over \\(\\mathbb{F}_p\\). Let \\(A\\) be a point on \\(E\\) having prime order \\(q\\), such that the Discrete Logarithm problem in \\(\\langle A \\rangle\\) is infeasible. Let \\(\\mathcal{P} = \\{0,1\\}^*\\) denote the set of messages. Define the public parameters \\(\\mathcal{K} = \\{(p,q,E,A,m,B) : B = mA\\}\\), where \\(0 \\le m \\le q-1\\). The values \\(p, q, E, A\\) and \\(B\\) are the public key, and \\(m\\) is the private key.\n\nThe signature for a message \\(x \\in \\mathcal{P}\\) is computed as follows: For \\(K = (p,q,E,A,m,B)\\), and for a (secret) random number \\(k\\), \\(1 \\le k \\le q-1\\), define\n\\[\nsig_K(x,k) = (r,s),\n\\]\nwhere \\(kA = (u,v)\\) and \\(r = u \\bmod q\\), \\(s = k^{-1}(\\mathrm{SHA-1}(x) + m r) \\bmod q\\).\n\n(If either \\(r=0\\) or \\(s=0\\), a new random value of \\(k\\) should be chosen.)\n\nTo verify A's signature \\((r,s)\\) on \\(M\\), Bob does the following:\n\n(i) Obtain an authentic copy of Alice's public key \\(h\\).\n\n(ii) Compute \\(m = \\mathrm{SHA-1}(M)\\).\n\n(iii) Check that \\(1 \\le r, s \\le q-1\\).\n\n(iv) Compute \\(u_1 = m s^{-1} \\bmod q\\) and \\(u_2 = r s^{-1} \\bmod q\\).\n\n(v) Accept iff \\(r = (h u_1 + B u_2)\\!\\restriction_q\\) (i.e., the \\(x\\)-coordinate modulo \\(q\\) of the point \\(u_1 A + u_2 B\\)).\n\nRecall that a signature scheme is secure if it is existentially forgeable, etc.\n\n\\begin{enumerate}[label=(\\alph*)]\n    \\item Suppose that two messages \\(x\\) and \\(x'\\) are signed with the same \\(k\\) under the same key, producing signatures \\((r,s)\\) and \\((r',s')\\). Show that if SHA-1 is used as the hash, then \\(x \\neq x'\\) can still yield the same signature \\((r,s)\\) with non-negligible probability. Explain how this leads to an attack on the ECDSA signature scheme.\n    \\item Suppose that two messages \\(x\\) and \\(x'\\) are said to have duplicate ECDSA signatures if \\(\\mathrm{SHA\\text{-}1}(x) \\neq \\mathrm{SHA\\text{-}1}(x')\\) but \\(\\mathrm{sig}_K(x,k) = \\mathrm{sig}_K(x',k')\\) for some integers \\(k, k'\\) for some key parameters. Suppose the public key parameters \\(p, q, E\\) and \\(A\\) are fixed. Given any two messages \\(x\\) and \\(x'\\) such that \\(\\mathrm{SHA\\text{-}1}(x) \\neq \\mathrm{SHA\\text{-}1}(x')\\), show that it is possible for Alice to choose a private key \\(m\\) (and hence a corresponding public key \\(B\\)) so that \\(x\\) and \\(x'\\) have duplicate ECDSA signatures under the key \\(p, q, E, A, m\\) and \\(B\\).\n    \\item Suppose that Alice, say, signs message \\(x\\) with signature \\((r,s)\\), and then later claims that she really signed the message \\(x'\\), where \\((r,s)\\) is also a signature on \\(x'\\). Show that an adversary can now easily compute Alice's secret key.\n    \\item We have shown that Alice can choose her private key in such a way that she can later construct duplicate signatures on two messages \\(x\\) and \\(x'\\). Does this property mean that the ECDSA is \u201cinsecure\u201d? (Discuss.)\n\n\\end{enumerate}",
      "raw_solution": "",
      "source_file": "problems/2002/7.tex"
    }
  ]
}
---
