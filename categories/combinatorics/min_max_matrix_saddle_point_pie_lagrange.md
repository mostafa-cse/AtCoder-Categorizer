# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The condition min_i max_j A_{i,j} = max_j min_i A_{i,j} = m holds iff the matrix contains at least one saddle point. By inclusion-exclusion over non-empty subsets of h rows and w columns forming saddle points, the total valid matrices is sum_{h=1}^H sum_{w=1}^W sum_{m=1}^M C(H,h) C(W,w) (-1)^{h+w} m^{h(W-w)} (M+1-m)^{(H-h)w} M^{(H-h)(W-w)}. Viewing F(M) = sum_{m=1}^M f(m) as a polynomial of degree <= HW + 1, Lagrange interpolation computes the result in O(H^2 W log W) time.
- Common Reductions: Minimax equality is equivalent to the existence of a matrix saddle point. Inclusion-exclusion yields a polynomial expression in M summed over m, evaluated via binomial contraction and Lagrange interpolation in O(H^2 W log W) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc230_d`](../../analysis/AtCoder-arc230_d.md) | D. Min Max Matrix | 2395 | Minimax equality is equivalent to the existence of a matrix saddle point. Inclusion-exclusion yields a polynomial expres... |
