# Subset Sum Problem using Generating Functions

**Taxonomy Path**: `Math` > `Polynomial` > `Subset Sum Problem using Generating Functions`

## Description
This topic focuses on subset sum problem using generating functions techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Because A_i <= 10, there are only 10 distinct value types. The polynomial for each value v is (1 +- x^v)^c_v, which is sparse and can be evaluated using binomial coefficients up to degree M / v. Multiplying these 10 polynomials via NTT takes O(M log M) time.
- Common Reductions: Count subsets of odd cardinality with sum M by constructing the generating functions P(x) = prod(1 + x^v)^c_v and Q(x) = prod(1 - x^v)^c_v over the small value domain A_i in [1, 10], multiplying via divide-and-conquer NTT, and extracting (P_M - Q_M) / 2 mod 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc267_h`](../../analysis/AtCoder-abc267_h.md) | Ex. Odd Sum | 2422 | Count subsets of odd cardinality with sum M by constructing the generating functions P(x) = prod(1 + x^v)^c_v and Q(x) =... |
