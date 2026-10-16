# 📖 Recursive Backtracking & Prefix Balance Invariant

- **Tag / Domain**: `Basics`
- **Subtopic**: `Backtracking & Recursion`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Recursive Backtracking & Prefix Balance Invariant**.

---

## 🏆 Curated High-Value Problems

### Encyclopedia of Parentheses (`[problem:AtCoder-typical90_b]`)

- **Role**: *Recursive Backtracking & Prefix Balance Invariant*
- **Rating**: `800` (★3) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_b)
- **Full Analysis**: [AtCoder-typical90_b Analysis](../../analysis/AtCoder-typical90_b.md)

#### Problem Statement & Task
Print all valid parentheses strings of length N in lexicographical order. N <= 16.

#### Core Invariant & Observation
Since N <= 16 is small, recursive backtracking placing '(' before ')' naturally generates all Catalan(N/2) valid strings in strict lexicographical order without sorting.

#### Algorithmic Formulation
1. If N is odd, return immediately (no valid strings).
2. Recursive DFS(s, open_count, close_count):
   - If len(s) == N: output s.
   - If open_count < N/2: DFS(s + '(', open_count + 1, close_count).
   - If close_count < open_count: DFS(s + ')', open_count, close_count + 1).

**Complexity**: `Time: O(Catalan(N/2) * N), Space: O(N) recursion stack.`  
**Editorial Alignment**: Backtracking or bitmask simulation checking Dyck path prefix non-negativity.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Parenthesis validity invariants, Dyck paths, and lexicographical recursive search without sorting.
- **Reusable Pattern**: `Prefix balance invariant backtracking.`

---

[Back to Master Categories](../../README.md)
