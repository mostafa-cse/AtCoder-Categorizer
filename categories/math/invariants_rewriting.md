# 📖 Binary Positional Weight Invariant on String Rewriting

- **Tag / Domain**: `Math`
- **Subtopic**: `Invariants & Monoids`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Binary Positional Weight Invariant on String Rewriting**.

---

## 🏆 Curated High-Value Problems

### ABC String 2 (`[problem:AtCoder-typical90_bv]`)

- **Role**: *Binary Positional Weight Invariant on String Rewriting*
- **Rating**: `2100` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bv)
- **Full Analysis**: [AtCoder-typical90_bv Analysis](../../analysis/AtCoder-typical90_bv.md)

#### Problem Statement & Task
String of length N over {'a', 'b', 'c'}. Operation replaces 'b' with 'aa' and 'c' with 'bb'. Total operations until only 'a' remains.

#### Core Invariant & Observation
A character at position i (0-indexed) has positional weight 2^i. Total operations is exactly sum_{i=0}^{N-1} val(S[i]) * 2^i.

#### Algorithmic Formulation
1. total = 0.
2. For i from 0 to N - 1:
   - val = (S[i] == 'a' ? 0 : (S[i] == 'b' ? 1 : 2))
   - total += val * (1ULL << i)
3. Output total.

**Complexity**: `Time: O(N), Space: O(1).`  
**Editorial Alignment**: Positional binary invariant on string rewriting rules.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Mathematical invariants in term rewriting systems and binary counter reductions.
- **Reusable Pattern**: `Binary Counter Rewriting Invariant.`

---

[Back to Master Categories](../../README.md)
