# Meet in the Middle

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Meet in the Middle`

## Description
This topic focuses on meet in the middle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: There are at most 25 primes $\le 100$. By splitting the primes into two subsets—small primes $\le 19$ (8 primes) and large primes in $[23, 97]$ (17 primes)—the number of smooth numbers $\le 10^{16}$ generated independently by each half is bounded by $\approx 3.2 \times 10^6$ and $\approx 2.8 \times 10^6$, perfectly balanced for meet-in-the-middle.
- Common Reductions: Count $P$-smooth numbers $\le N$ ($P \le 100, N \le 10^{16}$). Splitting the 25 primes into small primes $\le 19$ (8 primes) and large primes in $[23, 97]$ (17 primes) balances search spaces at $\approx 3 \times 10^6$, solved via meet-in-the-middle in $O(M_1 \log M_1 + M_2 \log M_2)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc300_g`](../../analysis/AtCoder-abc300_g.md) | G. P-smooth number | 2343 | Count $P$-smooth numbers $\le N$ ($P \le 100, N \le 10^{16}$). Splitting the 25 primes into small primes $\le 19$ (8 pri... |
