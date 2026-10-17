# Bitmask DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Bit Related DP` > `Bitmask DP`

## Description
This topic focuses on bitmask dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let E(mask) be the sum of mutual trust weights between all pairs of employees with both endpoints in mask. For any partition of mask into S and mask \ S, the cut cost is E(mask) - E(S) - E(mask \ S). Submask DP evaluates dp[mask] = max_{S subset mask, lowbit(mask) in S} (dp[mask \ S] + K - (E(mask) - E(S) - E(mask \ S))) in O(3^{N-1}) time.
- Common Reductions: Partition N <= 17 employees into non-empty departments to maximize (m * K) minus the sum of mutual trust w_{i, j} between employees in different departments. Fixing the lowest bit of the remaining vertex subset to belong to the peeled department avoids permutation overcounting.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc056_c`](../../analysis/AtCoder-arc056_c.md) | C. 部門分け | 2179 | Partition N <= 17 employees into non-empty departments to maximize (m * K) minus the sum of mutual trust w_{i, j} betwee... |
