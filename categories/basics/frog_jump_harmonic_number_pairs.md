# Harmonic Number

**Taxonomy Path**: `Basics` > `Very Basic Math` > `Harmonic Number`

## Description
This topic focuses on harmonic number techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because the game ends on a $+A$ jump landing at $N - 1$, $A = N - 1 - kC$. The intermediate forward coordinates are $kC$ and reverse coordinates are $N - 1 - kC$. As long as no coordinates collide or overlap with 0, all lotuses are distinct. Collisions only occur when $C$ divides $N - 1$ and $2kC \ge N - 1$.
- Common Reductions: Maximize score by jumping $+A, -B, +A, -B, \dots$ to reach $N - 1$. Let $C = A - B > 0$. The sequence of visited lotuses consists of pairs $(kC, N - 1 - kC)$ for $k = 1, 2, \dots$. A lotus is visited twice if and only if $(N - 1) \bmod C == 0$ and $2kC \ge N - 1$. Iterating over all step sizes $C$ and valid $k$ evaluates all feasible paths in $O(N \log N)$ time using the harmonic series.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc128_f`](../../analysis/AtCoder-abc128_f.md) | F. Frog Jump | 2464 | Maximize score by jumping $+A, -B, +A, -B, \dots$ to reach $N - 1$. Let $C = A - B > 0$. The sequence of visited lotuses... |
