# Digit DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Digit DP` > `Digit DP`

## Description
This topic focuses on digit dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Once a prefix is strictly less than N, choosing one of the c existing digits maintains count c (c choices), while choosing an unused digit increases count to c + 1 (16 - c choices). The single tight prefix is maintained with a bitmask.
- Common Reductions: Count integers 1 <= x <= N (length up to 2e5 hex digits) having exactly K distinct hex digits. By digit symmetry, non-tight prefixes only need to track the count c in [0, 16] of distinct digits used so far, reducing non-tight DP to 17 states per position in O(16 * |N|) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc194_f`](../../analysis/AtCoder-abc194_f.md) | F. Digits Paradise in Hexadecimal | 2197 | Count integers 1 <= x <= N (length up to 2e5 hex digits) having exactly K distinct hex digits. By digit symmetry, non-ti... |
