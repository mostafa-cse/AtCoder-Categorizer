# 📖 Discrete Golden-Section / Fibonacci Search on Unimodal Functions

- **Tag / Domain**: `Basics`
- **Subtopic**: `Ternary Search & Optimization`

---

## 💡 Topic Overview
High-value competitive programming techniques for **Discrete Golden-Section / Fibonacci Search on Unimodal Functions**.

---

## 🏆 Curated High-Value Problems

### Discrete Dowsing (`[problem:AtCoder-typical90_ba]`)

- **Role**: *Discrete Golden-Section / Fibonacci Search on Unimodal Functions*
- **Rating**: `2600` (★7) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ba)
- **Full Analysis**: [AtCoder-typical90_ba Analysis](../../analysis/AtCoder-typical90_ba.md)

#### Problem Statement & Task
Interactive problem: array A of length N (N <= 1500) strictly increases then strictly decreases (strictly unimodal). Find the maximum value of A using at most 15 queries.

#### Core Invariant & Observation
Fibonacci numbers satisfy F_{k+1} = F_k + F_{k-1}. Pad the array to F_{16} = 1597. In each step, test two interior points at distances F_{k-1} and F_k from the boundary. One point is always carried over from the previous step!

#### Algorithmic Formulation
1. Pad array to size F_{16} = 1597 with -1.
2. Maintain active interval [L, R] of length F_k.
3. Place probes at L + F_{k-2} and L + F_{k-1}.
4. Compare values and contract interval to F_{k-1}.
5. Return maximum probed value.

**Complexity**: `Time: O(log_phi N) = 15 queries max, Space: O(N).`  
**Editorial Alignment**: Fibonacci search reusing interior function evaluations on unimodal functions.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Fibonacci / Golden Section search, query budget minimization, and unimodal optimization.
- **Reusable Pattern**: `Fibonacci Search on Unimodal Arrays.`

---

[Back to Master Categories](../../README.md)
