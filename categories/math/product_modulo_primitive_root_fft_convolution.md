# Number Theoretic Transform (NTT)

**Taxonomy Path**: `Math` > `Convolution` > `Number Theoretic Transform (NTT)`

## Description
This topic focuses on number theoretic transform (ntt) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Zero elements contribute nothing to products and are ignored. Convolving $cnt$ with itself computes pairwise sums for all ordered pairs $(i, j)$. Subtracting self-products $A_i^2 \pmod P$ and dividing the total sum by 2 yields the exact unordered sum.
- Common Reductions: Compute $\sum_{1 \le i < j \le N} (A_i A_j \pmod P)$ for prime $P = 200003$. $g = 2$ is a primitive root modulo $P$. Using discrete logarithm, map each non-zero $A_i$ to its exponent $e_i \in [0, P - 2]$ such that $g^{e_i} \equiv A_i \pmod P$. Then $A_i A_j \pmod P = g^{(e_i + e_j) \pmod{P - 1}} \pmod P$. The distribution of exponent sums is the polynomial multiplication $C(x) * C(x)$ where $C(x) = \sum cnt[e] x^e$. Fast Fourier Transform (FFT) convolves the frequency array in $O(P \log P)$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc047_c`](../../analysis/AtCoder-agc047_c.md) | C. Product Modulo | 2496 | Compute $\sum_{1 \le i < j \le N} (A_i A_j \pmod P)$ for prime $P = 200003$. $g = 2$ is a primitive root modulo $P$. Usi... |
