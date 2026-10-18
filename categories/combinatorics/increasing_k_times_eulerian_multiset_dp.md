# Product Trick

**Taxonomy Path**: `Combinatorics` > `Techniques` > `Product Trick`

## Description
This topic focuses on product trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When numbers are sorted and inserted in non-decreasing order, each group of identical elements $x$ with frequency $cnt$ can be placed into existing spaces. If an element is inserted into an existing 'ascent' slot, the number of ascents does not increase. If inserted into a non-ascent slot, it creates a new ascent. This generalizes Eulerian numbers to multisets via polynomial DP.
- Common Reductions: Count permutations of a multiset $A$ having exactly $K$ positions where $P_i < P_{i+1}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc267_g`](../../analysis/AtCoder-abc267_g.md) | G - Increasing K Times | 2561 | Count permutations of a multiset $A$ having exactly $K$ positions where $P_i < P_{i+1}$.... |
