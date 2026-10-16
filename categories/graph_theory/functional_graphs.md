# 📖 Cycle Detection & Periodicity on Functional Graphs (Rho Algorithm)

- **Tag / Domain**: `Graph Theory`
- **Subtopic**: `Functional Graphs`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Cycle Detection & Periodicity on Functional Graphs (Rho Algorithm)**.

---

## 🏆 Curated High-Value Problems

### Original Calculator (`[problem:AtCoder-typical90_bf]`)

- **Role**: *Cycle Detection & Periodicity on Functional Graphs (Rho Algorithm)*
- **Rating**: `1250` (★4) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_bf)
- **Full Analysis**: [AtCoder-typical90_bf Analysis](../../analysis/AtCoder-typical90_bf.md)

#### Problem Statement & Task
A calculator displays integer x (0 <= x < 10^5). Pressing button replaces x with (x + digit_sum(x)) mod 10^5. Find display value after K presses (K <= 10^18).

#### Core Invariant & Observation
Track visited step indices step[x]. When a state repeats, the path consists of a pre-period tail of length t and a cycle of length c. For K >= t, remaining steps modulo c gives the exact state in O(MOD) time.

#### Algorithmic Formulation
1. Maintain pos[x] = -1.
2. Simulate step by step, storing history array.
3. If state repeats at step i with previous visit pos[x]: cycle_len = i - pos[x], tail_len = pos[x].
4. If K < tail_len: return history[K].
5. Else: return history[tail_len + (K - tail_len) % cycle_len].

**Complexity**: `Time: O(M) where M = 10^5, Space: O(M).`  
**Editorial Alignment**: Cycle detection on functional graph with periodic loop index calculation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Functional graphs, tail-and-cycle decomposition (Floyd's/Brent's idea), and large step exponentiation via modulo.
- **Reusable Pattern**: `Functional Graph Cycle Detection.`

---

[Back to Master Categories](../../README.md)
