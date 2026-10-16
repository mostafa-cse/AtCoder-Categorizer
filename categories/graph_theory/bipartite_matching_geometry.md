# 📖 Bipartite Matching on Geometric Directional Lattice via Dinic / Hopcroft-Karp

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Bipartite Matching & Network Flow`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Bipartite Matching on Geometric Directional Lattice via Dinic / Hopcroft-Karp**.

---

## 🏆 Curated High-Value Problems

### Planes on a 2D Plane (`[problem:AtCoder-typical90_by]`)

- **Role**: *Bipartite Matching on Geometric Directional Lattice via Dinic / Hopcroft-Karp*
- **Rating**: `2600` (★7) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_by)
- **Full Analysis**: [AtCoder-typical90_by Analysis](../../analysis/AtCoder-typical90_by.md)

#### Problem Statement & Task
N points A_i, N destination points B_j. Each point A_i must move to a unique destination B_j along one of 8 compass directions by exact distance T. Determine if valid bijection exists, and output direction for each point.

#### Core Invariant & Observation
For each point A_i, check its 8 compass destinations. Use a hash map on B coordinates to identify target indices in O(1). Add directed edges and run Dinic's Max-Flow algorithm.

#### Algorithmic Formulation
1. Hash map B points: map<pair<int, int>, int> id_B.
2. For each A_i: test 8 compass offsets by T. If destination in id_B, add flow edge i -> j.
3. Run Dinic's Algorithm. If max_flow == N, reconstruct direction for each A_i; else 'No'.

**Complexity**: `Time: O(N sqrt(N)) with Dinic on unit network, Space: O(N).`  
**Editorial Alignment**: Bipartite matching reduction on 8-direction geometric grid.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Bipartite matching with coordinate hash table lookup and path direction reconstruction.
- **Reusable Pattern**: `Geometric Bipartite Matching via Max-Flow.`

---

[Back to Master Categories](../../README.md)
