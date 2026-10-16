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


### VS AtCoder (`[problem:AtCoder-typical90_ae]`)

- **Role**: *Sprague-Grundy Theorem on Multi-Pile Impartial Games*
- **Rating**: `2150` (★6) | **Contest**: [`typical90`](https://atcoder.jp/contests/typical90/tasks/typical90_ae)
- **Full Analysis**: [AtCoder-typical90_ae Analysis](../../analysis/AtCoder-typical90_ae.md)

#### Problem Statement & Task
N independent piles with white stones W_i <= 50 and blue stones B_i <= 50. Turn moves: (1) change (W, B) to (W - 1, B + W) if W >= 1; or (2) change (W, B) to (W, B - k) for 1 <= k <= B / 2 if B >= 2. Determine if First or Second player wins under optimal play.

#### Core Invariant & Observation
Precompute 2D Grundy values G[w][b] using minimum excluded value (mex) of all reachable transition states. Maximum blue stones reaches <= 50 + sum(1..50) = 1325. Precomputation runs in O(W * B^2) in < 0.05s.

#### Algorithmic Formulation
1. 2D array G[55][1500] = 0.
2. Fill G[w][b] by increasing w and b using mex of transitions: (w - 1, b + w) and (w, b - k) for 1 <= k <= b / 2.
3. Compute xor_sum = G[W_1][B_1] ^ ... ^ G[W_N][B_N].
4. If xor_sum != 0 output 'First' else 'Second'.

**Complexity**: `Time: O(W_max * B_max^2 + N), Space: O(W_max * B_max).`  
**Editorial Alignment**: Sprague-Grundy theorem with 2D state mex precomputation.  

#### What This Teaches & Reusable Pattern
- **Skill Taught**: Multi-pile impartial game decomposition, 2D Grundy mex induction, and Nim-sum winning condition.
- **Reusable Pattern**: `Sprague-Grundy Theorem with Mex Table Precomputation.`

---

[Back to Game Theory Index](README.md) |
