# 📖 Inclusion-Exclusion on Bitwise Constraints

- **Tag / Domain**: `Combinatorics`
- **Subtopic**: `Inclusion-Exclusion Principle`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Inclusion-Exclusion on Bitwise Constraints**.

---

## 🏆 Curated High-Value Problems

### Let's Share Bit (`[problem:AtCoder-typical90_cb]`)

- **Role**: *Inclusion-Exclusion on Bitwise Constraints*
- **Rating**: `2200` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_cb)
- **Full Analysis**: [AtCoder-typical90_cb Analysis](../../analysis/AtCoder-typical90_cb.md)

#### Problem Statement & Task
N bitmasks A_1, ..., A_N in [0, 2^D - 1] (N <= 20, D <= 60). Count integers x in [0, 2^D - 1] such that (x & A_i) != 0 for all i.

#### Core Invariant & Observation
For subset S of conditions, x & A_i = 0 for all i in S iff x & (OR_{i in S} A_i) == 0. Let M = OR_{i in S} A_i. The bits of x where M has 1 must be 0; remaining D - popcount(M) bits can be chosen freely (2^(D - popcount(M)) choices).

#### Algorithmic Formulation
1. Loop mask from 0 to 2^N - 1.
2. M = OR of A_i for i where mask has bit i.
3. ways = 1ULL << (D - popcount(M)).
4. If popcount(mask) is odd: ans -= ways; else ans += ways.
5. Output ans.

**Complexity**: `Time: O(N * 2^N), Space: O(N).`  
**Editorial Alignment**: Inclusion-Exclusion principle on bitwise OR condition negation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Inclusion-Exclusion Principle, bitwise independence, and bitmask subset iteration.
- **Reusable Pattern**: `Inclusion-Exclusion on Bitwise Constraints.`

---

[Back to Master Categories](../../README.md)
