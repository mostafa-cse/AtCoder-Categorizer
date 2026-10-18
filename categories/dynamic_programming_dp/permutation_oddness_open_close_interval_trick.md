# Open and Close Interval Trick

**Taxonomy Path**: `Dynamic Programming (DP)` > `More Tricks` > `Open and Close Interval Trick`

## Description
This topic focuses on open and close interval trick techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Use the Open and Close Interval Trick (Profile DP). Process positions $i = 1 \dots N$. At boundary $i$, suppose $j$ indices $x \le i$ have not yet been assigned their values $P_x > i$, and symmetrically $j$ values $y \le i$ have not yet been matched to indices $P_z = y$ with $z > i$. Crossing from $i$ to $i + 1$, each of these $2j$ open lines contributes $+2j$ to the total oddness.
- Common Reductions: Count permutations $P$ of $1 \dots N$ with 'oddness' $\sum_{i=1}^N |i - P_i| = K$. Since $|i - P_i| = \max(i, P_i) - \min(i, P_i)$, think of each pair $(i, P_i)$ as an interval between $i$ and $P_i$. The oddness is equal to $2 \times \sum_{i=1}^{N-1} (\text{number of intervals crossing boundary } i + 0.5)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc134_f`](../../analysis/AtCoder-abc134_f.md) | F. Permutation Oddness | 2532 | Count permutations $P$ of $1 \dots N$ with 'oddness' $\sum_{i=1}^N |i - P_i| = K$. Since $|i - P_i| = \max(i, P_i) - \mi... |
