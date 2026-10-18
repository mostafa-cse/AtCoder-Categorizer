# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By PIE over gardens receiving no seedlings: $\sum_{m=0}^N (-1)^{N-m} \binom{N}{m} f(m, A) f(m, B) f(m, C)$, where $f(m, K) = \sum_{k=0}^K \binom{m}{k}$. Using Pascal's identity, $f(m, K) = \sum_{k=0}^K (\binom{m-1}{k} + \binom{m-1}{k-1}) = 2 f(m-1, K) - \binom{m-1}{K}$. This enables $O(1)$ state transitions as $m$ advances.
- Common Reductions: Count the number of ways to plant at most $A$ apple, $B$ banana, and $C$ cherry seedlings across $N$ gardens such that every garden receives at least one seedling and at most one of each kind.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc235_g`](../../analysis/AtCoder-abc235_g.md) | G. Gardens | 2462 | Count the number of ways to plant at most $A$ apple, $B$ banana, and $C$ cherry seedlings across $N$ gardens such that e... |
