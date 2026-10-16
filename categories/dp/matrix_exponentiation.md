# 📖 Matrix Exponentiation DP

- **Tag / Domain**: `Dynamic Programming (DP)`
- **Subtopic**: `Dp on Different Structures`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Modeling linear DP state recurrences and graph path counting as matrix multiplications, accelerated to O(N^3 log K) via binary exponentiation.

---

## 🏆 Curated High-Value Problems

### 1. Walk (`[problem:AtCoder-dp_r]`)

- **Role**: *Matrix Exponentiation DP*
- **Rating**: `1700` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_r)
- **Full Analysis**: [AtCoder-dp_r Analysis](../../analysis/AtCoder-dp_r.md)

#### Problem Statement & Task
Given a directed graph with N vertices (N <= 50), count the number of directed paths of exact length K (K <= 10^18) modulo 10^9+7.

#### Core Invariant & Observation
Matrix multiplication computes transitions; binary exponentiation solves K <= 10^18 in O(N^3 log K) steps.

#### Algorithmic Formulation
1. Construct adjacency matrix A.
2. Compute M = A^K mod (10^9+7) using binary matrix exponentiation.
3. Total paths = sum_{i, j} M[i][j] mod MOD.

**Complexity**: `Time: O(N^3 log K), Space: O(N^2).`  
**Editorial Alignment**: Matrix exponentiation for path counting on graphs.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Formulating linear state recurrences as matrix products and exponentiating large step counts.
- **Reusable Pattern**: `Matrix exponentiation DP for enormous transition steps.`

---

[Back to Dynamic Programming (DP) Index](README.md) | [Back to Master Categories](../../README.md)
