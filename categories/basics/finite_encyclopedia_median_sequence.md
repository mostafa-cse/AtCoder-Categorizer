# Permutations, Combinations and Basic Counting Problems

**Taxonomy Path**: `Basics` > `Basic Counting` > `Permutations, Combinations and Basic Counting Problems`

## Description
This topic focuses on permutations, combinations and basic counting problems techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Stepping one step backwards in lexicographical order: if the sequence ends in 1, pop the 1; otherwise, decrement the last element and append copies of K until length reaches N. This amortizes to O(1) per step.
- Common Reductions: Finding the ceil(X/2)-th lexicographically smallest sequence of length 1..N with elements in 1..K. If K is even, exactly half of all sequences start with <= K/2, so the median is K/2 followed by N-1 copies of K. If K is odd, sequences symmetric under x -> K+1-x are precisely the N prefixes of (K+1)/2... (K+1)/2, placing that sequence at rank X/2 + N/2. The median is reached by stepping backwards floor(N/2) times in lexicographical order in O(N) amortized time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc084_c`](../../analysis/AtCoder-arc084_c.md) | Finite Encyclopedia of Integer Sequences | 2703 | Finding the ceil(X/2)-th lexicographically smallest sequence of length 1..N with elements in 1..K. If K is even, exactly... |
