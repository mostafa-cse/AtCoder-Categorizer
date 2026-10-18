# Permutations, Combinations and Basic Counting Problems

**Taxonomy Path**: `Basics` > `Basic Counting` > `Permutations, Combinations and Basic Counting Problems`

## Description
This topic focuses on permutations, combinations and basic counting problems techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: For any two legs A and B of lengths L_A <= L_B, the path outer(A) -> body -> outer(B) being a palindrome forces bones at distance k <= L_A from the tip to share identical characters across all legs, while the remaining suffix of length L_B - L_A on leg B must be a palindrome. For multiple leg lengths, these palindromic suffix constraints equate characters with period g = gcd of adjacent length differences, giving exactly L_min + floor((g + 1) / 2) independent components.
- Common Reductions: Paths between leg tips form palindromes iff identical-depth bones match and differences between leg lengths form periodic palindromic suffixes with period g = gcd of differences. The number of independent bone components is L_min + floor((g+1)/2), evaluated in O(N + log M) time.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc048_c`](../../analysis/AtCoder-arc048_c.md) | C. 足の多い高橋君 | 2390 | Paths between leg tips form palindromes iff identical-depth bones match and differences between leg lengths form periodi... |
