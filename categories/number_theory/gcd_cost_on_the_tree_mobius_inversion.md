# Mobius Function and Mobius Inversion

**Taxonomy Path**: `Number Theory` > `Multiplicative Functions` > `Mobius Function and Mobius Inversion`

## Description
This topic focuses on mobius function and mobius inversion techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any connected tree component $C$, the sum of distances between all pairs of nodes is $\sum_{e \in E_C} sz(e) \cdot (|C| - sz(e))$, where $sz(e)$ is the size of one of the subtrees formed by deleting edge $e$. By building induced subgraphs for each $d$ in $O(\sum_{v} d(A_v)) = O(N \log \max A)$, we compute subtree sizes via BFS/DFS and accumulate path distance sums in $O(N \log \max A)$ total time.
- Common Reductions: For all pairs of vertices $(u, v)$ on a tree, compute the sum over all simple paths of $\text{dist}(u, v) \cdot \gcd(\text{path\_nodes})$. Expressing $\gcd(X) = \sum_{d \mid X} \phi(d)$ transforms the sum into $\sum_{d} \phi(d) \sum_{u < v, \forall w \in \text{path}(u, v): d \mid A_w} \text{dist}(u, v)$. A path contains only multiples of $d$ if and only if $u$ and $v$ belong to the same connected component of the induced subgraph $V_d = \{v : d \mid A_v\}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc248_g`](../../analysis/AtCoder-abc248_g.md) | G. GCD cost on the tree | 2514 | For all pairs of vertices $(u, v)$ on a tree, compute the sum over all simple paths of $\text{dist}(u, v) \cdot \gcd(\te... |
