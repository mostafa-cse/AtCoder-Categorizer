# 📖 Digit-Length Interval Partition & Arithmetic Series Summation

- **Tag / Domain**: `Math`
- **Subtopic**: `Arithmetic Series & Digit Ranges`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Digit-Length Interval Partition & Arithmetic Series Summation**.

---

## 🏆 Curated High-Value Problems

### Counting Numbers (`[problem:AtCoder-typical90_cd]`)

- **Role**: *Digit-Length Interval Partition & Arithmetic Series Summation*
- **Rating**: `850` (★3) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_cd)
- **Full Analysis**: [AtCoder-typical90_cd Analysis](../../analysis/AtCoder-typical90_cd.md)

#### Problem Statement & Task
For each integer x in [L, R] (L, R <= 10^18), write x down x times. Count total digits written modulo 998244353.

#### Core Invariant & Observation
In subinterval [A, B] where all numbers have length d, sum of numbers is sum_{x=A}^B x = (A + B)*(B - A + 1)/2. Total digits written is d * sum mod 998244353.

#### Algorithmic Formulation
1. For d from 1 to 19:
   - low = 10^(d-1), high = 10^d - 1.
   - A = max(L, low), B = min(R, high).
   - If A <= B: total += d * sum(A..B) % MOD.
2. Output total.

**Complexity**: `Time: O(log_10 R) = 19 steps, Space: O(1).`  
**Editorial Alignment**: Partitioning range by base-10 digit length with arithmetic progression sums.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Digit length interval slicing, arithmetic progression summation, and modular arithmetic.
- **Reusable Pattern**: `Digit Length Interval Slicing.`

---

[Back to Master Categories](../../README.md)
