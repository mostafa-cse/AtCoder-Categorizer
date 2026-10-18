# Bit Manipulation

**Taxonomy Path**: `Basics` > `Bit Manipulation` > `Bit Manipulation`

## Description
This topic focuses on bit manipulation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A subarray sum $\sum_{i=l}^r 2^{A_i} = 2^k$ is bounded by $M \le k \le M + \lfloor \log_2 N \rfloor + 1$ where $M = \max_{i=l}^r A_i$. In a divide-and-conquer on interval $[L, R]$ splitting at the maximum element $m$, testing the smaller half against $O(\log N)$ candidate powers of 2 via rolling hashes guarantees $O(N \log^2 N)$ total checks.
- Common Reductions: Count subarrays whose power-of-two sum $\sum_{i=l}^r 2^{A_i}$ is a single power of 2. Divide and conquer on range maximums checks the smaller half against $O(\log N)$ candidate powers of 2 via rolling hashes in $O(N \log^2 N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc216_c`](../../analysis/AtCoder-arc216_c.md) | C. Count Power of 2 | 2346 | Count subarrays whose power-of-two sum $\sum_{i=l}^r 2^{A_i}$ is a single power of 2. Divide and conquer on range maximu... |
