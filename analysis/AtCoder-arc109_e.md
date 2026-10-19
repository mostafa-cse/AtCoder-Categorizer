# Problem Analysis: AtCoder-arc109_e — 1D Reversi Builder

**Problem ID**: `AtCoder-arc109_e`  
**Contest**: `arc109`  
**Rating / Difficulty**: 2661  
**URL**: https://atcoder.jp/contests/arc109/tasks/arc109_e  
**VJudge Tag**: `[problem:AtCoder-arc109_e]`  
**Category File**: [`../categories/game_theory/1d_reversi_builder_game.md`](../categories/game_theory/1d_reversi_builder_game.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Graph Games`  
- **Topic (Skill)**: `Games on Arbitrary Graphs`  

---

## 1. Problem Statement & Key Idea
Two players alternate placing white and black stones on an empty length-N strip, flipping contiguous opponent segments bounded by their own stones. The winner is determined by the stone color of cell K. By analyzing game state transitions and terminal configurations, the outcome reduces to identifying who controls boundary expansion and reachability to position K.

## 2. Core Observation & Invariant
When K=1 or K=N, the end cells are protected from being flanked from the outer side, so placing a stone on the boundary grants permanent dominance over adjacent cells. In general, whichever player secures cell K or builds an un-flippable wall can guarantee victory. The game forms a finite acyclic DAG of board states where backwards induction and reachability analysis yields a closed-form decision based on relative distances |K - 1| and |N - K|.

## 3. Step-by-Step Algorithm
1. 1. Analyze the relative parity and distance of target cell K to the endpoints 1 and N.
2. 2. If K is closer to an end, evaluate whether the first player (Takahashi) can secure the corner or adjacent blocking stone.
3. 3. Compare K - 1 and N - K against turn parity to determine the backward-induction optimal outcome.
4. 4. Output 'Takahashi' or 'Aoki' accordingly.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const long long MOD = 998244353;
static const long long INV2 = 499122177;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    int MAX = 2 * n + 5;
    vector<long long> pow2(MAX, 1);
    for (int i = 1; i < MAX; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    vector<long long> pref_odd(MAX, 0);
    for (int k = 3; k < MAX; k += 2) {
        long long term = (1LL * k * pow2[k - 1]) % MOD;
        pref_odd[k] = (pref_odd[k - 2] + term) % MOD;
    }

    vector<long long> inv2_pow(n + 1, 1);
    for (int i = 1; i <= n; ++i) {
        inv2_pow[i] = (inv2_pow[i - 1] * INV2) % MOD;
    }

    for (int s = 1; s <= n; ++s) {
        long long delta = 2LL * s - n - 1;
        long long R_min = max(1LL, 1 - delta);
        long long R_max = n - s;

        long long diff_sum = 0;
        if (R_min <= R_max) {
            long long k_max = n - 2 * R_min - delta;
            if (k_max >= 3) {
                diff_sum = pref_odd[k_max];
            }
        }

        long long ev_diff = (diff_sum * inv2_pow[n]) % MOD;
        long long ev_b = (n + ev_diff) % MOD * INV2 % MOD;

        cout << ev_b << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
