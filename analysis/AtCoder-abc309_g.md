# Problem Analysis: AtCoder-abc309_g — G. Ban Permutation

**Problem ID**: `AtCoder-abc309_g`  
**Contest**: `abc309`  
**Rating / Difficulty**: 2372  
**URL**: https://atcoder.jp/contests/abc309/tasks/abc309_g  
**VJudge Tag**: `[problem:AtCoder-abc309_g]`  
**Category File**: [`../categories/combinatorics/pie_sliding_window_profile_dp.md`](../categories/combinatorics/pie_sliding_window_profile_dp.md)  

- **Tag (Domain)**: `Combinatorics`  
- **Subtopic**: `Inclusion Exclusion`  
- **Topic (Skill)**: `Principle of Inclusion and Exclusion (PIE)`  

---

## 1. Problem Statement & Key Idea
Count permutations with $|P_i - i| \ge X$ ($X \le 5, N \le 100$). Inclusion-exclusion on banned positions uses profile DP tracking a sliding bitmask of width $2X - 1 \le 9$ of used values, running in $O(N^2 2^{2X-1})$ time.

## 2. Core Observation & Invariant
For each position $i$, $|P_i - i| < X$ confines banned values to a sliding window $[i - X + 1, i + X - 1]$ of width $2X - 1 \le 9$. By Principle of Inclusion-Exclusion, the answer is $\sum_{k=0}^N (-1)^k ways(k) (N-k)!$, where $ways(k)$ is the number of ways to choose $k$ non-conflicting banned placements computed via DP over the $2^{2X-1}$ mask of used window values.

## 3. Step-by-Step Algorithm
1. Process positions $i = 1 \dots N$. State $dp[k][mask]$ tracks $k$ chosen banned positions and a bitmask of used values in window $[i - X + 1, i + X - 1]$.
2. At position $i$, transition by choosing no banned placement, or placing $P_i = j$ for each available bit $j \in [i - X + 1, i + X - 1]$.
3. Shift the window to $i+1$ by discarding bit 0 and shifting right.
4. Apply PIE formula $\sum_{k=0}^N (-1)^k ways(k) (N - k)! \pmod{998244353}$ in $O(N^2 2^{2X-1})$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 2^{2X-1})`
- **Space Complexity**: `O(N 2^{2X-1})`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const int MOD = 998244353;

long long fact[105];

void init() {
    fact[0] = 1;
    for (int i = 1; i <= 100; i++) fact[i] = fact[i - 1] * i % MOD;
}

int dp[2][105][1 << 9];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    init();

    int n, x;
    if (!(cin >> n >> x)) return 0;

    int w = 2 * x - 1;
    int max_mask = 1 << w;

    int cur = 0, nxt = 1;
    dp[cur][0][0] = 1;

    for (int i = 1; i <= n; i++) {
        for (int k = 0; k <= i; k++) {
            for (int m = 0; m < max_mask; m++) {
                dp[nxt][k][m] = 0;
            }
        }

        for (int k = 0; k < i; k++) {
            for (int m = 0; m < max_mask; m++) {
                int val = dp[cur][k][m];
                if (!val) continue;

                // Option 1: don't choose any banned value for position i
                dp[nxt][k][m] = (dp[nxt][k][m] + val) % MOD;

                // Option 2: choose a banned value j for position i
                // j in [i - x + 1, i + x - 1]
                // relative offset in window: j - (i - x + 1)
                for (int d = -(x - 1); d <= x - 1; d++) {
                    int j = i + d;
                    if (j < 1 || j > n) continue;
                    int bit = d + (x - 1);
                    if (!(m & (1 << bit))) {
                        dp[nxt][k + 1][m | (1 << bit)] = (dp[nxt][k + 1][m | (1 << bit)] + val) % MOD;
                    }
                }
            }
        }

        // Shift window for next position i+1:
        // Value i - x + 1 leaves the window (bit 0 is discarded)
        // Values shift right by 1
        for (int k = 0; k <= i; k++) {
            for (int m = 0; m < max_mask; m++) {
                dp[cur][k][m] = 0;
            }
        }
        for (int k = 0; k <= i; k++) {
            for (int m = 0; m < max_mask; m++) {
                if (dp[nxt][k][m]) {
                    int shifted_m = m >> 1;
                    dp[cur][k][shifted_m] = (dp[cur][k][shifted_m] + dp[nxt][k][m]) % MOD;
                }
            }
        }
    }

    vector<long long> ways(n + 1, 0);
    for (int k = 0; k <= n; k++) {
        for (int m = 0; m < max_mask; m++) {
            ways[k] = (ways[k] + dp[cur][k][m]) % MOD;
        }
    }

    long long ans = 0;
    for (int k = 0; k <= n; k++) {
        long long term = ways[k] * fact[n - k] % MOD;
        if (k % 2 == 1) {
            ans = (ans - term + MOD) % MOD;
        } else {
            ans = (ans + term) % MOD;
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
