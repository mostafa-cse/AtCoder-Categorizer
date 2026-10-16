# Problem Analysis: AtCoder-abc118_d — Match Matching

**Problem ID**: `AtCoder-abc118_d`  
**Contest**: `abc118`  
**Rating / Difficulty**: 1657  
**URL**: https://atcoder.jp/contests/abc118/tasks/abc118_d  
**VJudge Tag**: `[problem:AtCoder-abc118_d]`  
**Category File**: [`../categories/dp/lexicographical_unbounded_knapsack.md`](../categories/dp/lexicographical_unbounded_knapsack.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Unbounded Knapsack for Lexicographically Largest Number`  

---

## 1. Problem Statement & Key Idea
Given N matchsticks and a set of M allowed digits. Find the largest integer that can be formed using EXACTLY N matchsticks, where each digit d requires a specific number of matchsticks.

**Key Insight**: The larger integer is first determined by having MORE DIGITS. If two integers have the same number of digits, compare lexicographically. Use unbounded knapsack DP: dp[n] = maximum number of digits formable with n matchsticks.

## 2. Core Observation & Invariant
Once max digits are known, greedily reconstruct the number from left to right: for each position, test allowed digits from 9 down to 1. If using digit d leaves n - cost[d] matchsticks with dp[n - cost[d]] == dp[n] - 1, pick d!

## 3. Step-by-Step Algorithm
1. Cost table for digits 1..9: {2, 5, 5, 4, 5, 6, 3, 7, 6}.
2. Initialize dp[N + 1] with -INF. dp[0] = 0.
3. For n from 1 to N:
4.   For each allowed digit d:
5.     if n >= cost[d]: dp[n] = max(dp[n], dp[n - cost[d]] + 1).
6. Sort allowed digits descending.
7. Reconstruct string: curr = N.
8. While curr > 0:
9.   For digit d in allowed_digits:
10.     if curr >= cost[d] and dp[curr - cost[d]] == dp[curr] - 1:
11.       append d to result, curr -= cost[d], break.
12. Print result string.

## 4. Complexity Analysis
- **Time Complexity**: `O(N * M)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const int match_costs[10] = {0, 2, 5, 5, 4, 5, 6, 3, 7, 6};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> a(m);
    for (int i = 0; i < m; ++i) {
        cin >> a[i];
    }
    sort(a.rbegin(), a.rend());

    vector<int> dp(n + 1, -1e9);
    dp[0] = 0;

    for (int i = 1; i <= n; ++i) {
        for (int d : a) {
            int c = match_costs[d];
            if (i >= c && dp[i - c] >= 0) {
                dp[i] = max(dp[i], dp[i - c] + 1);
            }
        }
    }

    string ans = "";
    int curr = n;

    while (curr > 0) {
        for (int d : a) {
            int c = match_costs[d];
            if (curr >= c && dp[curr - c] == dp[curr] - 1) {
                ans += to_string(d);
                curr -= c;
                break;
            }
        }
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Two-phase optimization: maximize sequence length via DP, then greedily reconstruct lexicographical maximum.
- **Reusable Pattern**: `Lexicographical Unbounded Knapsack: dp[weight] = max_length, greedy backtrack from 9 down to 1.`
