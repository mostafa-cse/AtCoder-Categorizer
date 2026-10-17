# Meet in the Middle

**Taxonomy Path**: `Miscellaneous` > `Techniques` > `Meet in the Middle`

## Description
This topic focuses on meet in the middle techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: By linearity of expectation, the expected value equals the sum over all subsets S with sum(S) < X of the probability of reaching state S times the expected money stolen next: sum_{S: sum(S)<X} [1 / (C(N, |S|) * (N - |S|))] * (A_all - sum(S)). Grouping by subset size k = |S|, we only need the count of subsets of size k with sum < X and the sum of their sums. Because N <= 40, we split the elements into halves of size 20 and apply Meet-in-the-Middle with binary search.
- Common Reductions: Find the expected total amount stolen from N <= 40 safes opened in uniform random order until the total amount stolen reaches at least X.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc464_f`](../../analysis/AtCoder-abc464_f.md) | Random Vault Heist | 2225 | Find the expected total amount stolen from N <= 40 safes opened in uniform random order until the total amount stolen re... |
