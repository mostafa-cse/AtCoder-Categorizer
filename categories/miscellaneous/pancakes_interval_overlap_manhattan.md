# Manhattan <> Chebyshev

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Manhattan <> Chebyshev`

## Description
This topic focuses on manhattan <> chebyshev techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Reversing $A[l \dots r]$ changes only two boundary transitions. Prefix reversals ($l = 1$) and suffix reversals ($r = N$) are evaluated in $O(N)$ time. For interior reversals $1 < l < r < N$, the ugliness decrease is $2 \times \text{length}(I_1 \cap I_2)$ where $I_1$ and $I_2$ are intervals of transitions with the same direction (both increasing or both decreasing). Finding maximum interval overlap is solved via sweep-line in $O(N \log N)$.
- Common Reductions: Reverse at most one contiguous subarray $A[l \dots r]$ to minimize total ugliness $\sum_{i=1}^{N-1} |A_{i+1} - A_i|$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc119_e`](../../analysis/AtCoder-arc119_e.md) | E. Pancakes | 2502 | Reverse at most one contiguous subarray $A[l \dots r]$ to minimize total ugliness $\sum_{i=1}^{N-1} |A_{i+1} - A_i|$.... |
