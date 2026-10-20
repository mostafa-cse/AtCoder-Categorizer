# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Formulate as strings of A, B, X. Using the reflection principle across the diagonal, subtracting paths that violate the prefix condition requires tracking whether the violation step is followed by BB or BX. The base function f(a, b, x) counts arrangements without AA and without BB using stars and bars / PIE on adjacent pairs: f(a, b, x) = \sum_{k=0}^{a-1} \binom{a-1}{k} \binom{x+1}{a-k} \binom{a+x+1-k}{b-k}. The total valid strings is f(A, B, x) - f(B-1, A, x) - f(B-1, A, x-1) - f(B-1, A+1, x-1).
- Common Reductions: Count the number of rock-paper-scissors sequences of length N with A wins for Alice, B wins for Bob, and X = N - A - B draws such that Alice's cumulative wins are always >= Bob's wins, and neither player wins twice consecutively without an intervening draw.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc070_c`](../../analysis/AtCoder-agc070_c.md) | C - No Streak | 2983 | Count the number of rock-paper-scissors sequences of length N with A wins for Alice, B wins for Bob, and X = N - A - B d... |
