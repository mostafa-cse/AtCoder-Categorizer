# 📖 Manhattan Median Principle / Dimension Separation L1 Minimization

- **Tag / Domain**: `Math`
- **Subtopic**: `Optimization & Medians`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Manhattan Median Principle / Dimension Separation L1 Minimization**.

---

## 🏆 Curated High-Value Problems

### Plant Planning (`[problem:AtCoder-typical90_br]`)

- **Role**: *Manhattan Median Principle / Dimension Separation L1 Minimization*
- **Rating**: `1200` (★4) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_br)
- **Full Analysis**: [AtCoder-typical90_br Analysis](../../analysis/AtCoder-typical90_br.md)

#### Problem Statement & Task
Given N factories at coordinates (X_i, Y_i), choose plant location (x, y) to minimize the sum of Manhattan distances: sum (|X_i - x| + |Y_i - y|).

#### Core Invariant & Observation
For any 1D set of numbers, sum |X_i - x| is minimized when x is the MEDIAN of {X_1, ..., X_N}!

#### Algorithmic Formulation
1. Sort X array, choose median x = X[N / 2].
2. Sort Y array, choose median y = Y[N / 2].
3. Sum |X_i - x| + |Y_i - y| over all points.

**Complexity**: `Time: O(N log N), Space: O(N).`  
**Editorial Alignment**: Dimension separation and 1D median minimization.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: L1 metric dimensional independence and the Median Minimization theorem.
- **Reusable Pattern**: `Independent Median Minimization for L1 Metric.`

---

[Back to Master Categories](../../README.md)
