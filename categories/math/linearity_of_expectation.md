# 📖 Linearity of Expectation on Inversions

- **Tag / Domain**: `Math`
- **Subtopic**: `Probability & Expected Value`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Linearity of Expectation on Inversions**.

---

## 🏆 Curated High-Value Problems

### Various Arrays (`[problem:AtCoder-typical90_bn]`)

- **Role**: *Linearity of Expectation on Inversions*
- **Rating**: `1550` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bn)
- **Full Analysis**: [AtCoder-typical90_bn Analysis](../../analysis/AtCoder-typical90_bn.md)

#### Problem Statement & Task
N independent random variables A_i chosen uniformly from [L_i, R_i]. Find the expected number of inversions (pairs i < j with A_i > A_j).

#### Core Invariant & Observation
E[Inversions] = sum_{1 <= i < j <= N} P(A_i > A_j). For fixed i < j, P(A_i > A_j) is the count of pairs (x, y) with x in [L_i, R_i], y in [L_j, R_j], x > y, divided by (R_i - L_i + 1) * (R_j - L_j + 1).

#### Algorithmic Formulation
1. ans = 0.0.
2. Loop 1 <= i < j <= N:
   - Count pairs (x, y) with x in [L_i, R_i], y in [L_j, R_j] such that x > y.
   - prob = pairs / ((R_i - L_i + 1) * (R_j - L_j + 1)).
   - ans += prob.
3. Output ans.

**Complexity**: `Time: O(N^2 * (R - L)), Space: O(N).`  
**Editorial Alignment**: Linearity of expectation summing pairwise inversion probabilities.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Linearity of Expectation on discrete independent random variables without joint distributions.
- **Reusable Pattern**: `Linearity of Expectation on Pairwise Indicators.`

---

[Back to Master Categories](../../README.md)
