# Problem Analysis: AtCoder-dp_k — Stones

**Problem ID**: `AtCoder-dp_k`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1100  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_k  
**VJudge Tag**: `[problem:AtCoder-dp_k]`  
**Category File**: [`../categories/game_theory/sprague_grundy_impartial_games.md`](../categories/game_theory/sprague_grundy_impartial_games.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Impartial Games`  
- **Topic (Skill)**: `Sprague-Grundy / Combinatorial Game DP`  

---

## 1. Problem Statement & Key Idea
Two players remove a_i stones from a pile of size K. Determine if First or Second player wins under optimal play.

**Core Idea**: State x is Winning (First wins) if there exists a valid move a_i such that state x - a_i is Losing (Second wins). If all valid moves lead to Winning states, x is Losing.

## 2. Core Observation & Invariant
Game state graph is finite and directed acyclic. Backward induction computes boolean outcomes in O(N * K).

## 3. Step-by-Step Algorithm
1. dp[0] = False (Losing state).
2. For x from 1 to K: dp[x] = True if any(a_i <= x and not dp[x - a_i] for a_i in A) else False.
3. Output 'First' if dp[K] else 'Second'.

## 4. Complexity Analysis
Time: O(N * K), Space: O(K).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    vector<bool> dp(k + 1, false);
    for (int x = 1; x <= k; ++x) {
        for (int v : a) {
            if (v <= x && !dp[x - v]) {
                dp[x] = true;
                break;
            }
        }
    }

    cout << (dp[k] ? "First" : "Second") << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Classic backward induction on impartial game graph.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: P-positions and N-positions, finite state game backward induction, and Sprague-Grundy fundamentals.
- **Reusable Pattern**: `Boolean game state induction: win(x) = \exists a, 
eg win(x - a).`

---
Back to [Sprague-Grundy / Combinatorial Game DP](../categories/game_theory/sprague_grundy_impartial_games.md) | [Categories Directory](../categories/README.md)