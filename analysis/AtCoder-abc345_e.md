# Problem Analysis: AtCoder-abc345_e — E. Colorful Subsequence

**Problem ID**: `AtCoder-abc345_e`  
**Contest**: `abc345`  
**Rating / Difficulty**: 2356  
**URL**: https://atcoder.jp/contests/abc345/tasks/abc345_e  
**VJudge Tag**: `[problem:AtCoder-abc345_e]`  
**Category File**: [`../categories/dynamic_programming/top2_color_linear_dp.md`](../categories/dynamic_programming/top2_color_linear_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Delete exactly $K$ balls such that adjacent remaining balls have distinct colors, maximizing total value. For each deletion count $j \le K$, maintaining only the top 2 maximum values with distinct colors allows $O(1)$ transitions per ball in $O(NK)$ time.

## 2. Core Observation & Invariant
When deleting exactly $K$ balls such that adjacent remaining balls have distinct colors, the optimal value for each deletion count $j \in [0, K]$ depends only on the color of the last kept ball. Because a new ball of color $C_i$ can transition from any previous state with color $\ne C_i$, it suffices to maintain only the top 2 maximum values with distinct colors for each deletion count $j$.

## 3. Step-by-Step Algorithm
1. Maintain DP array $dp[j]$ of size $K + 1$, where each entry stores the top 2 `(value, color)` pairs with distinct colors for having deleted $j$ balls so far.
2. For each ball $i$ with color $C_i$ and value $V_i$, transition: delete ball ($j \to j+1$, copying top 2 states) or keep ball ($j \to j$, extending the best previous state whose color differs from $C_i$).
3. Merge candidates into new top 2 states in $O(1)$ per $j$, running in $O(NK)$ time and $O(K)$ space.

## 4. Complexity Analysis
- **Time Complexity**: `O(NK)`
- **Space Complexity**: `O(K)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

const long long INF = 1e18;

struct Element {
    long long val;
    int col;
};

struct Top2 {
    Element first, second;
    Top2() {
        first = {-INF, -1};
        second = {-INF, -2};
    }
    void update(long long v, int c) {
        if (c == first.col) {
            if (v > first.val) first.val = v;
        } else if (c == second.col) {
            if (v > second.val) second.val = v;
            if (second.val > first.val) swap(first, second);
        } else {
            if (v > first.val) {
                second = first;
                first = {v, c};
            } else if (v > second.val) {
                second = {v, c};
            }
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;
    vector<int> c(n);
    vector<long long> v(n);
    for (int i = 0; i < n; i++) cin >> c[i] >> v[i];

    vector<Top2> dp(k + 1);
    dp[0].update(0, 0);

    for (int i = 0; i < n; i++) {
        vector<Top2> next_dp(k + 1);
        int cur_col = c[i];
        long long cur_val = v[i];

        for (int j = 0; j <= k; j++) {
            // Delete ball i
            if (j + 1 <= k) {
                if (dp[j].first.val >= 0) next_dp[j + 1].update(dp[j].first.val, dp[j].first.col);
                if (dp[j].second.val >= 0) next_dp[j + 1].update(dp[j].second.val, dp[j].second.col);
            }
            // Keep ball i
            if (dp[j].first.val >= 0) {
                if (dp[j].first.col != cur_col) {
                    next_dp[j].update(dp[j].first.val + cur_val, cur_col);
                } else if (dp[j].second.val >= 0 && dp[j].second.col != cur_col) {
                    next_dp[j].update(dp[j].second.val + cur_val, cur_col);
                }
            }
        }
        dp = move(next_dp);
    }

    long long ans = dp[k].first.val;
    if (ans < 0) cout << -1 << "\n";
    else cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
