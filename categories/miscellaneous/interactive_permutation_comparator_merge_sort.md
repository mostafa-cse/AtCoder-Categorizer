# Interactive Problems

**Taxonomy Path**: `Miscellaneous` > `Interactive Problems` > `Interactive Problems`

## Description
This topic focuses on interactive problems techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: First, locate the index $x$ where $P_x = 1$ in $N-1$ queries. Start with candidate $x = 1$. For $i = 2 \dots N$, query '? i i x' ($P_i + P_i > P_x$). If 'No', then $2 P_i \le P_x \implies P_i < P_x$, so update candidate $x \leftarrow i$. When $i$ hits the true position of $1$, $2(1) \le P_x$ is 'No' (since $P_x \ge 2$), so $x$ switches to the position of $1$, and never changes again since $2 P_k > 1$ for all other elements.
Once the index $x$ with $P_x = 1$ is known, querying '? b x a' tests $P_b + 1 > P_a \iff P_b \ge P_a$. Since all elements are distinct, this provides a strict comparison oracle between any two elements $P_a$ and $P_b$. Using standard merge sort on the remaining $N-1$ elements takes at most $(N-1) \lceil \log_2 (N-1) \rceil \le 22,000$ queries, well within the 25,000 query limit.
- Common Reductions: An unknown permutation $P$ of length $N \le 2000$ is hidden. We can ask at most 25,000 queries of the form '? i j k', asking if $P_i + P_j > P_k$. Recover the entire permutation $P$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc154_d`](../../analysis/AtCoder-arc154_d.md) | D. A + B > C ? | 2265 | An unknown permutation $P$ of length $N \le 2000$ is hidden. We can ask at most 25,000 queries of the form '? i j k', as... |
