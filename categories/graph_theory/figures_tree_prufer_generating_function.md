# Prufer Code

**Taxonomy Path**: `Graph Theory` > `Graph Counting` > `Prufer Code`

## Description
This topic focuses on prufer code techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Cayley's tree formula via Prüfer sequences, the number of trees with specified vertex degrees deg_1, ..., deg_N is (N - 2)! / prod (deg_i - 1)!. For part i with d_i available holes, choosing deg_i holes has d_i * (d_i - 1) * ... * (d_i - deg_i + 1) = d_i! / (d_i - deg_i)! ways. Multiplying and summing over all degree sequences sum deg_i = 2N - 2 yields the closed form: prod_{i=1}^N d_i * (sum d_i - N)_{N-2} * (N - 2)! / (N - 2)! = (prod d_i) * (S)_{N-2} mod 998244353, where S = (sum d_i) - N and (S)_k = S * (S - 1) * ... * (S - k + 1) is the falling factorial.
- Common Reductions: Given N parts where part i has d_i holes, we want to connect them using N-1 components to form a connected tree. Each component connects two distinct holes in different parts. Find the number of valid complete figures modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc106_f`](../../analysis/AtCoder-arc106_f.md) | F - Figures | 2754 | Given N parts where part i has d_i holes, we want to connect them using N-1 components to form a connected tree. Each co... |
