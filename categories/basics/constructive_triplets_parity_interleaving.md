# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Comparing the minimum sum of $2N$ smallest elements with the maximum sum of $N$ largest elements yields the necessary condition $K \le \lfloor (N+1)/2 \rfloor$. This condition is also sufficient: partition the numbers into $A = [K, K+N-1]$, $B = [K+N, K+2N-1]$, $C = [K+2N, K+3N-1]$. Splitting $A$ and $B$ into sizes $L_1 = \lfloor(N+1)/2\rfloor$ and $L_2 = N - L_1$ and interleaving parity pairs generates every target in $C$ with $a_i + b_i \le c_i$.
- Common Reductions: Determine if the $3N$ integers $K, K+1, \dots, K+3N-1$ can be partitioned into $N$ triplets $(a_i, b_i, c_i)$ such that $a_i + b_i \le c_i$ for all $i$. If possible, construct the partition; otherwise output -1.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-nikkei2019_2_qual_e`](../../analysis/AtCoder-nikkei2019_2_qual_e.md) | E. Non-triangular Triplets | 2257 | Determine if the $3N$ integers $K, K+1, \dots, K+3N-1$ can be partitioned into $N$ triplets $(a_i, b_i, c_i)$ such that ... |
