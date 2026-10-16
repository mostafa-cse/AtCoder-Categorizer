# 📖 Maximum Weight Closure / Project Selection Problem via Min-Cut

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Network Flow`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Maximum Weight Closure / Project Selection Problem via Min-Cut**.

---

## 🏆 Curated High-Value Problems

### Get More Money (`[problem:AtCoder-typical90_an]`)

- **Role**: *Maximum Weight Closure / Project Selection Problem via Min-Cut*
- **Rating**: `2550` (★7) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_an)
- **Full Analysis**: [AtCoder-typical90_an Analysis](../../analysis/AtCoder-typical90_an.md)

#### Problem Statement & Task
N houses with burglary alarms awarding reward A_i. Unlocking house i costs key price W. Opening house i requires owning keys for a prerequisite set of houses C_{i, j}. Find maximum net profit.

#### Core Invariant & Observation
Net profit = A_i - W. Positive rewards connect from Source S to node i with capacity A_i. Costs connect from node i to Sink T with capacity W. Dependency i -> j has infinite capacity. Max Profit = sum(positive A_i) - MinCut.

#### Algorithmic Formulation
1. Build flow network: S -> i with cap A_i; i -> T with cap W; i -> j with cap INF for all prerequisites.
2. Run Dinic's Algorithm to find Max-Flow (equal to Min-Cut).
3. Output sum(positive A_i) - max_flow.

**Complexity**: `Time: O(V^2 E) with Dinic, fast in practice, Space: O(V + E).`  
**Editorial Alignment**: Project selection / maximum weight closure reduction to minimum cut.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Network flow modeling, Project Selection Problem, and Dinic's algorithm.
- **Reusable Pattern**: `Project Selection / Max-Weight Closure via Min-Cut.`

---

[Back to Master Categories](../../README.md)
