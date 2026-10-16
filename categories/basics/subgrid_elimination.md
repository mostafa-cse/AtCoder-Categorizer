# 📖 Corner-First Unique Determinism / 2x2 Subgrid Elimination

- **Tag / Domain**: `Basics`
- **Subtopic**: `Greedy & Invariants`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Corner-First Unique Determinism / 2x2 Subgrid Elimination**.

---

## 🏆 Curated High-Value Problems

### Two by Two (`[problem:AtCoder-typical90_ca]`)

- **Role**: *Corner-First Unique Determinism / 2x2 Subgrid Elimination*
- **Rating**: `850` (★3) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ca)
- **Full Analysis**: [AtCoder-typical90_ca Analysis](../../analysis/AtCoder-typical90_ca.md)

#### Problem Statement & Task
H x W matrices A and B. In one operation, add +-1 to any 2x2 subgrid. Can A be transformed to B, and what is the minimum operations?

#### Core Invariant & Observation
Process greedily in row-major order: at cell (r, c), diff = B_{r, c} - A_{r, c}. Apply diff to the 2x2 subgrid. After all (H-1)*(W-1) steps, verify if the remaining last row and last column match B.

#### Algorithmic Formulation
1. ops = 0.
2. For r from 0 to H - 2: for c from 0 to W - 2:
   - diff = B[r][c] - A[r][c]
   - ops += abs(diff)
   - Add diff to A[r][c], A[r+1][c], A[r][c+1], A[r+1][c+1].
3. If A == B: output 'Yes' and ops; else 'No'.

**Complexity**: `Time: O(H * W), Space: O(H * W).`  
**Editorial Alignment**: Corner-first unique deterministic greedy elimination.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Deterministic cascade elimination in grid operations and invariant propagation.
- **Reusable Pattern**: `Corner-First Deterministic Elimination.`

---

[Back to Master Categories](../../README.md)
