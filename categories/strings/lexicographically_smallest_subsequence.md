# 📖 Next-Occurrence Array & Lexicographical Subsequences

- **Tag / Domain**: `Strings`
- **Subtopic**: `Greedy on Strings`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Precomputing next-character occurrence lookup tables to greedily construct optimal subsequences.

---

## 🏆 Curated High-Value Problems

### 1. Smallest Subsequence (`[problem:AtCoder-typical90_f]`)

- **Role**: *Next-Occurrence Table Subsequence Construction*
- **Rating**: `1500` | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_f)
- **Full Analysis**: [AtCoder-typical90_f Analysis](../../analysis/AtCoder-typical90_f.md)

#### Problem Statement & Task
Find the lexicographically smallest subsequence of length K from string S of length N.

#### Core Invariant & Observation
Precomputing next_pos[i][c] (earliest index >= i of character c) allows O(26) decision per position.

#### Algorithmic Formulation
1. Precompute next_pos[i][c] in O(26 * N).
2. cur = 0.
3. For step from 1 to K: for char c in 'a'..'z': pos = next_pos[cur][c]; if N - pos >= K - step: append c, cur = pos + 1, break.
4. Output string.

**Complexity**: `Time: O(26 * N + 26 * K), Space: O(26 * N).`  
**Editorial Alignment**: Next-character transition table with greedy lookahead.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Precomputing next-occurrence transition tables on strings and greedy lexicographical construction.
- **Reusable Pattern**: `Next-occurrence array for subsequence queries.`

---

[Back to Strings Index](README.md) | [Back to Master Categories](../../README.md)
