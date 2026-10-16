# ♟️ AtCoder Curriculum: Game Theory

Curated collection of high-value problems in **Game Theory** selected for teaching reusable competitive programming algorithms, structural observations, and mathematical invariants.

- **Total Curated Problems**: 1
- **Taxonomy Tier**: Tag (Domain Level)

---

## 📑 Table of Contents

- [Impartial Games](#impartial-games)
  - [Sprague-Grundy / Combinatorial Game DP](#sprague-grundy--combinatorial-game-dp) (1 problems)

---

## Impartial Games

### Sprague-Grundy / Combinatorial Game DP

#### Stones (`[problem:AtCoder-dp_k]`)
- **Rating / Difficulty**: 1100
- **Contest**: `dp` | [AtCoder Link](https://atcoder.jp/contests/dp/tasks/dp_k)
- **Detailed Analysis**: [`analysis/AtCoder-dp_k.md`](../analysis/AtCoder-dp_k.md)
- **Key Idea**: Two players take turns removing a_i stones from a pile of size K. Determine if First or Second player wins under optimal play.
- **Core Observation**: State x is Winning (First wins) if there exists a valid move a_i such that state x - a_i is Losing (Second wins). If all valid moves lead to Winning states, x is Losing.
- **Algorithm & Complexity**: Time: O(N * K), Space: O(K).
- **What This Problem Teaches**: P-positions and N-positions, finite state game backward induction, and Sprague-Grundy fundamentals.
- **Reusable Pattern**: `Boolean game state induction: win(x) = \exists a, 
eg win(x - a).`

---
