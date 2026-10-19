# Vector Space and XOR Basis

**Taxonomy Path**: `Math` > `Linear Algebra` > `Vector Space and XOR Basis`

## Description
This topic focuses on vector space and xor basis techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For each odd part d, available switches are at levels k = 0..L-1. A bit string B is achievable iff at each step k, choosing bit B_k = 1 leaves available switches M >= 1, giving maximum next carry floor((M - B_k)/2). The set of available switch values at level k consists of at most 2 consecutive integers, allowing an O(L) DP per odd part.
- Common Reductions: Switches with values A_i correspond to polynomial multiplication (1 + x^{A_i}) in F_2[x] mod x^N. Pressing two switches of value X reduces to pressing one switch of value 2X. Distinct switch sets uniquely characterize final sequences B. Grouping by odd parts d = A_i / 2^{v_2(A_i)} splits the problem into independent digit-DP problems on powers of two.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc227_e`](../../analysis/AtCoder-arc227_e.md) | Shift and XOR Switches | 2710 | Switches with values A_i correspond to polynomial multiplication (1 + x^{A_i}) in F_2[x] mod x^N. Pressing two switches ... |
