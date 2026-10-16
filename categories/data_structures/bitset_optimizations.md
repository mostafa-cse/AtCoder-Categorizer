# 📖 Batch Bitset Acceleration on DAG Reachability Queries

- **Tag / Domain**: `Data Structures (DS)`
- **Subtopic**: `Bitset Optimization`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Batch Bitset Acceleration on DAG Reachability Queries**.

---

## 🏆 Curated High-Value Problems

### Many Graph Queries (`[problem:AtCoder-typical90_bg]`)

- **Role**: *Batch Bitset Acceleration on DAG Reachability Queries*
- **Rating**: `2600` (★7) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bg)
- **Full Analysis**: [AtCoder-typical90_bg Analysis](../../analysis/AtCoder-typical90_bg.md)

#### Problem Statement & Task
Directed Acyclic Graph (DAG) with N <= 60000 vertices, M <= 100000 edges. Q <= 100000 queries: can A_i reach B_i? Output 'Yes' or 'No' for each query.

#### Core Invariant & Observation
Group queries into batches of size W = 64. For each batch, dp[u] is a 64-bit integer representing reachability to the target of query q in the batch. Propagate backwards along topological order.

#### Algorithmic Formulation
1. Topologically sort vertices.
2. Divide Q queries into chunks of 64.
3. For each chunk: initialize dp[target_q] |= (1ULL << q).
4. In reverse topological order: dp[u] = OR_{v in adj[u]} dp[v].
5. Check if dp[start_q] has bit q set.

**Complexity**: `Time: O((Q / 64) * (N + M)), Space: O(N + M).`  
**Editorial Alignment**: Batch-parallel 64-bit word bitset acceleration on topological DAG transitions.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Bit parallelism on word-level operations, batching queries, and topological reachability.
- **Reusable Pattern**: `Batch Bitset DAG Reachability.`

---

[Back to Master Categories](../../README.md)
