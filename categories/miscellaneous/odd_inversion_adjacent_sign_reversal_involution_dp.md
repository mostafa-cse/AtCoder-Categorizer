# Inversions

**Taxonomy Path**: `Miscellaneous` > `General` > `Inversions`

## Description
This topic focuses on inversions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let C and D be counts of sequences with even and odd inversions. Then C + D = prod A_i, while C - D = X_N under sign-reversing involution: swapping adjacent elements B_{i-1} != B_i within [1, A_{i-1}] cancels out opposite parities, leaving only B_{i-1} = B_i (contributing A_{i-1} X_{i-2}) and B_i > A_{i-1} (contributing (A_i - A_{i-1}) X_{i-1}).
- Common Reductions: The difference between even and odd inversion sequences satisfies X_i = (A_i - A_{i-1}) X_{i-1} + A_{i-1} X_{i-2} by adjacent element swapping involution. Solving this linear recurrence yields the exact odd count in O(N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc231_e`](../../analysis/AtCoder-arc231_e.md) | E. Odd Inversion | 2393 | The difference between even and odd inversion sequences satisfies X_i = (A_i - A_{i-1}) X_{i-1} + A_{i-1} X_{i-2} by adj... |
