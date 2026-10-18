# Interval DP / Range DP / Matrix Chain Multiplication (MCM)

**Taxonomy Path**: `Dynamic Programming (DP)` > `Classic DP` > `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`

## Description
This topic focuses on interval dp / range dp / matrix chain multiplication (mcm) techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any substring S[l..r], optimal deletions preserve contiguous remaining subsequences. Whenever S[l]=='o' pairs with S[m]=='f' such that the enclosed interval S[l+1..m-1] is completely eliminated (dp[l+1][m-1] == 0), the formed 'of' can delete up to K remaining characters from S[m+1..r], leaving max(0, dp[m+1][r] - K) characters.
- Common Reductions: Minimize remaining length of string S under operations deleting 'of' plus up to K subsequent characters (|S| <= 300). Interval DP dp[l][r] considers splitting at mid, and whenever S[l]=='o' pairs with S[m]=='f' with dp[l+1][m-1]==0, the operation consumes up to K remaining characters from S[m+1..r], yielding transitions in O(|S|^3) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-abc325_g`](../../analysis/AtCoder-abc325_g.md) | G. offence | 2388 | Minimize remaining length of string S under operations deleting 'of' plus up to K subsequent characters (|S| <= 300). In... |
