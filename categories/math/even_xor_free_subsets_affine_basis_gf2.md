# Vector Space and XOR Basis

**Taxonomy Path**: `Math` > `Linear Algebra` > `Vector Space and XOR Basis`

## Description
This topic focuses on vector space and xor basis techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any subset T, sum_{x in T} (x, 1) = (XOR_{x in T} x, |T| mod 2). Thus an even-sized subset with XOR sum 0 corresponds exactly to a linear dependency among the augmented vectors! The size of S is bounded by N + 1, and the count of linearly independent sets of size k has a closed product form.
- Common Reductions: Count subsets S of GF(2)^N where no non-empty even subset has XOR sum 0 by mapping each element x to the vector (x, 1) in GF(2)^(N+1) and recognizing that the condition is equivalent to linear independence in GF(2)^(N+1).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc146_c`](../../analysis/AtCoder-arc146_c.md) | Even XOR | 2428 | Count subsets S of GF(2)^N where no non-empty even subset has XOR sum 0 by mapping each element x to the vector (x, 1) i... |
