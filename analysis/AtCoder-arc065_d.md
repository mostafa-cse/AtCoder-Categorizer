# Problem Analysis: AtCoder-arc065_d — Shuffling

**Problem ID**: `AtCoder-arc065_d`  
**Contest**: `arc065`  
**Rating / Difficulty**: 2652  
**URL**: https://atcoder.jp/contests/arc065/tasks/arc065_d  
**VJudge Tag**: `[problem:AtCoder-arc065_d]`  
**Category File**: [`../categories/basics/shuffling_substrings_sliding_window.md`](../categories/basics/shuffling_substrings_sliding_window.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `More Techniques`  
- **Topic (Skill)**: `Sliding Window Technique`  

---

## 1. Problem Statement & Key Idea
Count distinct binary strings achievable after applying interval shuffle operations by tracking the cumulative count of 1s in the prefix under sliding-window reachability constraints.

## 2. Core Observation & Invariant
Each interval shuffle operation allows arbitrary rearrangement of characters within [l_i, r_i]. By computing the cumulative max-reach interval R[i] covering prefix i, the count of 1s in prefix i, denoted c_i, is strictly bounded: max(c_{i-1}, ones(R[i]) - (R[i] - i)) <= c_i <= min(c_{i-1} + 1, ones(R[i])). Dynamic programming over prefix index i and current 1-count c_i with sliding window state optimization counts all valid binary sequences.

## 3. Step-by-Step Algorithm
1. 1. For each position i, precalculate the furthest reachable index R[i] across all intervals covering i.
2. 2. Compute prefix sums of 1s in the original string.
3. 3. Define DP state dp[i][c] = number of valid prefix assignments up to index i with exactly c ones.
4. 4. Transition dp[i][c] from dp[i-1][c] (choosing 0) and dp[i-1][c-1] (choosing 1), maintaining validity within [min_ones[i], max_ones[i]].
5. 5. Sum dp[N][ones(N)] modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    string S;
    cin >> S;

    vector<int> pref(N + 1, 0);
    for (int i = 1; i <= N; ++i) {
        pref[i] = pref[i - 1] + (S[i - 1] == '1' ? 1 : 0);
    }

    vector<int> R(N + 1);
    for (int i = 0; i <= N; ++i) R[i] = i;

    for (int i = 0; i < M; ++i) {
        int l, r;
        cin >> l >> r;
        R[l] = max(R[l], r);
    }

    for (int i = 1; i <= N; ++i) {
        R[i] = max(R[i], R[i - 1]);
    }

    // dp[j]: number of ways such that prefix of length i has j ones
    vector<int> dp(N + 1, 0);
    dp[0] = 1;

    for (int i = 1; i <= N; ++i) {
        vector<int> next_dp(N + 1, 0);
        int low = max(0, pref[R[i]] - (R[i] - i));
        int high = min(i, pref[R[i]]);

        for (int j = low; j <= high; ++j) {
            long long ways = dp[j]; // T[i] = 0
            if (j > 0) {
                ways += dp[j - 1]; // T[i] = 1
            }
            if (ways >= MOD) ways %= MOD;
            next_dp[j] = ways;
        }
        dp = move(next_dp);
    }

    cout << dp[pref[N]] << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
