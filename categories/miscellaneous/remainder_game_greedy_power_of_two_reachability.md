# Exchange Arguments

**Taxonomy Path**: `Miscellaneous` > `Greedy Algorithms` > `Exchange Arguments`

## Description
This topic focuses on exchange arguments techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Moduli k > 50 are useless since all values are <= 50. Because cost is sum of 2^k, choosing 2^k is more expensive than any combination of smaller powers sum_{j < k} 2^j < 2^k. Thus, a greedy high-to-low elimination strategy is optimal. Reachability on the 51-node directed graph (u -> u mod m for allowed m) is checked in O(50 * V^2).
- Common Reductions: Transform array a into b using operations v <- v mod k at cost 2^k. Since costs are powers of 2, minimizing the sum corresponds to lexicographically minimizing the set of chosen moduli from largest to smallest. Greedily attempt to drop k from 50 down to 1, retaining k iff removing it destroys reachability from a_i to b_i.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc022_c`](../../analysis/AtCoder-agc022_c.md) | C. Remainder Game | 2176 | Transform array a into b using operations v <- v mod k at cost 2^k. Since costs are powers of 2, minimizing the sum corr... |
