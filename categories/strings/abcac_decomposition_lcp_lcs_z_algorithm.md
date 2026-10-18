# Z Algorithm

**Taxonomy Path**: `Strings` > `String Matching` > `Z Algorithm`

## Description
This topic focuses on z algorithm techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: In any decomposition S = ABCAC with non-empty A, B, C, let L = |AC| = |S| - i, where i is the start index of the suffix AC. A must be a common prefix of S and S[i..], so 1 <= |A| <= min(LCP(S, S[i..]), L-1). C must be a common suffix of S[..i-1] and S, so |AC| - |A| <= LCS(S[..i-1], S), giving max(1, L - LCS) <= |A| <= min(LCP, L-1).
- Common Reductions: Fix the split index between ABC and AC. The length of A is bounded above by LCP and below by L - LCS. Computing both via Z-algorithm on S and S^R counts valid decompositions in O(|S|) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc055_c`](../../analysis/AtCoder-arc055_c.md) | C. ABCAC | 2392 | Fix the split index between ABC and AC. The length of A is bounded above by LCP and below by L - LCS. Computing both via... |
