# Sliding Window Technique

**Taxonomy Path**: `Basics` > `More Techniques` > `Sliding Window Technique`

## Description
This topic focuses on sliding window technique techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each interval shuffle operation allows arbitrary rearrangement of characters within [l_i, r_i]. By computing the cumulative max-reach interval R[i] covering prefix i, the count of 1s in prefix i, denoted c_i, is strictly bounded: max(c_{i-1}, ones(R[i]) - (R[i] - i)) <= c_i <= min(c_{i-1} + 1, ones(R[i])). Dynamic programming over prefix index i and current 1-count c_i with sliding window state optimization counts all valid binary sequences.
- Common Reductions: Count distinct binary strings achievable after applying interval shuffle operations by tracking the cumulative count of 1s in the prefix under sliding-window reachability constraints.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc065_d`](../../analysis/AtCoder-arc065_d.md) | Shuffling | 2652 | Count distinct binary strings achievable after applying interval shuffle operations by tracking the cumulative count of ... |
