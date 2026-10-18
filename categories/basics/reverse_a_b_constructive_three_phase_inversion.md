# Basic Constructive Algorithms

**Taxonomy Path**: `Basics` > `Greedy and Constructive` > `Basic Constructive Algorithms`

## Description
This topic focuses on basic constructive algorithms techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: Substrings reversed must start with 'A' and end with 'B'. Reversing such a substring changes its first character to 'B' and its last character to 'A', strictly increasing the string lexicographically while preserving 'A' counts and decreasing the reversed string. Thus, necessary and sufficient conditions are: equal 'A' counts, $X \le Y$, and $\text{rev}(X) \ge \text{rev}(Y)$. Stripping matching prefixes and suffixes leaves $X[l]='A', X[r]='B', Y[l]='B', Y[r]='A'$. By matching minority characters between inner substrings, at most $\lfloor N/2 \rfloor$ operations suffice.
- Common Reductions: Determine if binary string $X$ can be transformed into $Y$ using at most $\lfloor N/2 \rfloor$ reversals of substrings starting with 'A' and ending with 'B', and construct the operations.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-agc077_a`](../../analysis/AtCoder-agc077_a.md) | A - Reverse A…B | 2512 | Determine if binary string $X$ can be transformed into $Y$ using at most $\lfloor N/2 \rfloor$ reversals of substrings s... |
