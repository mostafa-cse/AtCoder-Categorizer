# Principle of Inclusion and Exclusion (PIE)

**Taxonomy Path**: `Combinatorics` > `Inclusion Exclusion` > `Principle of Inclusion and Exclusion (PIE)`

## Description
This topic focuses on principle of inclusion and exclusion (pie) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The total polynomial $Q(x) = \prod_{i} P_i(x) = \sum_{k=0}^N a_k x^k$ has coefficient $a_k$ equal to the number of ways to choose $k$ monochromatic pairs. The remaining $2N - 2k$ people are paired arbitrarily in $(2N - 2k - 1)!!$ ways. By PIE, each monochromatic pair carries weight $-1$, giving $\sum_{k=0}^N (-1)^k a_k (2N - 2k - 1)!! \pmod{998244353}$.
- Common Reductions: Given $2N$ people with heights $h_i$, form $N$ disjoint pairs such that no pair contains two people of the same height. Group people by identical heights: suppose group $i$ has size $c_i$. Total unrestricted pairings of $2K$ people is $(2K - 1)!!$. By the Principle of Inclusion and Exclusion, if we choose $k$ monochromatic pairs across all groups, each group $i$ with $j$ monochromatic pairs contributes $c_i! / ((c_i - 2j)! 2^j j!) x^j$. Multiply these group polynomials using Divide and Conquer NTT.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abl_f`](../../analysis/AtCoder-abl_f.md) | F. Heights and Pairs | 2545 | Given $2N$ people with heights $h_i$, form $N$ disjoint pairs such that no pair contains two people of the same height. ... |
