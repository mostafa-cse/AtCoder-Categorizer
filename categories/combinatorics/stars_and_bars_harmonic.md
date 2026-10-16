# 📖 Spacing Constraint Combinatorics + Harmonic Series O(N log N)

- **Tag / Domain**: `Combinatorics`
- **Subtopic**: `Stars and Bars & Combinatorial Bounds`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Spacing Constraint Combinatorics + Harmonic Series O(N log N)**.

---

## 🏆 Curated High-Value Problems

### Don't be too close (`[problem:AtCoder-typical90_o]`)

- **Role**: *Spacing Constraint Combinatorics + Harmonic Series O(N log N)*
- **Rating**: `2150` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_o)
- **Full Analysis**: [AtCoder-typical90_o Analysis](../../analysis/AtCoder-typical90_o.md)

#### Problem Statement & Task
For each k from 1 to N, count non-empty subsets of {1, 2, ..., N} such that any two chosen elements have absolute difference >= k. Output modulo 10^9+7.

#### Core Invariant & Observation
For fixed k, max elements m <= ceil(N/k). Summing m over all k in [1, N] gives sum_{k=1}^N (N/k) = O(N log N) total evaluations!

#### Algorithmic Formulation
1. Precompute factorials and inverse factorials up to N.
2. For each k from 1 to N:
   - ans = 0
   - for m from 1 to (N + k - 1) / k:
     - total_items = N - (k - 1) * (m - 1)
     - if total_items >= m: ans = (ans + nCr(total_items, m)) % MOD
   - Output ans.

**Complexity**: `Time: O(N log N), Space: O(N).`  
**Editorial Alignment**: Stars and bars reduction with harmonic series complexity bound.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Spacing constraint bijection to standard combinations and bounding loop iterations via harmonic series.
- **Reusable Pattern**: `Combinatorial spacing reduction + Harmonic Series loop.`

---

[Back to Master Categories](../../README.md)
