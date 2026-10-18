# Two Pointers

**Taxonomy Path**: `Basics` > `Leveraging Monotonicity` > `Two Pointers`

## Description
This topic focuses on two pointers techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because every bag contributes one ball to Blue, finding the minimum range $[L, R]$ covering at least one ball from each bag is an exact equivalent to the shortest subarray containing all $N$ colors. Two pointers in $O(N \log N)$ over the $2N$ sorted values determines the optimal interval.
- Common Reductions: Each bag has two balls $(x_i, y_i)$. We paint one red and the other blue to minimize $(R_{max} - R_{min}) \times (B_{max} - B_{min})$. In Case 1, global minimum and global maximum are different colors: assigning the smaller of each bag to Red and larger to Blue is optimal. In Case 2, global minimum and maximum are the same color (say Red), so $R_{max} - R_{min} = ALL_{max} - ALL_{min}$ is fixed, and the remaining balls in Blue must contain exactly one ball from each bag, which is solved by sliding a two-pointer window over the sorted $2N$ values.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc073_c`](../../analysis/AtCoder-arc073_c.md) | E. Ball Coloring | 2434 | Each bag has two balls $(x_i, y_i)$. We paint one red and the other blue to minimize $(R_{max} - R_{min}) \times (B_{max... |
