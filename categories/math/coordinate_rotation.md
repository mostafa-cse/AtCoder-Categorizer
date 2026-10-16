# 📖 45-Degree Coordinate Rotation / Manhattan to Chebyshev Distance Transformation

- **Tag / Domain**: `Math`
- **Subtopic**: `Coordinate Geometry & Metrics`

---

## 💡 Topic Overview
High-value competitive programming techniques for **45-Degree Coordinate Rotation / Manhattan to Chebyshev Distance Transformation**.

---

## 🏆 Curated High-Value Problems

### Max Manhattan Distance (`[problem:AtCoder-typical90_aj]`)

- **Role**: *45-Degree Coordinate Rotation / Manhattan to Chebyshev Distance Transformation*
- **Rating**: `1600` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_aj)
- **Full Analysis**: [AtCoder-typical90_aj Analysis](../../analysis/AtCoder-typical90_aj.md)

#### Problem Statement & Task
Given N points (x_i, y_i), answer Q queries: for point q, find max Manhattan distance |x_q - x_j| + |y_q - y_j| to any point j.

#### Core Invariant & Observation
After transforming, max Chebyshev distance from (X_q, Y_q) is max(|X_q - min X|, |X_q - max X|, |Y_q - min Y|, |Y_q - max Y|), which evaluates in O(1)!

#### Algorithmic Formulation
1. For each point i: X_i = x_i + y_i, Y_i = x_i - y_i.
2. Find min_X, max_X, min_Y, max_Y over all N points.
3. For each query q: output max({|X_q - min_X|, |X_q - max_X|, |Y_q - min_Y|, |Y_q - max_Y|}).

**Complexity**: `Time: O(N + Q), Space: O(N).`  
**Editorial Alignment**: 45-degree rotation converting Manhattan metric to Chebyshev metric.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Transforming coupled L1 distance dimensions into independent L_infinity coordinate extremes.
- **Reusable Pattern**: `45-Degree Coordinate Rotation (Manhattan to Chebyshev).`

---

[Back to Master Categories](../../README.md)
