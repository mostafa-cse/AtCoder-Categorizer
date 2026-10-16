# 📖 2D Imos Method / 2D Difference Array

- **Tag / Domain**: `Data Structures (DS)`
- **Subtopic**: `Prefix Sums & Difference Arrays`

---

## 💡 Topic Overview
High-value competitive programming techniques for **2D Imos Method / 2D Difference Array**.

---

## 🏆 Curated High-Value Problems

### Cluttered Paper (`[problem:AtCoder-typical90_ab]`)

- **Role**: *2D Imos Method / 2D Difference Array*
- **Rating**: `1300` (★4) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ab)
- **Full Analysis**: [AtCoder-typical90_ab Analysis](../../analysis/AtCoder-typical90_ab.md)

#### Problem Statement & Task
N axis-aligned sheets of paper are placed on a 1000 x 1000 grid. Each rectangle covers [lx, rx) x [ly, ry). For each k from 1 to N, calculate the total area covered by exactly k sheets.

#### Core Invariant & Observation
For each rectangle [lx, rx) x [ly, ry), add +1 at (lx, ly) and (rx, ry), and -1 at (lx, ry) and (rx, ly). A 2D prefix sum over rows and columns reconstructs all cell coverage counts in O(W^2).

#### Algorithmic Formulation
1. Initialize D[1005][1005] = 0.
2. For each rectangle: D[lx][ly]++; D[rx][ry]++; D[lx][ry]--; D[rx][ly]--;
3. Prefix sum rows: D[x][y] += D[x-1][y].
4. Prefix sum cols: D[x][y] += D[x][y-1].
5. Count frequency of each k in 1..N and output.

**Complexity**: `Time: O(N + W^2), Space: O(W^2) where W = 1000.`  
**Editorial Alignment**: 2D Imos method for cumulative 2D rectangle additions.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: 2D Difference arrays (Imos method), 2D prefix accumulation, and O(1) rectangle range updates.
- **Reusable Pattern**: `2D Imos Difference Array.`

---

[Back to Master Categories](../../README.md)
