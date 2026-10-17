# Interactive Problems

**Taxonomy Path**: `Miscellaneous` > `Interactive Problems` > `Interactive Problems`

## Description
This topic focuses on interactive problems techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Querying $n$ returns 'Y' iff ($n \le N$ and $str(n) \le str(N)$) or ($n > N$ and $str(n) > str(N)$). Querying $10^9$ uniquely isolates powers of 10. For non-powers of 10, querying $10^k$ reveals the number of digits $L$ of $N$, and querying $mid \times 10$ ensures $mid \times 10 > N$, returning 'Y' if and only if $mid \ge N$.
- Common Reductions: Identify a hidden integer $1 \le N \le 10^9$ in at most 64 queries where each query $n$ returns whether $(n \le N \land n \le_{lex} N)$ or $(n > N \land n >_{lex} N)$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc078_c`](../../analysis/AtCoder-arc078_c.md) | E. Awkward Response | 2300 | Identify a hidden integer $1 \le N \le 10^9$ in at most 64 queries where each query $n$ returns whether $(n \le N \land ... |
