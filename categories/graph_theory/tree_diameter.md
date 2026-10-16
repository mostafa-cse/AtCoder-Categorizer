# 📖 Tree Diameter via Double BFS/DFS

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Trees`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Finding the longest simple path in an unweighted or weighted tree using two consecutive breadth-first or depth-first searches.

---

## 🏆 Curated High-Value Problems

### 1. Longest Circular Road (`[problem:AtCoder-typical90_c]`)

- **Role**: *Canonical 2-Pass Tree Diameter*
- **Rating**: `1100` | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_c)
- **Full Analysis**: [AtCoder-typical90_c Analysis](../../analysis/AtCoder-typical90_c.md)

#### Problem Statement & Task
Add one edge between any two vertices in a tree to form the longest possible simple cycle.

#### Core Invariant & Observation
Running BFS from any arbitrary node 1 finds a node u on the diameter. Running a second BFS from u finds the opposite end v of the diameter.

#### Algorithmic Formulation
1. Run BFS from node 1 to find farthest node u.
2. Run BFS from u to find farthest node v. dist(u, v) is the tree diameter.
3. Output dist(u, v) + 1.

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: Two-pass BFS tree diameter proof.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Tree diameter characterization and the canonical 2-BFS algorithm.
- **Reusable Pattern**: `2-pass BFS tree diameter.`

---

[Back to Graph Theory Index](README.md) | [Back to Master Categories](../../README.md)
