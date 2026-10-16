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


### Uplift (`[problem:AtCoder-typical90_bl]`)

- **Role**: *Difference Array Local Perturbation for O(1) Range Update Inconvenience*
- **Rating**: `800` (★3) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bl)
- **Full Analysis**: [AtCoder-typical90_bl Analysis](../../analysis/AtCoder-typical90_bl.md)

#### Problem Statement & Task
Array A of length N. Total inconvenience is sum_{i=1}^{N-1} |A_{i+1} - A_i|. Q queries: add V to range [L, R]. Print total inconvenience after each query.

#### Core Invariant & Observation
Update total inconvenience in O(1) time per query by subtracting |D_old| and adding |D_new| at indices L-1 and R.

#### Algorithmic Formulation
1. Compute D_i = A_{i+1} - A_i and initial total_inconvenience = sum |D_i|.
2. For each query (L, R, V):
   - If L > 1: subtract |D_{L-1}|, D_{L-1} += V, add |D_{L-1}|.
   - If R < N: subtract |D_R|, D_R -= V, add |D_R|.
   - Print total_inconvenience.

**Complexity**: `Time: O(N + Q), Space: O(N).`  
**Editorial Alignment**: Difference array local perturbation update in O(1).  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Maintaining global objective functions under range additions via difference array boundary perturbation.
- **Reusable Pattern**: `Difference Array Boundary Perturbation.`

---


### Friendly Group (`[problem:AtCoder-typical90_cc]`)

- **Role**: *2D Prefix Sums for Bounded Window Maximization*
- **Rating**: `1750` (★5) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_cc)
- **Full Analysis**: [AtCoder-typical90_cc Analysis](../../analysis/AtCoder-typical90_cc.md)

#### Problem Statement & Task
N students with height A_i <= 5000 and weight B_i <= 5000. Find maximum students in a group with max_A - min_A <= K and max_B - min_B <= K.

#### Core Invariant & Observation
Compute 2D prefix sums on the coordinate grid. Slide a (K + 1) x (K + 1) window over all positions to find the maximum sum in O(M^2) where M = 5000.

#### Algorithmic Formulation
1. Build count[A_i][B_i]++.
2. Compute 2D prefix sums pref[r][c].
3. Loop r from 1 to 5000, c from 1 to 5000: query sum in rectangle [r, min(5000, r + K)] x [c, min(5000, c + K)].
4. Output max rectangle sum.

**Complexity**: `Time: O(N + M^2) where M = 5000, Space: O(M^2).`  
**Editorial Alignment**: 2D prefix sums for sliding bounding-box query maximization.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: 2D Prefix sums, coordinate discretization, and 2D sliding window maximization.
- **Reusable Pattern**: `2D Prefix Sum Window Maximization.`

---

[Back to Master Categories](../../README.md)
