# The XOR Trick

**Taxonomy Path**: `Basics` > `Bit Manipulation` > `The XOR Trick`

## Description
This topic focuses on the xor trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each insertion operation replaces elements with XOR combinations of contiguous blocks. By linear algebra over GF(2), the set of all achievable elements forms an XOR vector space. Maintaining the linear basis of contiguous blocks allows fast determination of reachable states and optimization of the total XOR sum.
- Common Reductions: Given an array A and operations that insert XOR sums of subarrays, determine reachable values and maximize the XOR sum of subsets.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc203_d`](../../analysis/AtCoder-arc203_d.md) | D. Insert XOR | 2549 | Given an array A and operations that insert XOR sums of subarrays, determine reachable values and maximize the XOR sum o... |
