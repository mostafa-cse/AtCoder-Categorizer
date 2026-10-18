# Dijkstra's Algorithm

**Taxonomy Path**: `Graph Theory` > `Shortest Paths` > `Dijkstra's Algorithm`

## Description
This topic focuses on dijkstra's algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The residual is always a proper suffix or prefix of one of the original strings $S_i$. With $N \le 50$ and $|S_i| \le 20$, there are at most $2 \sum |S_i| \le 2000$ states. From each state, trying all $N$ transitions explores at most $10^5$ directed edges.
- Common Reductions: Find minimum cost to concatenate a sequence of strings from $S_1, \dots, S_N$ (with costs $C_i$) to form a palindrome. View palindrome formation as canceling characters inward from left and right boundaries. The state of the system is the unmatched residual string: either a suffix of $S_i$ remaining on the left, or a prefix of $S_i$ remaining on the right. Concatenating a string $S_k$ on the opposite side cancels matching characters and transitions to a new residual. Dijkstra's algorithm finds the shortest path from single-string initial states to any state whose residual is itself a palindrome.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc175_f`](../../analysis/AtCoder-abc175_f.md) | F. Making Palindrome | 2512 | Find minimum cost to concatenate a sequence of strings from $S_1, \dots, S_N$ (with costs $C_i$) to form a palindrome. V... |
