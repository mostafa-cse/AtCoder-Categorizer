# Problem Analysis: AtCoder-abc145_e — All-you-can-eat

**Problem ID**: `AtCoder-abc145_e`  
**Contest**: `abc145`  
**Rating / Difficulty**: 1528  
**URL**: https://atcoder.jp/contests/abc145/tasks/abc145_e  
**VJudge Tag**: `[problem:AtCoder-abc145_e]`  
**Category File**: [`../categories/dp/order_dependent_knapsack_sorting.md`](../categories/dp/order_dependent_knapsack_sorting.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Order-Dependent 0-1 Knapsack (Sorting by Time Before DP)`  

---

## 1. Problem Statement & Key Idea
N dishes with eating time A_i and deliciousness B_i. You can order as long as the current total time is strictly less than T. Once ordered, you can finish the dish regardless of how much time it takes. Maximize total deliciousness.

**Key Insight**: The final dish ordered can exceed time limit T. By sorting dishes by eating time A_i ascending, the dish that exceeds T can always be assumed to be the LAST dish processed in the DP sequence.

## 2. Core Observation & Invariant
Suppose an optimal subset of dishes is chosen. The last dish ordered must start before T, and it is optimal for this last dish to be the one with the largest eating time A_i. Therefore, sorting by A_i in ascending order ensures that when processing dish i, all previously selected dishes had eating time <= A_i.

## 3. Step-by-Step Algorithm
1. Sort items by A_i in ascending order.
2. Initialize dp[T] = 0 (dp[t] is max value using total time t < T).
3. ans = 0.
4. For each item (A_i, B_i):
5.   For each t from 0 to T - 1:
6.     ans = max(ans, dp[t] + B_i).
7.   For t from T - 1 down to A_i:
8.     dp[t] = max(dp[t], dp[t - A_i] + B_i).
9. Print ans.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * T)`
- **Space Complexity**: `O(T)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, T;
    if (!(cin >> n >> T)) return 0;

    vector<pair<int, int>> dishes(n);
    for (int i = 0; i < n; ++i) {
        cin >> dishes[i].first >> dishes[i].second;
    }

    // Sort by eating time ascending
    sort(dishes.begin(), dishes.end());

    vector<int> dp(T, 0);
    int ans = 0;

    for (int i = 0; i < n; ++i) {
        int a = dishes[i].first;
        int b = dishes[i].second;

        // Try using dish i as the final (overflowing) dish
        for (int t = 0; t < T; ++t) {
            ans = max(ans, dp[t] + b);
        }

        // Standard 0-1 knapsack transition for time < T
        for (int t = T - 1; t >= a; --t) {
            dp[t] = max(dp[t], dp[t - a] + b);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Sorting items by constraint parameter before 0-1 Knapsack to resolve boundary overflow relaxations.
- **Reusable Pattern**: `Relaxed Final Item Knapsack: sort by weight ascending, update global max before standard knapsack transition.`
