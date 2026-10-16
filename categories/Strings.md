# 🔤 AtCoder Curriculum: Strings

Curated collection of high-value problems in **Strings** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.

- **Total Curated Problems**: 1
- **Taxonomy Tier**: Tag (Domain Level)

---

## 📑 Table of Contents

- [Greedy on Strings](#greedy-on-strings)
  - [Next-Occurrence Array / Lexicographically Smallest Subsequence](#next-occurrence-array--lexicographically-smallest-subsequence) (1 problems)

---

## Greedy on Strings

### Next-Occurrence Array / Lexicographically Smallest Subsequence

#### Smallest Subsequence (`[problem:AtCoder-typical90_f]`)
- **Rating / Difficulty**: 1500
- **Contest**: `typical90` | [AtCoder Link](https://atcoder.jp/contests/typical90/tasks/typical90_f)
- **Detailed Analysis**: [`analysis/AtCoder-typical90_f.md`](../analysis/AtCoder-typical90_f.md)
- **Key Idea**: Find the lexicographically smallest subsequence of length K from string S of length N.
- **Core Observation**: To minimize lexicographically, greedily choose the smallest possible character for each of the K positions from left to right. A character choice at position p is valid if and only if the remaining suffix has length >= remaining positions needed.
- **Algorithm & Complexity**: Time: O(26 * N + 26 * K), Space: O(26 * N).
- **What This Problem Teaches**: Precomputing next-occurrence transition tables on strings and greedy lexicographical construction.
- **Reusable Pattern**: `Next-occurrence array for subsequence queries.`

---
