# 📖 Alternating Difference Prefix Sums & Interval DSU Reachability

- **Tag / Domain**: `Data Structures (DS)`
- **Subtopic**: `Disjoint Set Union (DSU) & Fenwick Tree`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Alternating Difference Prefix Sums & Interval DSU Reachability**.

---

## 🏆 Curated High-Value Problems

### Paired Information (`[problem:AtCoder-typical90_bp]`)

- **Role**: *Alternating Difference Prefix Sums & Interval DSU Reachability*
- **Rating**: `1750` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bp)
- **Full Analysis**: [AtCoder-typical90_bp Analysis](../../analysis/AtCoder-typical90_bp.md)

#### Problem Statement & Task
Array A of length N. Q queries: (0) told A_x + A_{x+1} = V; (1) given (x, y, v), if A_x = v, determine value of A_y or output 'Ambiguous'.

#### Core Invariant & Observation
Let A_i = (-1)^{i-1} A_1 + C_i where C is an alternating sum of known adjacent sums. Then A_y = (-1)^{y - x} A_x + (C_y - (-1)^{y - x} C_x). Use DSU to verify contiguous connectivity.

#### Algorithmic Formulation
1. Offline all Type 0 sum constraints; precompute alternating base values.
2. In second pass: maintain DSU of contiguous known adjacencies.
3. For Type 1 queries: if dsu.same(x, y), evaluate A_y using alternating difference; else 'Ambiguous'.

**Complexity**: `Time: O(Q log N), Space: O(N + Q).`  
**Editorial Alignment**: Potential array precomputation with DSU contiguous connectivity validation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Alternating linear systems, potential array offsets, and DSU interval reachability.
- **Reusable Pattern**: `Alternating Potential Offset & DSU Reachability.`

---

[Back to Master Categories](../../README.md)
