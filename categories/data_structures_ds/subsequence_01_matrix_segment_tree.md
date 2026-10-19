# Segment Tree (Point Update Range Query)

**Taxonomy Path**: `Data Structures (DS)` > `Segment Tree` > `Segment Tree (Point Update Range Query)`

## Description
This topic focuses on segment tree (point update range query) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For '0': dp_0' = dp_0 + dp_1 + 1, dp_1' = dp_1. Matrix: [[1, 1, 1], [0, 1, 0], [0, 0, 1]]. For '1': dp_0' = dp_0, dp_1' = dp_0 + dp_1 + 1. Matrix: [[1, 0, 0], [1, 1, 1], [0, 0, 1]]. For '?': sum of both matrices. Matrix multiplication is associative, allowing a standard point-update segment tree over 3 x 3 matrices.
- Common Reductions: Count non-empty distinct subsequences of a ternary string S in {0, 1, ?}^N under point updates. Counting distinct subsequences is equivalent to tracking DP state vector (dp_0, dp_1, 1)^T. Each character '0', '1', '?' corresponds to a 3 x 3 transition matrix. A segment tree maintaining matrix products processes point updates and queries in O(log N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc246_h`](../../analysis/AtCoder-abc246_h.md) | 01? Queries | 2677 | Count non-empty distinct subsequences of a ternary string S in {0, 1, ?}^N under point updates. Counting distinct subseq... |
