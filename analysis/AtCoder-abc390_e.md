# Problem Analysis: AtCoder-abc390_e — Vitamin Balance

**Problem ID**: `AtCoder-abc390_e`  
**Contest**: `abc390`  
**Rating / Difficulty**: 1227  
**URL**: https://atcoder.jp/contests/abc390/tasks/abc390_e  
**VJudge Tag**: `[problem:AtCoder-abc390_e]`  
**Category File**: [`../categories/dp/three_resource_knapsack_search.md`](../categories/dp/three_resource_knapsack_search.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Knapsack DP`  
- **Topic (Skill)**: `3-Resource Dual Knapsack DP with Monotonic Search`  

---

## 1. Problem Statement & Key Idea
N foods. Food i provides vitamin V_i in {1, 2, 3} with amount A_i and calories C_i. Total calories <= X. Maximize min(total vitamin 1, total vitamin 2, total vitamin 3).

**Key Idea**: Separate foods into 3 independent groups by vitamin type V in {1, 2, 3}.

## 2. Core Observation & Invariant
For each vitamin group, compute 0-1 Knapsack: dp[v][cal] = max vitamin v obtained using exactly cal calories. Then binary search on target vitamin minimum T: for each vitamin group, find the minimum calories needed to achieve >= T vitamins. If sum of min calories across all 3 groups <= X, target T is feasible.

## 3. Step-by-Step Algorithm
1. Compute 0-1 Knapsack table for each of the 3 vitamin groups up to X calories.
2. Make dp arrays prefix-max monotonic.
3. Binary search on T in [0, 10^9]: for each group v, find smallest cal such that dp[v][cal] >= T; if sum cal <= X, target T is achievable.
4. Print optimal T.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * X + log(MAX) * 3 * log X)`
- **Space Complexity**: `O(3 * X)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Food {
    int v;
    long long a, c;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, x;
    if (!(cin >> n >> x)) return 0;

    vector<vector<pair<long long, int>>> groups(4);
    for (int i = 0; i < n; ++i) {
        int v, c;
        long long a;
        cin >> v >> a >> c;
        groups[v].push_back({a, c});
    }

    vector<vector<long long>> dp(4, vector<long long>(x + 1, 0));

    for (int v = 1; v <= 3; ++v) {
        for (const auto& [amt, cal] : groups[v]) {
            for (int c = x; c >= cal; --c) {
                dp[v][c] = max(dp[v][c], dp[v][c - cal] + amt);
            }
        }
        for (int c = 1; c <= x; ++c) {
            dp[v][c] = max(dp[v][c], dp[v][c - 1]);
        }
    }

    long long low = 0, high = 1e9, ans = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        int total_cal = 0;
        bool ok = true;

        for (int v = 1; v <= 3; ++v) {
            auto it = lower_bound(dp[v].begin(), dp[v].end(), mid);
            if (it == dp[v].end()) {
                ok = false;
                break;
            }
            total_cal += (it - dp[v].begin());
        }

        if (ok && total_cal <= x) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Independent Knapsack decomposition with multi-objective bottleneck binary search.
- **Reusable Pattern**: `Maximize min of 3 resources: 3 separate Knapsacks + binary search feasibility check.`
