# 📖 Permutation Enumeration with Adjacency Graph Pruning

- **Tag / Domain**: `Basics`
- **Subtopic**: `Permutations & Brute Force`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Permutation Enumeration with Adjacency Graph Pruning**.

---

## 🏆 Curated High-Value Problems

### AtCoder Ekiden (`[problem:AtCoder-typical90_af]`)

- **Role**: *Permutation Enumeration with Adjacency Graph Pruning*
- **Rating**: `850` (★3) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_af)
- **Full Analysis**: [AtCoder-typical90_af Analysis](../../analysis/AtCoder-typical90_af.md)

#### Problem Statement & Task
N runners (N <= 10) run N sections. Runner i takes A_{i, j} time for section j. M pairs of runners (X_k, Y_k) cannot pass the sash directly to each other. Find minimum total time, or -1 if impossible.

#### Core Invariant & Observation
Store forbidden handoffs in a 2D boolean adjacency matrix bad[u][v]. Check bad[p_k][p_{k+1}] in O(1) during permutation traversal.

#### Algorithmic Formulation
1. Initialize p = {0, 1, ..., N - 1}.
2. bad[X_k][Y_k] = bad[Y_k][X_k] = true.
3. Loop permutations with std::next_permutation:
   - Check if any adjacent pair has bad[p_k][p_{k+1}] == true.
   - If valid, sum A[p_k][k] and update minimum total time.
4. Output min time or -1.

**Complexity**: `Time: O(N! * N), Space: O(N^2).`  
**Editorial Alignment**: Full permutation traversal with O(1) graph adjacency verification.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Permutation generation with std::next_permutation and Hamiltonian path filtering on small graphs.
- **Reusable Pattern**: `Permutation Generation with Adjacency Graph Validation.`

---

[Back to Master Categories](../../README.md)
