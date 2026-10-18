# DP Optimization using Data Structures [Some Practice Problems]

**Taxonomy Path**: `Dynamic Programming (DP)` > `DP Optimizations` > `DP Optimization using Data Structures [Some Practice Problems]`

## Description
This topic focuses on dp optimization using data structures [some practice problems] techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By Principle of Inclusion-Exclusion on the conditions $X_i \ne X_{i+1}$, the recurrence is $dp[i] = \sum_{j < i} dp[j] (-1)^{i - 1 - j} \min_{j < k \le i} A_k$. Setting $f[i] = (-1)^i dp[i]$ yields $f[i] = - \sum_{j < i} f[j] \min_{j < k \le i} A_k$. The prefix minimum terms form a monotonic histogram that can be maintained dynamically using a monotonic stack with aggregated sums.
- Common Reductions: Count sequences with $1 \le X_i \le A_i$ and $X_i \ne X_{i+1}$. By inclusion-exclusion, the recurrence $f[i] = - \sum_{j < i} f[j] \min_{j < k \le i} A_k$ is evaluated dynamically using a monotonic stack with aggregated dot-products in $O(N)$ time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc115_e`](../../analysis/AtCoder-arc115_e.md) | E. LEQ and NEQ | 2363 | Count sequences with $1 \le X_i \le A_i$ and $X_i \ne X_{i+1}$. By inclusion-exclusion, the recurrence $f[i] = - \sum_{j... |
