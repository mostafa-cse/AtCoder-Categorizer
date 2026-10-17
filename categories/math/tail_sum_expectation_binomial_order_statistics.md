# Probabilities and Expected Values

**Taxonomy Path**: `Math` > `Probabilities and Expected Values` > `Probabilities and Expected Values`

## Description
This topic focuses on probabilities and expected values techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: A_K >= x if and only if the total count of elements strictly less than x is at most K - 1. Fixed non-zero elements contribute a deterministic count C_{< x}. The remaining Z zeros independently land in [1, x-1] with probability p = (x-1)/M. The count of zeros < x follows a Binomial distribution B(Z, p), evaluated in O(Z) per x.
- Common Reductions: Sequence A has zeros replaced uniformly at random with integers in 1..M. Compute the expected value of the K-th smallest element of sorted A modulo 998244353 using the tail sum formula E[X] = sum_{x=1}^M P(X >= x).

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| `[problem:AtCoder-abc295_e]` | Kth Number | 2157 | Sequence A has zeros replaced uniformly at random with integers in 1..M. Compute the expected value of the K-th smallest... |
