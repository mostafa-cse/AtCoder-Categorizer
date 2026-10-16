# 📖 Binary Search on Answer / Greedy Feasibility

- **Tag / Domain**: `Basics`
- **Subtopic**: `Binary Search`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Transforming optimization problems ('maximize the minimum' or 'minimize the maximum') into monotonic decision problems solved by binary search.

---

## 🏆 Curated High-Value Problems

### 1. Yokan Party (`[problem:AtCoder-typical90_a]`)

- **Role**: *The Canonical Maximize the Minimum Template*
- **Rating**: `1200` | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_a)
- **Full Analysis**: [AtCoder-typical90_a Analysis](../../analysis/AtCoder-typical90_a.md)

#### Problem Statement & Task
Cut a stick of length L at K positions to maximize the length of the shortest piece.

#### Core Invariant & Observation
The predicate 'Can we obtain at least K+1 pieces each of length >= M?' is monotonically decreasing with respect to M. Feasibility is verified greedily in O(N).

#### Algorithmic Formulation
1. Binary search M in [1, L].
2. check(M): Greedily cut whenever current piece length >= M. If total pieces cut is >= K and remaining piece >= M, return True; else False.
3. Upper boundary is the optimal answer.

**Complexity**: `Time: O(N log L), Space: O(1).`  
**Editorial Alignment**: Textbook binary search on answer.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Formulating feasibility predicates, establishing monotonicity, and greedy cut verification.
- **Reusable Pattern**: `Binary search on answer + greedy feasibility check.`

---

[Back to Basics Index](README.md) | [Back to Master Categories](../../README.md)
