# Permutations, Combinations and Basic Counting Problems

**Taxonomy Path**: `Basics` > `Basic Counting` > `Permutations, Combinations and Basic Counting Problems`

## Description
This topic focuses on permutations, combinations and basic counting problems techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Elements whose last operation moved them to the front form a prefix of length L in reverse order of their last touch. Elements moved to the back form a suffix of length R in order of their last touch. The unmoved elements in the middle must be strictly increasing. For s = L + R moved elements, the number of operation sequences is C(s, L) * dp[m][s], where dp[i][j] = dp[i-1][j-1] + 2j * dp[i-1][j].
- Common Reductions: Count operation sequences of moving elements to the front or back to form a target permutation by tracking the suffix of last-touch operations using dynamic programming combined with prefix/suffix combination matching.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc112_e`](../../analysis/AtCoder-arc112_e.md) | Cigar Box | 2659 | Count operation sequences of moving elements to the front or back to form a target permutation by tracking the suffix of... |
