# ⚡ AtCoder Curriculum: Basics

Curated collection of high-value problems in **Basics** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.

- **Total Curated Problems**: 2
- **Taxonomy Tier**: Tag (Domain Level)

---

## 📑 Table of Contents

- [Binary Search](#binary-search)
  - [Binary Search on Answer / Greedy Feasibility](#binary-search-on-answer--greedy-feasibility) (1 problems)
- [Implementation / Simulation](#implementation--simulation)
  - [Dual Index Mapping (Value-to-Position & Position-to-Value)](#dual-index-mapping-value-to-position--position-to-value) (1 problems)

---

## Binary Search

### Binary Search on Answer / Greedy Feasibility

#### Yokan Party (`[problem:AtCoder-typical90_a]`)
- **Rating / Difficulty**: 1200
- **Contest**: `typical90` | [AtCoder Link](https://atcoder.jp/contests/typical90/tasks/typical90_a)
- **Detailed Analysis**: [`analysis/AtCoder-typical90_a.md`](../analysis/AtCoder-typical90_a.md)
- **Key Idea**: Cut a stick of length L at K positions to maximize the length of the shortest piece.
- **Core Observation**: 'Maximize the minimum' is the definitive indicator for Binary Search on Answer. The predicate 'Can we obtain at least K+1 pieces each of length >= M?' is strictly monotonic with respect to M.
- **Algorithm & Complexity**: Time: O(N log L), Space: O(1).
- **What This Problem Teaches**: Formulating feasibility predicates, establishing monotonicity, and greedy cut verification.
- **Reusable Pattern**: `Binary search on answer + greedy feasibility check.`

---

## Implementation / Simulation

### Dual Index Mapping (Value-to-Position & Position-to-Value)

#### Adjacent Swaps (`[problem:AtCoder-abc250_c]`)
- **Rating / Difficulty**: 800
- **Contest**: `abc250` | [AtCoder Link](https://atcoder.jp/contests/abc250/tasks/abc250_c)
- **Detailed Analysis**: [`analysis/AtCoder-abc250_c.md`](../analysis/AtCoder-abc250_c.md)
- **Key Idea**: Perform Q swaps where each query swaps the ball with integer x and its right neighbor (or left neighbor if at boundary).
- **Core Observation**: Finding ball x in an array of size N naively takes O(N) per query. Maintaining two arrays: `val_at[pos]` and `pos_of[val]` allows locating and swapping in O(1).
- **Algorithm & Complexity**: Time: O(Q), Space: O(N).
- **What This Problem Teaches**: O(1) bidirectional lookup mapping and maintaining invertible permutations under swap operations.
- **Reusable Pattern**: `Dual index mapping (Position <-> Value).`

---
