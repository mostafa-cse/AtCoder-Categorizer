# Functional Graphs

**Taxonomy Path**: `Miscellaneous` > `General` > `Functional Graphs`

## Description
This topic focuses on functional graphs techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any functional graph on N vertices, every connected component contains exactly one directed cycle, and all strongly connected components are precisely these cycles. Using exponential generating functions (EGF), the cycle structure of functional graphs is governed by exp(sum_{n >= 1} x^n / n^2). The problem reduces to computing the N-th coefficient [x^N] exp(sum_{n=1}^N x^n / n^2) and combining with (N!)^2 factors, which can be computed via CDQ divide-and-conquer NTT or polynomial exp in O(N log^2 N) time.
- Common Reductions: Count the number of functional graphs on N vertices with specific strong component structure modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc318_h`](../../analysis/AtCoder-abc318_h.md) | Ex - Count Strong Test Cases | 2785 | Count the number of functional graphs on N vertices with specific strong component structure modulo 998244353.... |
