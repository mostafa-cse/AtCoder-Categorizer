# Expression Parsing

**Taxonomy Path**: `Miscellaneous` > `General` > `Expression Parsing`

## Description
This topic focuses on expression parsing techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: The compressed string grammar consists of literals, blocks, and repetition expressions `(expr)K`. Parse the expression into an Abstract Syntax Tree (AST) where each node computes its decompressed length using 64-bit integers. If $B < 0$, wrap to $M + B$ where $M$ is root length. Querying character by character takes too long when $L = 10^5$, but querying the continuous range $[B, B + L - 1]$ recursively through the AST intersects at most 2 periods per repetition node, yielding $O(L + \text{depth})$ efficient extraction.
- Common Reductions: Extract a substring of length $L \le 10^5$ starting at 0-indexed position $B$ from an EBNF run-length compressed string $S$ with decompressed length up to $10^{15}$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-tenka1_2013_qualA_d`](../../analysis/AtCoder-tenka1_2013_qualA_d.md) | D - 天下一展開 | 2507 | Extract a substring of length $L \le 10^5$ starting at 0-indexed position $B$ from an EBNF run-length compressed string ... |
