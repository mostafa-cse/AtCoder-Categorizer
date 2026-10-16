# 📖 Grid DP & Path Counting with Obstacles

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Classic DP`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
2D grid dynamic programming, path counting under directional movement restrictions, obstacle nullification, and modular arithmetic transitions.

---

## 🏆 Curated High-Value Problems

### 1. Grid 1 (`[problem:AtCoder-dp_h]`)

- **Role**: *Grid DP / Path Counting with Obstacles*
- **Rating**: `1050` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_h)
- **Full Analysis**: [AtCoder-dp_h Analysis](../../analysis/AtCoder-dp_h.md)

#### Problem Statement & Task
Count paths from top-left (1,1) to bottom-right (H,W) moving only right and down, avoiding obstacle walls '#'. Output modulo 10^9+7.

#### Core Invariant & Observation
Transitions are purely local: dp[r][c] = (dp[r-1][c] + dp[r][c-1]) mod (10^9+7). Any obstacle cell '#' strictly resets dp[r][c] to 0.

#### Algorithmic Formulation
1. dp[1][1] = 1.
2. For r in 1..H, c in 1..W: if grid[r][c] == '#': dp[r][c] = 0; else dp[r][c] = (dp[r-1][c] + dp[r][c-1]) % MOD.
3. Return dp[H][W].

**Complexity**: `Time: O(H * W), Space: O(W).`  
**Editorial Alignment**: Grid combinatorial dynamic programming.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Grid boundary enforcement, obstacle nullification, and modulo arithmetic accumulation.
- **Reusable Pattern**: `2D additive grid DP.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
