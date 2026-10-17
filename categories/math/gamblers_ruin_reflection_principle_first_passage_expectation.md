# Gambler's Ruin

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Gambler's Ruin`

## Description
This topic focuses on gambler's ruin techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each card drawn from the deck advances a random walk in $(a, b)$ where the hand runs out of draw cards exactly when $b - a = K$ for the first time. The number of paths hitting this absorbing barrier is given by the reflection principle $\binom{a+b-1}{a} - \binom{a+b-1}{a-1}$, while paths never reaching it yield the full deck hand size $B$.
- Common Reductions: A grid walk starts at $(0, 0)$ and makes $A$ horizontal steps and $B$ vertical steps. Compute the number of paths that reach $(A, B)$ without the number of vertical steps ever exceeding horizontal steps by $K$ or more, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc223_d`](../../analysis/AtCoder-arc223_d.md) | D. Xpectation of Cards in Hand with Laboratory | 2281 | A grid walk starts at $(0, 0)$ and makes $A$ horizontal steps and $B$ vertical steps. Compute the number of paths that r... |
