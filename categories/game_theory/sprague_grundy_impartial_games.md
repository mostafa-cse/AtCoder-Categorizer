# 📖 Sprague-Grundy & Impartial Game Induction

- **Tag / Domain**: `Game Theory`
- **Subtopic**: `Impartial Games`
- **Total Curated Problems**: 1

---

## 💡 Topic Overview
Finite impartial sequential games, normal play convention, P-positions (previous player winning) and N-positions (next player winning).

---

## 🏆 Curated High-Value Problems

### 1. Stones (`[problem:AtCoder-dp_k]`)

- **Role**: *Finite Game Backward Induction*
- **Rating**: `1100` | **Contest**: [`dp`](https://atcoder.jp/contests/dp/tasks/dp_k)
- **Full Analysis**: [AtCoder-dp_k Analysis](../../analysis/AtCoder-dp_k.md)

#### Problem Statement & Task
Two players remove a_i stones from a pile of size K. Determine if First or Second player wins under optimal play.

#### Core Invariant & Observation
Game state graph is finite and directed acyclic. Backward induction computes boolean outcomes in O(N * K).

#### Algorithmic Formulation
1. dp[0] = False (Losing state).
2. For x from 1 to K: dp[x] = True if any(a_i <= x and not dp[x - a_i] for a_i in A) else False.
3. Output 'First' if dp[K] else 'Second'.

**Complexity**: `Time: O(N * K), Space: O(K).`  
**Editorial Alignment**: Classic backward induction on impartial game graph.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: P-positions and N-positions, finite state game backward induction, and Sprague-Grundy fundamentals.
- **Reusable Pattern**: `Boolean game state induction: win(x) = \exists a, 
eg win(x - a).`

---

[Back to Game Theory Index](README.md) | [Back to Master Categories](../../README.md)
