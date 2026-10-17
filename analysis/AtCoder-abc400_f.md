# Problem Analysis: AtCoder-abc400_f — F. Happy Birthday! 3

**Problem ID**: `AtCoder-abc400_f`  
**Contest**: `abc400`  
**Rating / Difficulty**: 2263  
**URL**: https://atcoder.jp/contests/abc400/tasks/abc400_f  
**VJudge Tag**: `[problem:AtCoder-abc400_f]`  
**Category File**: [`../categories/dynamic_programming_dp/interval_dp_circular_cake_coloring.md`](../categories/dynamic_programming_dp/interval_dp_circular_cake_coloring.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Interval DP / Range DP / Matrix Chain Multiplication (MCM)`  

---

## 1. Problem Statement & Key Idea
A circular cake has $N$ equal slices ($N \le 400$). Slices initially have color 0 and must end with color $C_i \in [1, N]$. An operation paints $b$ contiguous slices starting at $a$ with color $c$ for cost $b + X_c$. Find the minimum total cost to reach the target configuration.

## 2. Core Observation & Invariant
Reverse the process: start with the target colors $C_i$ and repaint contiguous intervals to color 0. A final operation on interval $[l, r)$ costs $(r - l) + X_c$, where endpoints $l$ and $r-1$ must originally have color $c$. Operations form a non-crossing laminar family, reducing the problem to Interval DP. Unroll the circular cake into an array of length $2N$. Let $dp[l][r]$ be the minimum cost to clear $[l, r)$ to color 0, and $ep[l][r]$ be the minimum cost to make all elements in $[l, r)$ either color 0 or color $C_l$. For $m \in (l, r)$, transitions split via $dp[l][m] + dp[m][r]$ and $ep[l][m] + dp[m][r]$. When $C_l == C_{r-1}$, we transition $ep[l][r] = \min(ep[l][r], ep[l][r-1])$ and $dp[l][r] = \min(dp[l][r], ep[l][r] + (r - l) + X_{C_l})$. The answer is $\min_{0 \le i < N} dp[i][i + N]$.

## 3. Step-by-Step Algorithm
1. Duplicate the color array to size $2N$.
2. Initialize $dp[i][i] = 0$ and $ep[i][i] = 0$ for all $i \le 2N$.
3. Iterate interval length $len = 1 \dots N$ and starting left endpoint $l = 0 \dots 2N - len$ ($r = l + len$).
4. Split over midpoint $m \in (l, r)$: update $dp[l][r] = \min(dp[l][r], dp[l][m] + dp[m][r])$ and $ep[l][r] = \min(ep[l][r], ep[l][m] + dp[m][r])$.
5. If $C_l == C_{r-1}$, update $ep[l][r] = \min(ep[l][r], ep[l][r-1])$ and $dp[l][r] = \min(dp[l][r], ep[l][r] + (r - l) + X_{C_l})$.
6. Compute answer as $\min_{0 \le i < N} dp[i][i + N]$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

inline void chmin(long long &a, long long b) {
    if (b < a) a = b;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> c(2 * n);
    for (int i = 0; i < n; ++i) {
        cin >> c[i];
        --c[i];
        c[n + i] = c[i];
    }

    vector<long long> x(n);
    for (int i = 0; i < n; ++i) {
        cin >> x[i];
    }

    // dp[l][r] = min cost to clear [l, r) to 0
    // ep[l][r] = min cost to make all in [l, r) either 0 or c[l]
    vector<vector<long long>> dp(2 * n + 1, vector<long long>(2 * n + 1, INF));
    vector<vector<long long>> ep(2 * n + 1, vector<long long>(2 * n + 1, INF));

    for (int i = 0; i <= 2 * n; ++i) {
        dp[i][i] = 0;
        ep[i][i] = 0;
    }

    for (int len = 1; len <= n; ++len) {
        for (int l = 0; l + len <= 2 * n; ++l) {
            int r = l + len;
            for (int m = l + 1; m < r; ++m) {
                chmin(dp[l][r], dp[l][m] + dp[m][r]);
                chmin(ep[l][r], ep[l][m] + dp[m][r]);
            }
            if (c[l] == c[r - 1]) {
                chmin(ep[l][r], ep[l][r - 1]);
                chmin(dp[l][r], ep[l][r] + (r - l) + x[c[l]]);
            }
        }
    }

    long long ans = INF;
    for (int i = 0; i < n; ++i) {
        chmin(ans, dp[i][i + n]);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
