# 📖 Doubling DP / Matrix Exponentiation on Modular Digit Transitions

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `DP on Different Structures`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Doubling DP / Matrix Exponentiation on Modular Digit Transitions**.

---

## 🏆 Curated High-Value Problems

### Restricted Digits (`[problem:AtCoder-typical90_e]`)

- **Role**: *Doubling DP / Matrix Exponentiation on Modular Digit Transitions*
- **Rating**: `2400` (★7) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_e)
- **Full Analysis**: [AtCoder-typical90_e Analysis](../../analysis/AtCoder-typical90_e.md)

#### Problem Statement & Task
Count N-digit positive integers (N <= 10^18) whose digits are chosen from a set of K non-zero digits and are divisible by B (B <= 1000). Modulo 10^9+7.

#### Core Invariant & Observation
Concatenating two numbers X and Y each of length L produces X * 10^L + Y. Thus remainder mod B is (rem(X) * 10^L + rem(Y)) % B. Compute dp[p][r] for length 2^p in O(B^2 log N).

#### Algorithmic Formulation
1. Base: dp[0][c % B] = count of digit c in allowed set.
2. Doubling step: dp[p+1][(r1 * pow10[p] + r2) % B] = sum(dp[p][r1] * dp[p][r2]).
3. Combine binary powers of N to get final remainder distribution.
4. Output answer at remainder 0.

**Complexity**: `Time: O(B^2 log N), Space: O(B log N).`  
**Editorial Alignment**: Doubling DP on remainder transitions across power-of-two digit lengths.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Doubling DP on large digit lengths, modular arithmetic concatenation, and transition convolution.
- **Reusable Pattern**: `Doubling DP on digit concatenations.`

---

[Back to Master Categories](../../README.md)
