# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By the 0-1 principle, sum_{a in A} a = sum_{v=1}^M sum_{a in A} [a >= v]. For any fixed threshold v, map elements >= v to 1 and < v to 0. An inserted 1 increases the count of ones c by 1 iff c <= N - X, while an inserted 0 decreases c by 1 iff c > N - X + 1. Thus c = N - X + 1 is an absorbing boundary! Crucially, the final count of 1s depends solely on the total number of inserted 1s j, independent of insertion order: final_c = min(N - X + 1, c_0 + j) if c_0 <= N - X + 1, and max(N - X + 1, c_0 - (K - j)) otherwise.
- Common Reductions: Given a multiset A of N integers in [1, M], repeat K times: insert a uniformly chosen integer in [1, M] and erase the X-th smallest element. Find the sum of multiset element sums across all M^K operation sequences modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc139_d`](../../analysis/AtCoder-arc139_d.md) | D - Priority Queue | 2816 | Given a multiset A of N integers in [1, M], repeat K times: insert a uniformly chosen integer in [1, M] and erase the X-... |
