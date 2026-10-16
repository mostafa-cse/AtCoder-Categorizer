# 📖 Grid Simple Cycle Search via DFS Backtracking (Small N <= 16)

- **Tag / Domain**: `Basics`
- **Subtopic**: `Backtracking & Recursion`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Grid Simple Cycle Search via DFS Backtracking (Small N <= 16)**.

---

## 🏆 Curated High-Value Problems

### Loop Railway Plan (`[problem:AtCoder-typical90_bt]`)

- **Role**: *Grid Simple Cycle Search via DFS Backtracking (Small N <= 16)*
- **Rating**: `1350` (★4) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bt)
- **Full Analysis**: [AtCoder-typical90_bt Analysis](../../analysis/AtCoder-typical90_bt.md)

#### Problem Statement & Task
H x W grid with empty cells '.' and walls '#' (H, W <= 16, H*W <= 16). Find a simple cycle of length >= 3 traversing only empty cells that maximizes cycle length, or -1 if no cycle exists.

#### Core Invariant & Observation
Iterate each non-wall cell as the cycle start (r0, c0). Run DFS marking visited cells. When reaching an adjacent neighbor that equals (r0, c0) with step >= 3, update max cycle length.

#### Algorithmic Formulation
1. For each cell (r, c): DFS(r, c, r0, c0, step).
2. If neighbor == (r0, c0) and step >= 3: max_cycle = max(max_cycle, step).
3. If neighbor unvisited and not wall: mark visited, DFS(nr, nc, r0, c0, step + 1), unmark visited.
4. Output max_cycle or -1.

**Complexity**: `Time: O(4^(HW)), extremely fast for HW <= 16 (< 0.02s), Space: O(HW).`  
**Editorial Alignment**: DFS backtracking cycle search on small bounded grid.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Grid cycle finding, backtracking state restoration, and constraint-based pruning.
- **Reusable Pattern**: `Grid Cycle Backtracking DFS.`

---

[Back to Master Categories](../../README.md)
