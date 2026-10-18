# Two Pointers

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Two Pointers`

## Description
This topic focuses on two pointers techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: When balls arrive, an empty box is allocated to color c on its 1st, (K+1)-th, (2K+1)-th ball until M boxes are full. Once b_c boxes are allocated to color c, exactly min(total_count[c], b_c * K) balls of color c are accepted. The set of balls allocating boxes forms a sliding window [L, R) on the doubled array, maintained via two pointers in O(N) amortized time.
- Common Reductions: For all N cyclic rotations of balls into M boxes of capacity K, find total stored balls. A box is allocated when a color reaches 1, K+1, 2K+1, ... balls in the active prefix until M boxes are full, accepting min(total_count[c], b_c * K) balls per color. A two-pointer sliding window maintaining allocated boxes evaluates all shifts in O(N) amortized time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc337_f`](../../analysis/AtCoder-abc337_f.md) | F. Usual Color Ball Problems | 2386 | For all N cyclic rotations of balls into M boxes of capacity K, find total stored balls. A box is allocated when a color... |
