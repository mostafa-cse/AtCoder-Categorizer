# 📖 Modular Linear Congruences & Extended GCD

- **Tag / Domain**: `Number Theory`
- **Subtopic**: `Modular Arithmetic`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Solving linear congruences ax = b (mod m) and computing modular inverses via the Extended Euclidean Algorithm.

---

## 🏆 Curated High-Value Problems

### 1. Throne (`[problem:AtCoder-abc186_e]`)

- **Role**: *Extended Euclidean Algorithm for Linear Congruence*
- **Rating**: `1250` | **Contest**: [`abc186`](https://atcoder.jp/contests/abc186/tasks/abc186_e)
- **Full Analysis**: [AtCoder-abc186_e Analysis](../../analysis/AtCoder-abc186_e.md)

#### Problem Statement & Task
Move K steps clockwise on a circle of size N, starting at position S. Find minimum steps to reach 0.

#### Core Invariant & Observation
Dividing through by g = gcd(K, N) yields K' * x = -S' (mod N') where gcd(K', N') = 1. The modular inverse of K' mod N' gives the unique solution.

#### Algorithmic Formulation
1. g = gcd(K, N). If S % g != 0 return -1.
2. K' = K/g, S' = S/g, N' = N/g.
3. Find inv = mod_inv(K', N') via Extended GCD.
4. Output (-S' * inv) mod N'.

**Complexity**: `Time: O(log(min(K, N))), Space: O(1).`  
**Editorial Alignment**: Extended Euclidean Algorithm for modular inverse.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Modular linear congruences, solvability condition via GCD divisibility, and Extended Euclidean Algorithm.
- **Reusable Pattern**: `Extended Euclidean linear congruence solver.`

---

[Back to Number Theory Index](README.md) | [Back to Master Categories](../../README.md)
