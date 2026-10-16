# 📖 Monotonicity of Floyd-Warshall Distance & Dual Binary Search

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Shortest Paths & Binary Search`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Monotonicity of Floyd-Warshall Distance & Dual Binary Search**.

---

## 🏆 Curated High-Value Problems

### Chokudai's Demand (`[problem:AtCoder-typical90_ci]`)

- **Role**: *Monotonicity of Floyd-Warshall Distance & Dual Binary Search*
- **Rating**: `1850` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ci)
- **Full Analysis**: [AtCoder-typical90_ci Analysis](../../analysis/AtCoder-typical90_ci.md)

#### Problem Statement & Task
Complete graph with N <= 40 vertices. Some edges have unknown weight X. Count number of integer values of X >= 1 such that exactly K pairs of vertices have shortest path distance <= P.

#### Core Invariant & Observation
Let f(X) be the number of pairs with distance <= P computed via Floyd-Warshall in O(N^3). Since f(X) is monotonic, use binary search to find maximum X with f(X) >= K (call it R) and maximum X with f(X) >= K + 1 (call it L). The number of valid X is R - L (or Infinity if R exceeds limit).

#### Algorithmic Formulation
1. Function count_pairs(X): run Floyd-Warshall, count pairs with dist <= P.
2. Binary search R = max X with count_pairs(X) >= K.
3. Binary search L = max X with count_pairs(X) >= K + 1.
4. If R >= INF_BOUND: output 'Infinity'; else output R - L.

**Complexity**: `Time: O(N^3 * log(INF)), Space: O(N^2).`  
**Editorial Alignment**: Dual binary search on Floyd-Warshall distance monotonicity.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Monotonicity in parametric shortest paths and dual binary search range boundary subtraction.
- **Reusable Pattern**: `Parametric Floyd-Warshall with Dual Binary Search.`

---

[Back to Master Categories](../../README.md)
