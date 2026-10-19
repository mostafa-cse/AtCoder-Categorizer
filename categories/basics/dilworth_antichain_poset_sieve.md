# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Partition [1, 2M] into M chains according to their odd part o in {1, 3, ..., 2M - 1}. By Dilworth's Theorem, any antichain under divisibility contains at most one element per chain, so an antichain of size M must pick exactly one power of 2 for each odd part. Divisibility constraints between odd parts o and multiples (2k+1)o restrict the exponent of 2 to an interval [min_pow[o], max_pow[o]]. Sieve propagation yields valid intervals for all odd parts.
- Common Reductions: Given an array A of N integers from [1, 2M], determine for each element A_i whether there exists a subset of size M containing A_i such that no element divides another.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc141_d`](../../analysis/AtCoder-arc141_d.md) | D. Non-divisible Set | 2890 | Given an array A of N integers from [1, 2M], determine for each element A_i whether there exists a subset of size M cont... |
