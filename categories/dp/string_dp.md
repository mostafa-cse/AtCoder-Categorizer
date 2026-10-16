# 📖 Subsequence Matching DP / Automaton DP

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Classic DP`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Subsequence Matching DP / Automaton DP**.

---

## 🏆 Curated High-Value Problems

### AtCounter (`[problem:AtCoder-typical90_h]`)

- **Role**: *Subsequence Matching DP / Automaton DP*
- **Rating**: `1150` (★4) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_h)
- **Full Analysis**: [AtCoder-typical90_h Analysis](../../analysis/AtCoder-typical90_h.md)

#### Problem Statement & Task
Given string S of length N, count the number of subsequences equal to 'atcoder' modulo 10^9+7.

#### Core Invariant & Observation
Each character S[i] can either be skipped or, if it matches target[j], can advance all existing prefixes of length j to length j+1.

#### Algorithmic Formulation
1. dp[0] = 1, dp[1..7] = 0.
2. Target T = 'atcoder'.
3. For char c in S: for j from 0 to 6: if c == T[j]: dp[j+1] = (dp[j+1] + dp[j]) % MOD.
4. Output dp[7].

**Complexity**: `Time: O(|T| * N) = O(7N), Space: O(|T|) = O(1).`  
**Editorial Alignment**: Linear string prefix matching dynamic programming.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Counting pattern subsequences in linear time using state transition arrays.
- **Reusable Pattern**: `Pattern-Prefix Subsequence DP.`

---

[Back to Master Categories](../../README.md)
