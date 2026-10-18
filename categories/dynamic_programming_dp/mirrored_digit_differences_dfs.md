# Digit DP

**Taxonomy Path**: `Dynamic Programming (DP)` > `Digit DP` > `Digit DP`

## Description
This topic focuses on digit dp techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Since $x_i \in [-9, 9]$, there are at most two candidate values for $x_i$ satisfying $x_i \equiv -D \pmod{10}$. Once $x_i$ is chosen, $(D - x_i (10^{r - l} - 1))$ is divisible by 10, so dividing by 10 advances the problem to the next inner digit layer. The number of digit pairs $(d_l, d_r)$ achieving difference $x_i$ is easily counted. With at most 2 choices per layer and depth $\le 10$, the recursion visits $\le 1024$ states per length $L \in [2, 18]$.
- Common Reductions: Count positive integers $N$ such that $\text{rev}(N) - N = D$ for $1 \le D < 10^9$. For a fixed length $L$, expanding the decimal expansion expresses $\text{rev}(N) - N = \sum_{i=0}^{\lfloor (L-1)/2 \rfloor} x_i (10^{L-1-i} - 10^i) = D$, where $x_i = d_{L-1-i} - d_i \in [-9, 9]$. Working from the outside layer inward, at each step $x_i$ is uniquely constrained modulo 10: $x_i \equiv -D \pmod{10}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc075_d`](../../analysis/AtCoder-arc075_d.md) | F. Mirrored | 2549 | Count positive integers $N$ such that $\text{rev}(N) - N = D$ for $1 \le D < 10^9$. For a fixed length $L$, expanding th... |
