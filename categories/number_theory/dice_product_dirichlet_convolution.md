# Dirichlet convolution

**Taxonomy Path**: `Number Theory` > `Multiplicative Functions` > `Dirichlet convolution`

## Description
This topic focuses on dirichlet convolution techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The state space consists only of integers of the form floor(M / k). For M <= 10^9, there are at most 2*sqrt(M) approx 63245 such states. In the sum over X, intervals of X where floor(v / X) = q are handled simultaneously as (r - l + 1) * f(q). Using dual-array indexing provides O(1) state lookups with zero hash collisions.
- Common Reductions: An N-sided die with faces 1..N multiplies an initial product P=1 until P > M. Find expected turns modulo 10^9+7. The expected remaining turns f(v) with target threshold v = floor(M / P) satisfies (N - 1) f(v) = N + sum_{X=2}^{min(N, v)} f(floor(v / X)). Because floor(v / X) takes at most 2*sqrt(v) distinct values, quotient chunking computes f(M) across all O(sqrt(M)) states in O(M^{3/4}) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc239_h`](../../analysis/AtCoder-abc239_h.md) | Dice Product 2 | 2686 | An N-sided die with faces 1..N multiplies an initial product P=1 until P > M. Find expected turns modulo 10^9+7. The exp... |
