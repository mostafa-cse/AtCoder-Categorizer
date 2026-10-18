# Chromatic Number

**Taxonomy Path**: `Graph Theory` > `Graph Coloring` > `Chromatic Number`

## Description
This topic focuses on chromatic number techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The rolling hash condition hash(A[L..R]) != 0 mod P is equivalent to (H_R - H_{L-1} B^{R-L+1}) != 0 mod P. Multiplying by B^{-R} yields y_R != y_{L-1} mod P where y_k = H_k B^{-k} mod P. Since any prefix hash assignment is achievable, the problem is equivalent to proper vertex coloring of the difference graph on N+1 vertices with at most P colors.
- Common Reductions: Determine if a sequence A exists such that M rolling hash subsegments are all non-zero mod prime P. Inverting powers of base B reduces hash(L..R) != 0 to y_R != y_{L-1} mod P on prefix hashes, which is graph coloring on N+1 <= 17 vertices. Testing if chromatic number chi(G) <= P via Fast Zeta Transform and inclusion-exclusion runs in O(N 2^N) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc171_d`](../../analysis/AtCoder-arc171_d.md) | D. Rolling Hash | 2377 | Determine if a sequence A exists such that M rolling hash subsegments are all non-zero mod prime P. Inverting powers of ... |
