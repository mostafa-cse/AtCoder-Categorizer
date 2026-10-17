# Floor Sum and Mod Sum of Arithmetic Progression

**Taxonomy Path**: `Number Theory` > `Floor Sum` > `Floor Sum and Mod Sum of Arithmetic Progression`

## Description
This topic focuses on floor sum and mod sum of arithmetic progression techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Rewrite the inequality algebraically:
$(Ak + B) \bmod M > k \iff k + 1 \le Ak + B - M \lfloor \frac{Ak + B}{M} \rfloor \iff \lfloor \frac{Ak + B}{M} \rfloor \le \frac{(A - 1)k + (B - 1)}{M}$.
Since the LHS is an integer, this is equivalent to $\lfloor \frac{Ak + B}{M} \rfloor \le \lfloor \frac{(A - 1)k + (B - 1)}{M} \rfloor$.
Furthermore, the difference $\Delta(k) = \lfloor \frac{Ak + B}{M} \rfloor - \lfloor \frac{(A - 1)k + (B - 1)}{M} \rfloor$ only ever takes values in $\{0, 1\}$. The condition $\Delta(k) \le 0$ means $\Delta(k) = 0$. Hence, the number of valid $k$ is precisely $N - \sum_{k=0}^{N-1} \Delta(k) = N - \text{floor\_sum}(N, M, A, B) + \text{floor\_sum}(N, M, A - 1, B - 1)$. Using generalized floor division and Euclidean floor sum computes each query in $O(\log M)$ time.
- Common Reductions: Given integers $N, M, A, B$ with $1 \le N \le M \le 10^9$ and $0 \le A, B < M$. Across $T \le 3 \times 10^5$ test cases, find the number of integers $0 \le k < N$ such that $(Ak + B) \bmod M > k$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc443_g`](../../analysis/AtCoder-abc443_g.md) | G. Another Mod of Linear Problem | 2268 | Given integers $N, M, A, B$ with $1 \le N \le M \le 10^9$ and $0 \le A, B < M$. Across $T \le 3 \times 10^5$ test cases,... |
