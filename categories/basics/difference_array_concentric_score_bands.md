# Difference Array

**Taxonomy Path**: `Basics` > `More Techniques` > `Difference Array`

## Description
This topic focuses on difference array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Arrows should be placed at exact intervals of $D$ to remain as close to 0 as possible: $x_j(k) = A + k + j D$ for $j = 0, \dots, N-1$, where $A = -\lfloor \frac{ND}{2} \rfloor$ and shift $k \in [0, D-1]$.
As the shift $k$ increases from $k$ to $k+1$, all arrows shift right by $+1$. An arrow's score only changes when it crosses a concentric ring boundary $\pm r_i$. For each boundary point $B$, at most one arrow $j = \lfloor \frac{B - A - rem}{D} \rfloor$ crosses $B$ at $k = (B - A) \bmod D$. Using a difference array of size $D$, we add score changes for all $2M$ boundaries in $O(M)$ time, and find the maximum total score in $O(M + D)$ time via prefix sums.
- Common Reductions: Shoot $N$ arrows into concentric scoring bands $[-r_i, r_i]$ with scores $s_i$ centered at 0. Any two arrows must be separated by distance $\ge D$ ($D \le 10^6$). Find the maximum total score obtainable.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc131_d`](../../analysis/AtCoder-arc131_d.md) | D. AtArcher | 2271 | Shoot $N$ arrows into concentric scoring bands $[-r_i, r_i]$ with scores $s_i$ centered at 0. Any two arrows must be sep... |
