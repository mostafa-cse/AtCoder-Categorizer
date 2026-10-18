# Problem Analysis: AtCoder-arc074_c — E. RGB Sequence

**Problem ID**: `AtCoder-arc074_c`  
**Contest**: `arc074`  
**Rating / Difficulty**: 2519  
**URL**: https://atcoder.jp/contests/arc074/tasks/arc074_c  
**VJudge Tag**: `[problem:AtCoder-arc074_c]`  
**Category File**: [`../categories/dynamic_programming_dp/rgb_sequence_prefix_color_dp.md`](../categories/dynamic_programming_dp/rgb_sequence_prefix_color_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
We have $N$ positions colored with 3 colors (Red, Green, Blue). There are $M$ constraints: interval $[L_i, R_i]$ must contain exactly $X_i$ distinct colors. Formulate a DP state that tracks the positions of the most recent occurrences of the three colors. When moving from step $i - 1$ to $i$, the new position $i$ takes one color, and the other two colors last appeared at positions $j$ and $k$ with $0 \le k < j < i$ (where 0 indicates the color hasn't appeared yet).

## 2. Core Observation & Invariant
Due to symmetry of color names, the state only needs to track $(i, j, k)$ with $k < j < i$: the current prefix length $i$, the last position $j$ of the second most recent color, and the last position $k$ of the third most recent color. The number of distinct colors in interval $[L, i]$ is simply $1 + [j \ge L] + [k \ge L]$. All constraints ending at $R = i$ can be checked immediately against this formula.

## 3. Step-by-Step Algorithm
1. 1. Precompute constraints ending at each position $i \in [1, N]$.
2. 2. Initialize $DP[0][0] = 1$ for prefix 0.
3. 3. Iterate $i$ from 1 to $N$:
4.    a. From state $(i-1, j, k)$:
5.       - Option 1 (extend current color): new state is $(i, j, k)$, ways $= DP[j][k]$.
6.       - Option 2 (extend second color): new state is $(i, i-1, k)$, ways $= DP[j][k]$.
7.       - Option 3 (extend third color): new state is $(i, i-1, j)$, ways $= DP[j][k]$.
8.    b. Filter valid states $(j, k)$: check if for all constraints $(L, i, X)$, $1 + [j \ge L] + [k \ge L] == X$. Invalidate states failing any constraint.
9. 4. Sum all $DP[j][k]$ at $i = N$ modulo $10^9 + 7$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^3 + M)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>

using namespace std;

static const int MOD = 1000000007;

struct Req {
    int l, x;
};

int dp[305][305];
int nxt_dp[305][305];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Req>> req(n + 1);
    for (int i = 0; i < m; ++i) {
        int l, r, x;
        cin >> l >> r >> x;
        req[r].push_back({l, x});
    }

    dp[0][0] = 3;

    for (const auto& r : req[1]) {
        if (r.x != 1) {
            cout << 0 << "\n";
            return 0;
        }
    }

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j <= i; ++j) {
            for (int k = 0; k <= j; ++k) {
                nxt_dp[j][k] = 0;
            }
        }

        for (int j = 0; j < i; ++j) {
            for (int k = 0; k <= j; ++k) {
                int val = dp[j][k];
                if (!val) continue;

                // 1. Same color as i -> (i+1, j, k)
                nxt_dp[j][k] = (nxt_dp[j][k] + val >= MOD ? nxt_dp[j][k] + val - MOD : nxt_dp[j][k] + val);
                // 2. Color at j -> (i+1, i, k)
                nxt_dp[i][k] = (nxt_dp[i][k] + val >= MOD ? nxt_dp[i][k] + val - MOD : nxt_dp[i][k] + val);
                // 3. Color at k -> (i+1, i, j)
                nxt_dp[i][j] = (nxt_dp[i][j] + val >= MOD ? nxt_dp[i][j] + val - MOD : nxt_dp[i][j] + val);
            }
        }

        for (int j = 0; j <= i; ++j) {
            for (int k = 0; k <= j; ++k) {
                if (nxt_dp[j][k] == 0) continue;
                for (const auto& r : req[i + 1]) {
                    int cnt = 1 + (j >= r.l ? 1 : 0) + (k >= r.l ? 1 : 0);
                    if (cnt != r.x) {
                        nxt_dp[j][k] = 0;
                        break;
                    }
                }
                dp[j][k] = nxt_dp[j][k];
            }
        }
    }

    int ans = 0;
    for (int j = 0; j < n; ++j) {
        for (int k = 0; k <= j; ++k) {
            ans = (ans + dp[j][k] >= MOD ? ans + dp[j][k] - MOD : ans + dp[j][k]);
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
