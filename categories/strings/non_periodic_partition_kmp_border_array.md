# Knuth Morris Pratt (KMP) and Prefix Automaton

**Taxonomy Path**: `Strings` > `String Matching` > `Knuth Morris Pratt (KMP) and Prefix Automaton`

## Description
This topic focuses on knuth morris pratt (kmp) and prefix automaton techniques for solving competitive programming problems.

## Key Invariants & Techniques
- Invariants: If all characters are identical, k = |w| and the answer is 1. If w itself is non-periodic, k = 1 and the answer is 1. Otherwise, k = 2 is always achievable! A partition into 2 non-periodic strings exists at cut i iff both prefix w[1..i] and suffix w[i+1..|w|] are non-periodic. By the KMP border array, string s of length L is periodic iff L % (L - pi[L]) == 0 and pi[L] > 0. We compute pi on w and on reversed w^R to classify all prefixes and suffixes in O(N) time.
- Common Reductions: Given a string w, find the minimum integer k such that w can be partitioned into k non-periodic strings, and count the number of such partitions of minimum size.

## Curated Problem Ladder
| Problem ID | Title | Rating | Key Technique / Reduction |
| :--- | :--- | :--- | :--- |
| [`AtCoder-arc060_d`](../../analysis/AtCoder-arc060_d.md) | F - Best Representation | 2804 | Given a string w, find the minimum integer k such that w can be partitioned into k non-periodic strings, and count the n... |
