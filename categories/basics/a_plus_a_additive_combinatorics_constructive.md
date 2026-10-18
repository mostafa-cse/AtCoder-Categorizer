# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By analyzing small cases and sumset parity constraints, a solution is impossible if and only if: (1) $K = 2$ and $M$ is odd, or (2) $K = 4$ and $M$ is not divisible by 4. For all other $(M, K)$, exact arithmetic progression sub-blocks construct the target sumset count directly: $K = M \implies A = \{0, 1, \dots, M-1\}$; $K = 2 \implies \{0, M/2\}$; $K = 4 \implies \{0, M/4, 2M/4, 3M/4\}$; odd $K \implies \{0, 1, \dots, (K-1)/2\}$; even $K \ge 6 \implies \{0, 2, 3, \dots, K/2\}$.
- Common Reductions: Construct a sequence $A \subseteq \mathbb{Z}_M$ such that the number of distinct pairwise sumsets $|(A + A) \bmod M|$ equals exactly $K$, or determine that none exists.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc200_d`](../../analysis/AtCoder-arc200_d.md) | D - |A + A| | 2474 | Construct a sequence $A \subseteq \mathbb{Z}_M$ such that the number of distinct pairwise sumsets $|(A + A) \bmod M|$ eq... |
