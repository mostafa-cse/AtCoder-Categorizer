# Sieve, Prime Factorization and Divisors

**Taxonomy Path**: `Number Theory` > `Primes and Divisors` > `Sieve, Prime Factorization and Divisors`

## Description
This topic focuses on sieve, prime factorization and divisors techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Constructing forward is hard, but constructing backwards is greedy and deterministic. Element $x$ can be placed last iff $x \nmid \text{LCM}(S \setminus \{x\}) \iff \text{LCM}_{s \in S \setminus \{x\}} \text{GCD}(x, s) < x$. Since $\text{GCD}(x, s)$ divides $x$, the LCM of these GCDs fits inside $x \le 10^{18}$, avoiding overflow.
- Common Reductions: Find a permutation of $A$ such that prefix LCMs are strictly increasing, or determine that none exists.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc122_e`](../../analysis/AtCoder-arc122_e.md) | E. Increasing LCMs | 2535 | Find a permutation of $A$ such that prefix LCMs are strictly increasing, or determine that none exists.... |
