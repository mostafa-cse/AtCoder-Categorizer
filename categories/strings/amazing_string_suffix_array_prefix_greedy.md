# Suffix Array

**Taxonomy Path**: `Strings` > `Suffix Structures` > `Suffix Array`

## Description
This topic focuses on suffix array techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If the total count of 'a' in $S$ plus $K$ is at least $|S|$, we can reduce the string to all 'a's of minimal length $\max(1, |S| - K)$. Otherwise, we must maximize the number of leading 'a's. Replacing all non-'a' characters in prefix $S[0 \dots i-1]$ with 'a' and prepending any remaining operations as 'a's produces $K + \text{cnt\_a}(i)$ leading 'a's, provided $\text{cnt\_nona}(i) \le K$. To minimize the resulting string, we select the candidate index $i$ that maximizes leading 'a's and minimizes the remaining suffix $S[i \dots |S|-1]$. The optimal suffix is selected in $O(1)$ using the Suffix Array.
- Common Reductions: Find the lexicographically smallest string obtainable by applying exactly $K$ operations (delete, replace, insert) to string $S$.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-discovery_2016_qual_c`](../../analysis/AtCoder-discovery_2016_qual_c.md) | C - アメージングな文字列は、きみが作る！ | 2527 | Find the lexicographically smallest string obtainable by applying exactly $K$ operations (delete, replace, insert) to st... |
