# 2 SAT

**Taxonomy Path**: `Graph Theory` > `Satisfiability` > `2 SAT`

## Description
This topic focuses on 2 sat techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Two numbers are coprime iff they share no prime factor. Each number <= 2 * 10^6 has at most 7 distinct prime factors. For each prime p, at most one card can select a side divisible by p. This "at most one" constraint across multiple choices is mapped to 2-SAT using prefix implication chains, keeping total 2-SAT vertices and edges O(N).
- Common Reductions: Given N cards with numbers A_i and B_i, choose one side for each card such that all chosen numbers are pairwise coprime.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc210_f`](../../analysis/AtCoder-abc210_f.md) | F - Coprime Solitaire | 2632 | Given N cards with numbers A_i and B_i, choose one side for each card such that all chosen numbers are pairwise coprime.... |
