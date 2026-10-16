# 📖 Online Grid Connectivity & 2D Linearization DSU

- **Tag / Domain**: `Data Structures (DS)`
- **Subtopic**: `Disjoint Set Union (DSU)`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Transforming 2D spatial coordinate grids into 1D arrays and maintaining dynamic component connectivity using Disjoint Set Union.

---

## 🏆 Curated High-Value Problems

### 1. Red Painting (`[problem:AtCoder-typical90_l]`)

- **Role**: *2D Grid Coordinate Linearization with Dynamic DSU*
- **Rating**: `1250` | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_l)
- **Full Analysis**: [AtCoder-typical90_l Analysis](../../analysis/AtCoder-typical90_l.md)

#### Problem Statement & Task
Dynamically color grid cells red and answer reachability queries between red cells.

#### Core Invariant & Observation
DSU handles incremental edge additions in almost constant amortized time O(alpha(V)), eliminating the need to rerun BFS/DFS per query.

#### Algorithmic Formulation
1. Map (r, c) -> r * W + c. Initialize DSU and boolean is_red grid.
2. On color query: set is_red[r][c] = True; for each neighbor (nr, nc) that is red: dsu.unite(idx(r,c), idx(nr,nc)).
3. On reachability query: if is_red[a] and is_red[b] and dsu.same(idx_a, idx_b) -> 'Yes', else 'No'.

**Complexity**: `Time: O(Q * alpha(H * W)), Space: O(H * W).`  
**Editorial Alignment**: Online dynamic connectivity on 2D grid via DSU.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: 2D-to-1D coordinate flattening and online component maintenance without BFS/DFS reruns.
- **Reusable Pattern**: `Grid coordinate linearization + online DSU.`

---

[Back to Data Structures (DS) Index](README.md) | [Back to Master Categories](../../README.md)
