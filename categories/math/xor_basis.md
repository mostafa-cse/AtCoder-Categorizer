# 📖 Gaussian Elimination over GF(2) / XOR Basis for Linear Systems

- **Tag / Domain**: `Math`
- **Subtopic**: `Linear Algebra & Basis`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Gaussian Elimination over GF(2) / XOR Basis for Linear Systems**.

---

## 🏆 Curated High-Value Problems

### Flip Flap (`[problem:AtCoder-typical90_be]`)

- **Role**: *Gaussian Elimination over GF(2) / XOR Basis for Linear Systems*
- **Rating**: `2200` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_be)
- **Full Analysis**: [AtCoder-typical90_be Analysis](../../analysis/AtCoder-typical90_be.md)

#### Problem Statement & Task
N switches, M bulbs. Switch i toggles a subset of bulbs. Target state S specifies desired on/off states for each bulb. Count combinations of switch presses that achieve target S modulo 998244353.

#### Core Invariant & Observation
Each switch is an M-bit vector over GF(2). Insert switches into an XOR basis of size M. If target S reduces to 0 using the basis, the number of solutions is 2^(N - rank) mod 998244353; otherwise 0.

#### Algorithmic Formulation
1. Represent each switch as a bitset of length M.
2. Insert each switch into XOR basis.
3. Reduce target vector S using the basis.
4. If S != 0: output 0.
5. Else: output 2^(N - rank) % 998244353.

**Complexity**: `Time: O(N * M^2 / 64), Space: O(N * M).`  
**Editorial Alignment**: Gaussian elimination over GF(2) with vector basis reduction.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: XOR Basis, linear systems over finite fields, and kernel dimension solution counting.
- **Reusable Pattern**: `GF(2) Gaussian Elimination & XOR Basis.`

---

[Back to Master Categories](../../README.md)
