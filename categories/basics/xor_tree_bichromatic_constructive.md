# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If $N$ is a power of 2, the MSB of $N$ appears only in vertices $N$ and $N+N$, so the path between them cannot form an XOR sum of $N$, making construction impossible. For odd $N$ or non-power-of-2 even $N$, pairs $(2k, 2k+1)$ satisfy $2k \oplus (2k+1) = 1$, allowing a star hub at 1 to achieve paths of XOR $x$ for all $x$.
- Common Reductions: Construct a tree of $2N$ vertices with weights $1 \dots N, 1 \dots N$ where the path between $i$ and $N+i$ has XOR sum $i$. Star topology around 1 with pairs $(2k, 2k+1)$ and 3-basis decomposition solves for all non-powers of 2 in $O(N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc035_c`](../../analysis/AtCoder-agc035_c.md) | C. Skolem XOR Tree | 2332 | Construct a tree of $2N$ vertices with weights $1 \dots N, 1 \dots N$ where the path between $i$ and $N+i$ has XOR sum $... |
