# Problem Analysis: AtCoder-abc145_f — Laminate

**Problem ID**: `AtCoder-abc145_f`  
**Contest**: `abc145`  
**Rating / Difficulty**: 2116  
**URL**: https://atcoder.jp/contests/abc145/tasks/abc145_f  
**VJudge Tag**: `[problem:AtCoder-abc145_f]`  
**Category File**: [`../categories/dynamic_programming/subsequence_retention_dp_laminate.md`](../categories/dynamic_programming/subsequence_retention_dp_laminate.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
You have N columns of heights H_1, ..., H_N. Minimum operations to level all columns to 0 is sum_{i=1}^N max(0, H_i - H_{i-1}). You can change the heights of at most K columns. Find the minimum operations required.

**Key Insight**: Changing at most K columns is equivalent to choosing M = N - K columns to KEEP at their original heights! The optimal choice for intermediate changed columns between two kept columns i and j is to set them to min(H_i, H_j), incurring cost max(0, H_j - H_i). We define dp[i][cnt] as the minimum cost for a prefix ending at kept column i with cnt columns kept. Transitions iterate over all previous kept columns i < j in O(N^2 * (N - K)).

## 2. Core Observation & Invariant
Modifying up to K columns is equivalent to selecting N - K columns to retain, with transitions between kept columns i and j contributing max(0, H_j - H_i).

## 3. Step-by-Step Algorithm
1. Set m = N - K. If m <= 0, output 0.
2. Initialize dp[N+1][m+1] with infinity, dp[0][0] = 0.
3. For i from 0 to N:
4.   For cnt from 0 to m:
5.     For j from i + 1 to N:
6.       dp[j][cnt + 1] = min(dp[j][cnt + 1], dp[i][cnt] + max(0LL, H[j] - H[i])).
7. Output min_{i} dp[i][m].

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2 * (N - K))`
- **Space Complexity**: `O(N * (N - K))`

## 5. Core Skill & Reusable Pattern
- **Core Skill**: Reformulating modification budgets into retention subsequence DP.
- **Reusable Pattern**: Reducing bounded element modifications in prefix-difference costs to selecting optimal retention subsequences.

## 6. Editorial Comparison & Alternative Approaches
Matches official editorial.

## 7. Verified C++17 Implementation
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, k;
    if (!(cin >> n >> k)) return 0;

    vector<long long> h(n + 1, 0);
    for (int i = 1; i <= n; ++i) cin >> h[i];

    int m = n - k;
    if (m <= 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<vector<long long>> dp(n + 1, vector<long long>(m + 1, INF));
    dp[0][0] = 0;

    for (int i = 0; i <= n; ++i) {
        for (int cnt = 0; cnt <= m; ++cnt) {
            if (dp[i][cnt] >= INF) continue;
            for (int j = i + 1; j <= n; ++j) {
                if (cnt + 1 <= m) {
                    long long cost = max(0LL, h[j] - h[i]);
                    dp[j][cnt + 1] = min(dp[j][cnt + 1], dp[i][cnt] + cost);
                }
            }
        }
    }

    long long ans = INF;
    for (int i = 1; i <= n; ++i) {
        ans = min(ans, dp[i][m]);
    }

    cout << ans << "\n";
    return 0;
}
```
