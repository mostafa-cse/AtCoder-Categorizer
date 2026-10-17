# Problem Analysis: AtCoder-abc206_f — Interval Game 2

**Problem ID**: `AtCoder-abc206_f`  
**Contest**: `abc206`  
**Rating / Difficulty**: 2221  
**URL**: https://atcoder.jp/contests/abc206/tasks/abc206_f  
**VJudge Tag**: `[problem:AtCoder-abc206_f]`  
**Category File**: [`../categories/game_theory/interval_game_2_sprague_grundy_range_dp.md`](../categories/game_theory/interval_game_2_sprague_grundy_range_dp.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Grundy Number / Nim`  
- **Topic (Skill)**: `Grundy Number and Basic Game Theory`  

---

## 1. Problem Statement & Key Idea
Two players alternately pick non-overlapping intervals from N given intervals [L_i, R_i) on line [1, 100]. The last player to move wins. Determine who wins under optimal play.

## 2. Core Observation & Invariant
Impartial game under normal play governed by the Sprague-Grundy theorem. Picking an interval [L_i, R_i) inside available subsegment [l, r) partitions the state into two independent subgames [l, L_i) and [R_i, r). The Grundy value of the transition is g(l, L_i) ^ g(R_i, r). State transitions can be precomputed using range DP over segment lengths in O(V^2 N) where V = 100.

## 3. Step-by-Step Algorithm
1. 1. Initialize 2D DP array dp[l][r] = 0 for 1 <= l < r <= 101.
2. 2. Loop over interval length len from 1 to 100, and left endpoint l from 1 to 101 - len (with r = l + len).
3. 3. Collect all Grundy values g(l, L_i) ^ g(R_i, r) for intervals [L_i, R_i) entirely contained in [l, r).
4. 4. Compute mex of collected values to set dp[l][r].
5. 5. If dp[1][101] != 0, Alice wins; otherwise Bob wins.

## 4. Complexity Analysis
- **Time Complexity**: `O(V^3 + V^2 N) per testcase, V = 100`
- **Space Complexity**: `O(V^2)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n;
    cin >> n;
    vector<pair<int, int>> intervals(n);
    for (int i = 0; i < n; i++) {
        cin >> intervals[i].first >> intervals[i].second;
    }

    // Coordinates are in [1, 100]
    // dp[l][r] is the Grundy value of the interval [l, r)
    // 1 <= l < r <= 101
    static int dp[105][105];
    for (int l = 1; l <= 101; l++) {
        for (int r = 1; r <= 101; r++) {
            dp[l][r] = 0;
        }
    }

    for (int len = 1; len <= 100; len++) {
        for (int l = 1; l + len <= 101; l++) {
            int r = l + len;
            vector<bool> seen(105, false);
            for (int i = 0; i < n; i++) {
                int L = intervals[i].first;
                int R = intervals[i].second;
                if (l <= L && R <= r) {
                    int g = dp[l][L] ^ dp[R][r];
                    if (g < 105) seen[g] = true;
                }
            }
            int mex = 0;
            while (seen[mex]) mex++;
            dp[l][r] = mex;
        }
    }

    if (dp[1][101] != 0) {
        cout << "Alice\n";
    } else {
        cout << "Bob\n";
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (cin >> t) {
        while (t--) {
            solve();
        }
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
