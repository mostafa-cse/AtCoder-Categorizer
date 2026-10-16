# 📖 Reverse Topological / Reverse Graph BFS Ordering

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Reverse Graph & BFS`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Reverse Topological / Reverse Graph BFS Ordering**.

---

## 🏆 Curated High-Value Problems

### Paint All (`[problem:AtCoder-typical90_bj]`)

- **Role**: *Reverse Topological / Reverse Graph BFS Ordering*
- **Rating**: `2100` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bj)
- **Full Analysis**: [AtCoder-typical90_bj Analysis](../../analysis/AtCoder-typical90_bj.md)

#### Problem Statement & Task
N balls initially white. Ball i can be painted black if ball A_i or B_i is already painted black, or unconditionally if A_i == i or B_i == i. Find an order to paint all balls black, or report -1 if impossible.

#### Core Invariant & Observation
Construct reverse graph: directed edges A_i -> i and B_i -> i. Start a BFS from all balls with self-loops (A_i == i or B_i == i). Once ball u is reached, it enables any ball v having u as a prerequisite. Reversing the BFS traversal order gives the exact valid painting sequence!

#### Algorithmic Formulation
1. Build reverse adjacency list: rev[A_i].push_back(i) and rev[B_i].push_back(i).
2. Push all nodes with A_i == i or B_i == i into BFS queue.
3. Run BFS, recording visited vertices in an order list.
4. If order.size() < N, output -1.
5. Else, reverse(order) and print the sequence.

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: Backward BFS on prerequisite activation graph.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Reverse thinking, backward graph reachability, and topological activation ordering.
- **Reusable Pattern**: `Reverse Graph Activation BFS.`

---

[Back to Master Categories](../../README.md)
