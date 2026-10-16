# Problem Analysis: AtCoder-typical90_ae — VS AtCoder

**Problem ID**: `AtCoder-typical90_ae`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 031)  
**Rating / Difficulty**: 2150 (★6)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ae  
**VJudge Tag**: `[problem:AtCoder-typical90_ae]`  
**Category File**: [`../categories/game_theory/sprague_grundy_impartial_games.md`](../categories/game_theory/sprague_grundy_impartial_games.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Sprague-Grundy Theorem on Multi-Pile Impartial Games`  

---

## 1. Problem Statement & Key Idea
N independent piles with white stones W_i <= 50 and blue stones B_i <= 50. Turn moves: (1) change (W, B) to (W - 1, B + W) if W >= 1; or (2) change (W, B) to (W, B - k) for 1 <= k <= B / 2 if B >= 2. Determine if First or Second player wins under optimal play.

**Core Idea**: Independent impartial games combined via Sprague-Grundy theorem. Total game is Winning iff XOR sum of Grundy values of all piles is > 0.

## 2. Core Observation & Invariant
Precompute 2D Grundy values G[w][b] using minimum excluded value (mex) of all reachable transition states. Maximum blue stones reaches <= 50 + sum(1..50) = 1325. Precomputation runs in O(W * B^2) in < 0.05s.

## 3. Step-by-Step Algorithm
1. 2D array G[55][1500] = 0.
2. Fill G[w][b] by increasing w and b using mex of transitions: (w - 1, b + w) and (w, b - k) for 1 <= k <= b / 2.
3. Compute xor_sum = G[W_1][B_1] ^ ... ^ G[W_N][B_N].
4. If xor_sum != 0 output 'First' else 'Second'.

## 4. Complexity Analysis
Time: O(W_max * B_max^2 + N), Space: O(W_max * B_max).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <set>

using namespace std;

const int MAXW = 51;
const int MAXB = 1500;
int G[MAXW][MAXB];

void precompute() {
    for (int w = 0; w < MAXW; ++w) {
        for (int b = 0; b < MAXB; ++b) {
            vector<bool> vis(MAXB, false);
            // Move 1: (w - 1, b + w)
            if (w >= 1 && b + w < MAXB) {
                vis[G[w - 1][b + w]] = true;
            }
            // Move 2: (w, b - k) for 1 <= k <= b / 2
            for (int k = 1; k <= b / 2; ++k) {
                vis[G[w][b - k]] = true;
            }
            // Mex
            int mex = 0;
            while (vis[mex]) mex++;
            G[w][b] = mex;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    precompute();

    int n;
    if (!(cin >> n)) return 0;

    vector<int> w(n), b(n);
    for (int i = 0; i < n; ++i) cin >> w[i];
    for (int i = 0; i < n; ++i) cin >> b[i];

    int xor_sum = 0;
    for (int i = 0; i < n; ++i) {
        xor_sum ^= G[w[i]][b[i]];
    }

    if (xor_sum != 0) {
        cout << "First\n";
    } else {
        cout << "Second\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Sprague-Grundy theorem with 2D state mex precomputation.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Multi-pile impartial game decomposition, 2D Grundy mex induction, and Nim-sum winning condition.
- **Reusable Pattern**: `Sprague-Grundy Theorem with Mex Table Precomputation.`

---
Back to [Sprague-Grundy Theorem on Multi-Pile Impartial Games](../categories/game_theory/sprague_grundy_impartial_games.md) | [Categories Directory](../categories/README.md)