# Hamiltonian Path and Cycle

**Taxonomy Path**: `Graph Theory` > `Hamiltonian Path` > `Hamiltonian Path and Cycle`

## Description
This topic focuses on hamiltonian path and cycle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Let $n = \text{ord}(a)$ and $m = \min \{ m \ge 1 \mid b^m \in \langle a \rangle \}$. The generated subgroup has size $n \cdot m$. A Hamiltonian cycle exists iff $n \cdot m = P - 1$. Since $P - 1$ is even, at least one of $n, m$ is even (swap $a, b$ if necessary so $m$ is even). The elements form an $n \times m$ grid $(i, j) \leftrightarrow a^i b^j$. On this grid, traverse rows $1 \dots n-1$ in 2-column serpentine blocks, step to $(0, m-1)$, and return along row 0 to $(0, 0)$.
- Common Reductions: Construct a Hamiltonian cycle on the Cayley graph of $(\mathbb{Z}/P\mathbb{Z})^\times$ with generator set $\{a, a^{-1}, b, b^{-1}\}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc118_d`](../../analysis/AtCoder-arc118_d.md) | D. Hamiltonian Cycle | 2448 | Construct a Hamiltonian cycle on the Cayley graph of $(\mathbb{Z}/P\mathbb{Z})^\times$ with generator set $\{a, a^{-1}, ... |
