# Fast Walsh Hadamard Transform (FWHT) and its Variations

**Taxonomy Path**: `Math` > `Convolution` > `Fast Walsh Hadamard Transform (FWHT) and its Variations`

## Description
This topic focuses on fast walsh hadamard transform (fwht) and its variations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In Nim, the first player has a winning strategy if and only if the XOR sum of the heap sizes is non-zero. The total number of sequences of length M is K^M, so the total number of sequences of length 1 <= M <= N is sum_{M=1}^N K^M. To find the number of losing sequences, we must count the number of sequences of length M whose XOR sum is exactly 0. Let P be the indicator vector of the K allowed integers in the group (Z_2)^16 (since A_i < 2^16). The XOR convolution power P^{(*M)} gives the distribution of XOR sums of M choices. By applying the Fast Walsh-Hadamard Transform (FWHT), convolution becomes pointwise multiplication: FWHT(P^{(*M)}) = FWHT(P)^M. Summing over 1 <= M <= N in the frequency domain yields sum_{M=1}^N v^M = v(v^N - 1)/(v - 1) if v != 1, or N if v = 1. Applying inverse FWHT yields the exact number of zero-XOR configurations in O(V log V) time where V = 2^16.
- Common Reductions: There are K integers A_1, ..., A_K. We choose an integer M between 1 and N, and then choose a sequence of M integers from the A_i. A game of Nim is played with M heaps of sizes corresponding to the chosen sequence. Find the number of ways to choose the sequence such that Takahashi (the first player) has a winning strategy, modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc212_h`](../../analysis/AtCoder-abc212_h.md) | H - Nim Counting | 2741 | There are K integers A_1, ..., A_K. We choose an integer M between 1 and N, and then choose a sequence of M integers fro... |
