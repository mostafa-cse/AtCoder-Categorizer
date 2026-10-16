# 📖 Virtual Circular Array Shift via Modulo Pointer Offset

- **Tag / Domain**: `Basics`
- **Subtopic**: `Array Transformations`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Virtual Circular Array Shift via Modulo Pointer Offset**.

---

## 🏆 Curated High-Value Problems

### Shift and Swapping (`[problem:AtCoder-typical90_ar]`)

- **Role**: *Virtual Circular Array Shift via Modulo Pointer Offset*
- **Rating**: `800` (★3) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ar)
- **Full Analysis**: [AtCoder-typical90_ar Analysis](../../analysis/AtCoder-typical90_ar.md)

#### Problem Statement & Task
Array of length N, Q queries: (1) swap A_x and A_y; (2) shift array right circularly A = (A_N, A_1, ..., A_{N-1}); (3) print A_x.

#### Core Invariant & Observation
A right shift moves the virtual start position back by 1: shift = (shift - 1 + N) % N. Array index x maps to real index (x + shift) % N in O(1).

#### Algorithmic Formulation
1. shift = 0.
2. Query 1: swap A[(x + shift) % N] and A[(y + shift) % N].
3. Query 2: shift = (shift - 1 + N) % N.
4. Query 3: print A[(x + shift) % N].

**Complexity**: `Time: O(Q), Space: O(N).`  
**Editorial Alignment**: Pointer offset virtualization for O(1) circular array shift.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Virtual array rotation using modulo index mapping without moving data.
- **Reusable Pattern**: `Virtual Circular Pointer Offset.`

---

[Back to Master Categories](../../README.md)
