# 📖 Directed Graph Cycle Detection & Topological Sort

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Directed Graphs`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Modeling dependency relations and handle transitions as directed graphs and detecting cycles via Kahn's algorithm or 3-color DFS.

---

## 🏆 Curated High-Value Problems

### 1. Change of User Name (`[problem:AtCoder-abc285_d]`)

- **Role**: *Dependency Resolution via Cycle Detection*
- **Rating**: `950` | **Contest**: [`abc285`](https://atcoder.jp/contests/abc285/tasks/abc285_d)
- **Full Analysis**: [AtCoder-abc285_d Analysis](../../analysis/AtCoder-abc285_d.md)

#### Problem Statement & Task
N users want to change their handles from S_i to T_i. Determine if all changes can be performed without collisions.

#### Core Invariant & Observation
A directed cycle forms a deadlock where no user in the cycle can change without overwriting another user's existing handle.

#### Algorithmic Formulation
1. Build adjacency list of directed edges S_i -> T_i.
2. Compute in-degrees and perform Kahn's Topological Sort.
3. If all nodes can be topologically sorted, output 'Yes'; else 'No'.

**Complexity**: `Time: O(N), Space: O(N).`  
**Editorial Alignment**: Topological sort cycle check on string handle transitions.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Modeling sequential dependencies as directed graph cycles and topological ordering.
- **Reusable Pattern**: `Topological sort cycle detection for dependency resolution.`

---

[Back to Graph Theory Index](README.md) | [Back to Master Categories](../../README.md)
