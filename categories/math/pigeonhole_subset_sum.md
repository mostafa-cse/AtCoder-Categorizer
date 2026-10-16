# 📖 Pigeonhole Principle Collision Search on Subset Sums

- **Tag / Domain**: `Math`
- **Subtopic**: `Pigeonhole Principle`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Pigeonhole Principle Collision Search on Subset Sums**.

---

## 🏆 Curated High-Value Problems

### Similar but Different Ways (`[problem:AtCoder-typical90_cj]`)

- **Role**: *Pigeonhole Principle Collision Search on Subset Sums*
- **Rating**: `2150` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_cj)
- **Full Analysis**: [AtCoder-typical90_cj Analysis](../../analysis/AtCoder-typical90_cj.md)

#### Problem Statement & Task
N <= 88 cards with values A_i <= 88. Q incompatible pairs. Find TWO distinct valid subsets of cards having identical sum of values.

#### Core Invariant & Observation
By the Pigeonhole Principle, a collision (two subsets with identical sum) MUST exist! Run DFS backtracking to collect subsets; store the first subset reaching each sum in an array. The moment a sum collides, terminate and output both subsets!

#### Algorithmic Formulation
1. Backtracking DFS(card_idx, cur_sum, chosen_subset).
2. If cur_sum already seen in memo: output memo[cur_sum] and chosen_subset, terminate immediately.
3. Else: memo[cur_sum] = chosen_subset.
4. Branch: include card (if compatible with chosen) or skip card.

**Complexity**: `Time: O(MaxSum * N) <= 7744 * 88 ops (< 0.05s), Space: O(MaxSum * N).`  
**Editorial Alignment**: Pigeonhole Principle collision search on bounded subset sum capacity.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Pigeonhole Principle guarantee of collisions, early termination search, and hashing subset sum states.
- **Reusable Pattern**: `Pigeonhole Principle Subset Sum Collision.`

---

[Back to Master Categories](../../README.md)
