# Problem Analysis: AtCoder-dp_e — Knapsack 2

**Problem ID**: `AtCoder-dp_e`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 1450  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_e  
**VJudge Tag**: `[problem:AtCoder-dp_e]`  
**Category File**: [`../categories/dp/knapsack.md`](../categories/dp/knapsack.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack Dual State / Value as State`  

---

## 1. Problem Statement & Key Idea
Solve 0/1 Knapsack when capacity W <= 10^9 is enormous, but v_i <= 1000 and N <= 100.

**Core Idea**: When capacity W is up to 10^9, weight cannot be an array index. Invert the state: define dp[v] as the minimum weight required to achieve exact value v.

## 2. Core Observation & Invariant
Total value sum <= 100 * 1000 = 10^5. The value dimension is pseudopolynomial while weight is not.

## 3. Step-by-Step Algorithm
1. V_sum = sum(v_i). dp[0] = 0, dp[1..V_sum] = INF.
2. For each item (w_i, v_i): for v from V_sum down to v_i: dp[v] = min(dp[v], dp[v - v_i] + w_i).
3. Return max v such that dp[v] <= W.

## 4. Complexity Analysis
Time: O(N * sum(V)), Space: O(sum(V)).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    vector<int> w(n);
    vector<int> v(n);
    int max_val = 0;
    for (int i = 0; i < n; ++i) {
        cin >> w[i] >> v[i];
        max_val += v[i];
    }

    vector<long long> dp(max_val + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int val = max_val; val >= v[i]; --val) {
            if (dp[val - v[i]] != INF) {
                dp[val] = min(dp[val], dp[val - v[i]] + w[i]);
            }
        }
    }

    int ans = 0;
    for (int val = max_val; val >= 0; --val) {
        if (dp[val] <= W) {
            ans = val;
            break;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Dual problem formulation and state parameter swapping.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Swapping objective function and state dimension when constraints are large but values are compact.
- **Reusable Pattern**: `Dual DP parameter inversion.`

---
Back to [Knapsack Dual State / Value as State](../categories/dp/knapsack.md) | [Categories Directory](../categories/README.md)