# Fast Fourier Transform (FFT)

**Taxonomy Path**: `Math` > `Convolution` > `Fast Fourier Transform (FFT)`

## Description
This topic focuses on fast fourier transform (fft) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The bitwise OR sum decomposes linearly across the 5 independent bit positions 0 <= bit < 5. For each bit, x_i | y_j = 1 - u_i * v_j where u_i = 1 - x_i and v_j = 1 - y_j. The sum sum_i u_i * v_{(i+k)%N} is a cyclic cross-correlation, computed by reversing u and convolving with duplicated v (length 2N) via NTT in O(N log N) time.
- Common Reductions: Maximize sum_{i=0}^{N-1} (A_i | B_{(i+k)%N}) over all cyclic shifts k in [0, N-1]. Decompose numbers into 5 bits. For each bit b, x | y = 1 - (1 - x)(1 - y). Compute cyclic cross-correlations of (1 - A) and (1 - B) across all shifts using Number Theoretic Transform (NTT) under modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc291_g`](../../analysis/AtCoder-abc291_g.md) | G. OR Sum | 2176 | Maximize sum_{i=0}^{N-1} (A_i | B_{(i+k)%N}) over all cyclic shifts k in [0, N-1]. Decompose numbers into 5 bits. For ea... |
