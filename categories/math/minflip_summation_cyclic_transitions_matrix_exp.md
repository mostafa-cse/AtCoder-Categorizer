# Matrix Exponentiation

**Taxonomy Path**: `Math` > `Matrices` > `Matrix Exponentiation`

## Description
This topic focuses on matrix exponentiation techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Each cyclic transition $S_i \ne S_{i+1}$ contributes independently. If both characters are fixed, contribution is $1$ if $S_i \ne S_{i+1}$ else $0$. If one or both characters are '?', the probability of differing is $1/2$. Summing across all $|S|$ boundaries in one copy and multiplying by $K \cdot 2^{K q - 1} \pmod{10^9 + 7}$ evaluates the exact total in $O(|S| + \log K)$ time.
- Common Reductions: Given string $S$ repeated $K$ times into $T$, sum over all $2^{K q}$ '?' replacements the minimum range inversions to make all characters equal. For any binary string, the minimum operations to make all characters equal is exactly $c_{circ} / 2$, where $c_{circ}$ is the number of cyclic transitions $T_i \ne T_{i+1 \pmod{|T|}}$ along the cyclic string! By linearity of expectation, the sum is $K \times \sum_{i=1}^{|S|} \mathbb{P}(S_i \ne S_{i+1}) \times 2^{K q - 1}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc200_f`](../../analysis/AtCoder-abc200_f.md) | F. Minflip Summation | 2556 | Given string $S$ repeated $K$ times into $T$, sum over all $2^{K q}$ '?' replacements the minimum range inversions to ma... |
