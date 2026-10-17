# Hamiltonian Path and Cycle

**Taxonomy Path**: `Graph Theory` > `Hamiltonian Path` > `Hamiltonian Path and Cycle`

## Description
This topic focuses on hamiltonian path and cycle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each step flips 1 bit, changing the parity of popcount. Since a Hamiltonian path has 2^N - 1 steps (an odd number of steps), popcount(A ^ B) must be odd for a solution to exist. If odd, we can recursively divide the N-cube along a differing bit k, choose an intermediate stepping pair differing only in bit k, and solve two independent subproblems of dimension N - 1.
- Common Reductions: Find a Hamiltonian path on the N-dimensional hypercube starting at A and ending at B where each step changes exactly one bit.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc031_c`](../../analysis/AtCoder-agc031_c.md) | Differ by 1 Bit | 2217 | Find a Hamiltonian path on the N-dimensional hypercube starting at A and ending at B where each step changes exactly one... |
