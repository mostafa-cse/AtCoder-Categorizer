# Fast Walsh Hadamard Transform (FWHT) and its Variations

**Taxonomy Path**: `Math` > `Convolution` > `Fast Walsh Hadamard Transform (FWHT) and its Variations`

## Description
This topic focuses on fast walsh hadamard transform (fwht) and its variations techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For $X = 0$, $f(0) = \sum \lfloor C[i] / 2 \rfloor$. For $X > 0$, values partition into independent pairs $\{i, i \oplus X\}$, so $f(X) = \frac{1}{2} \sum_i \min(C[i], C[i \oplus X])$. Using $\min(a, b) = \sum_{x \ge 1} [a \ge x][b \ge x]$, the sum decomposes into XOR convolutions of indicator vectors $S_x[i] = [C[i] \ge x]$ with themselves. By setting a threshold $K \approx 20$, the first $K$ terms are summed via FWHT in $O(K M 2^M)$ time, and remaining heavy pairs ($C[i] > K$) are corrected directly in $O((N/K)^2)$ time.
- Common Reductions: For each $X \in [0, 2^M - 1]$, find the maximum number of disjoint pairs of cards with bitwise XOR equal to $X$, and output $\sum_{X} f(X) 10^X \pmod{998244353}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc222_e`](../../analysis/AtCoder-arc222_e.md) | E - XOR Matching | 2423 | For each $X \in [0, 2^M - 1]$, find the maximum number of disjoint pairs of cards with bitwise XOR equal to $X$, and out... |
