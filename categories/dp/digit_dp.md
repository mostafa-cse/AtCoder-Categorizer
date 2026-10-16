# 📖 Digit DP & Prefix Bound Relaxation

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Digit DP`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Constructing numbers digit-by-digit from most significant to least significant digit while maintaining tight upper-bound flags and modulo constraints.

---

## 🏆 Curated High-Value Problems

### 1. Digit Sum (`[problem:AtCoder-dp_s]`)

- **Role**: *Digit DP with Remainder State*
- **Rating**: `1750` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_s)
- **Full Analysis**: [AtCoder-dp_s Analysis](../../analysis/AtCoder-dp_s.md)

#### Problem Statement & Task
Count positive integers up to K (K <= 10^10000) whose sum of digits is a multiple of D.

#### Core Invariant & Observation
At index i, if tight is True, the next digit can only range from 0 to K[i]. If tight is False, the next digit can range from 0 to 9 freely.

#### Algorithmic Formulation
1. dp[index][rem][tight]: count of valid prefix configurations.
2. For each digit d in 0..(tight ? K[idx] : 9): dp[idx+1][(rem + d) % D][tight and (d == K[idx])] += dp[idx][rem][tight].
3. Final count = (dp[len][0][0] + dp[len][0][1] - 1 + MOD) % MOD.

**Complexity**: `Time: O(|K| * D * 10), Space: O(|K| * D).`  
**Editorial Alignment**: Textbook Digit DP with tight bound tracking.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Digit-by-digit construction, tight prefix bound handling, and large integer parsing.
- **Reusable Pattern**: `Standard Digit DP state tuple (index, remainder, is_tight).`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
