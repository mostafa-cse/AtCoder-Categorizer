# 📖 Polar Angle Sort + Binary Search for Opposite Vector

- **Tag / Domain**: `Geometry`
- **Subtopic**: `Angular Sweep / Polar Angles`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Polar Angle Sort + Binary Search for Opposite Vector**.

---

## 🏆 Curated High-Value Problems

### Three Point Angle (`[problem:AtCoder-typical90_i]`)

- **Role**: *Polar Angle Sort + Binary Search for Opposite Vector*
- **Rating**: `2100` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_i)
- **Full Analysis**: [AtCoder-typical90_i Analysis](../../analysis/AtCoder-typical90_i.md)

#### Problem Statement & Task
Given N points in 2D plane (N <= 2000), choose three distinct points p_j, p_i, p_k to maximize the angle between vectors (p_j - p_i) and (p_k - p_i). Output maximum angle in degrees.

#### Core Invariant & Observation
Sort polar angles in [0, 360). For any angle theta_j, the optimal opposite angle is closest to (theta_j + 180). Use std::lower_bound to find the closest angles in O(log N).

#### Algorithmic Formulation
1. Iterate each point i as pivot.
2. Calculate angles theta = atan2(y - y_i, x - x_i) * 180 / PI in [0, 360).
3. Sort angles array.
4. For each angle t: binary search for (t + 180) % 360; check adjacent candidates and update max angle.
5. Return global max.

**Complexity**: `Time: O(N^2 log N), Space: O(N).`  
**Editorial Alignment**: Polar angle sorting and binary searching target opposite rays.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Polar coordinate transformations, atan2 angle sorting, and binary searching for antipodal vectors.
- **Reusable Pattern**: `Polar Angle Sort + Binary Search for Opposite Vector.`

---

[Back to Master Categories](../../README.md)
