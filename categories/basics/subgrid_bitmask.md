# 📖 Subgrid Dimension Reduction / Row Bitmask with Column Frequency Counting

- **Tag / Domain**: `Basics`
- **Subtopic**: `Bitmask Enumeration & Pruning`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Subgrid Dimension Reduction / Row Bitmask with Column Frequency Counting**.

---

## 🏆 Curated High-Value Problems

### Monochromatic Subgrid (`[problem:AtCoder-typical90_bk]`)

- **Role**: *Subgrid Dimension Reduction / Row Bitmask with Column Frequency Counting*
- **Rating**: `1250` (★4) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bk)
- **Full Analysis**: [AtCoder-typical90_bk Analysis](../../analysis/AtCoder-typical90_bk.md)

#### Problem Statement & Task
H x W grid (H <= 8, W <= 10^4). Select a subset of rows and columns such that all cells in the subgrid have the same integer. Maximize the number of cells in the subgrid.

#### Core Invariant & Observation
For a fixed subset of rows, column c is valid iff all chosen rows have identical value V = grid[r_first][c]. Count frequencies of valid values across all W columns; the max frequency gives the optimal column subset for this row mask.

#### Algorithmic Formulation
1. Loop mask from 1 to 2^H - 1.
2. For each column c: check if all rows in mask have same value V. If so, freq[V]++.
3. Max cells = popcount(mask) * max(freq.values()).
4. Return maximum over all 2^H - 1 masks.

**Complexity**: `Time: O(2^H * H * W), Space: O(H * W).`  
**Editorial Alignment**: Row bitmask brute force with linear column frequency counting.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Exploiting asymmetric dimensions (H <= 8 vs W <= 10^4) via bitmask state reduction.
- **Reusable Pattern**: `Asymmetric Dimension Reduction via Bitmask.`

---

[Back to Master Categories](../../README.md)
