# Number Theoretic Transform (NTT)

**Taxonomy Path**: `Math` > `Convolution` > `Number Theoretic Transform (NTT)`

## Description
This topic focuses on number theoretic transform (ntt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The mismatch count at offset $i$ is $\sum_{j=0}^{|T|-1} [S[i+j] \neq T[j]] = \sum [S[i+j] == 0 \land T[j] == 1] + \sum [S[i+j] == 1 \land T[j] == 0]$.
Let $T^R$ be the reversal of $T$. Then $\sum_{j=0}^{|T|-1} S_1[i+j] T_0^R[|T|-1-j]$ is precisely the convolution of indicator array $S_1$ with $T_0^R$, evaluated at index $i + |T| - 1$. Similarly, the other term is the convolution of $S_0$ with $T_1^R$. Using NTT modulo 998244353, both convolutions are computed in $O(|S| \log |S|)$ time.
- Common Reductions: Given binary strings $S$ and $T$ ($|T| \le |S| \le 10^6$). Choose a substring of $S$ of length $|T|$ to minimize the Hamming distance (number of differing characters) from $T$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc196_f`](../../analysis/AtCoder-abc196_f.md) | F. Substring 2 | 2274 | Given binary strings $S$ and $T$ ($|T| \le |S| \le 10^6$). Choose a substring of $S$ of length $|T|$ to minimize the Ham... |
