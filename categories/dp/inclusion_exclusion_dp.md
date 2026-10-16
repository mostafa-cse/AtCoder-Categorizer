# 📖 Inclusion-Exclusion Principle & Combinatorics Grid DP

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Classic DP`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Counting paths avoiding multiple obstacles on large coordinate grids by sorting obstacles and subtracting overlapping forbidden paths using dynamic programming.

---

## 🏆 Curated High-Value Problems

### 1. Grid 2 (`[problem:AtCoder-dp_y]`)

- **Role**: *First-Hit Obstacle Inclusion-Exclusion DP*
- **Rating**: `2150` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_y)
- **Full Analysis**: [AtCoder-dp_y Analysis](../../analysis/AtCoder-dp_y.md)

#### Problem Statement & Task
Grid of size H x W with N <= 3000 obstacles. Count paths from (1, 1) to (H, W) avoiding all obstacles. (H, W <= 10^5).

#### Core Invariant & Observation
dp[i] = binom((r_i - 1) + (c_i - 1), r_i - 1) - sum_{j < i, r_j <= r_i, c_j <= c_i} (dp[j] * binom((r_i - r_j) + (c_i - c_j), r_i - r_j)).

#### Algorithmic Formulation
1. Add destination (H, W) as (N+1)-th obstacle.
2. Sort obstacles by (r, c).
3. Precompute factorials and inverse factorials up to H + W.
4. For each obstacle i: dp[i] = ways(1,1 to i) - sum_{j < i} (dp[j] * ways(j to i)).
5. Return dp[destination].

**Complexity**: `Time: O(N^2 + (H + W)), Space: O(N + H + W).`  
**Editorial Alignment**: First-hit obstacle inclusion-exclusion dynamic programming.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Combinatorial grid paths with obstacles using first-encounter inclusion-exclusion.
- **Reusable Pattern**: `First-hit inclusion-exclusion over coordinate points.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
