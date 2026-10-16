# Problem Analysis: AtCoder-dp_k — Stones

**Problem ID**: `AtCoder-dp_k`  
**Contest**: `dp`  
**Rating**: 1100  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_k  
**VJudge Tag**: `[problem:AtCoder-dp_k]`  
**Category File**: [`../categories/Game_Theory.md`](../categories/Game_Theory.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Impartial Games`  
- **Topic (Skill)**: `Sprague-Grundy / Combinatorial Game DP`  

---

## 1. Problem Statement & Key Idea
Two players take turns removing a_i stones from a pile of size K. Determine if First or Second player wins under optimal play.

## 2. Core Observation & Invariant
State x is Winning (First wins) if there exists a valid move a_i such that state x - a_i is Losing (Second wins). If all valid moves lead to Winning states, x is Losing.

## 3. Step-by-Step Algorithm
1. dp[0] = False (Losing state).
2. For x from 1 to K: dp[x] = True if any(a_i <= x and not dp[x - a_i] for a_i in A) else False.
3. Output 'First' if dp[K] else 'Second'.

## 4. Complexity Analysis
Time: O(N * K), Space: O(K).

## 5. Editorial Comparison & Alignment
Classic backward induction on impartial game graph.

## 6. What This Problem Teaches
P-positions and N-positions, finite state game backward induction, and Sprague-Grundy fundamentals.

## 7. Reusable Competitive Programming Pattern
`Boolean game state induction: win(x) = \exists a, 
eg win(x - a).`

---
Back to [Category: Game Theory](../categories/Game_Theory.md) | [Categories Index](../categories/README.md)