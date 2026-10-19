# Online FFT / NTT

**Taxonomy Path**: `Math` > `Convolution` > `Online FFT / NTT`

## Description
This topic focuses on online fft / ntt techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The sum sum_{i+j < n} F_i * F_j is the prefix sum of the self-convolution C = F * F. Since each F_n requires C_{n-1}, which depends on F_0..F_{n-1}, we can compute this recurrence using online relaxed convolution with NTT. Relaxed multiplication feeds each newly determined coefficient F_k into an ongoing convolution engine that maintains partial products using power-of-2 doubling, making C_{n-1} available just in time to determine F_n.
- Common Reductions: Given sequence A of length N, compute F_1..F_N where F_0 = 1 and F_n = A_n * sum_{i+j < n} F_i * F_j modulo 998244353.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc315_h`](../../analysis/AtCoder-abc315_h.md) | Ex - Typical Convolution Problem | 2807 | Given sequence A of length N, compute F_1..F_N where F_0 = 1 and F_n = A_n * sum_{i+j < n} F_i * F_j modulo 998244353.... |
