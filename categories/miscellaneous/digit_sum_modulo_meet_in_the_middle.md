# Meet in the Middle

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Meet in the Middle`

## Description
This topic focuses on meet in the middle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Writing $N = A \times 10^5 + B$ decomposes $S(N) = S(A) + S(B)$. The congruence becomes $(A \times 10^5 - S(A)) \equiv (S(B) - B) \pmod K$. Precomputing frequencies of $(S(B) - B) \bmod K$ for $B \in [0, 10^5)$ enables $O(1)$ lookups for each $A \le \lfloor M / 10^5 \rfloor$.
- Common Reductions: Count non-negative integers $N \le M \le 10^{10}$ such that $N \equiv S(N) \pmod K$. Because $N - S(N)$ is inherently divisible by 9, $N - S(N)$ must be a multiple of $L = \text{lcm}(K, 9)$. If $L \ge 10^5$, we iterate over the few multiples $X$ of $L$ and test possible digit sums $d \in [0, 90]$. If $L < 10^5$, then $K < 10^5$, and we perform Meet-in-the-Middle on the upper and lower 5 digits.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc052_d`](../../analysis/AtCoder-arc052_d.md) | D. 9 | 2436 | Count non-negative integers $N \le M \le 10^{10}$ such that $N \equiv S(N) \pmod K$. Because $N - S(N)$ is inherently di... |
