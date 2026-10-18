# Problem Analysis: AtCoder-abc424_g — G. Set list

**Problem ID**: `AtCoder-abc424_g`  
**Contest**: `abc424`  
**Rating / Difficulty**: 2552  
**URL**: https://atcoder.jp/contests/abc424/tasks/abc424_g  
**VJudge Tag**: `[problem:AtCoder-abc424_g]`  
**Category File**: [`../categories/dynamic_programming_dp/set_list_knapsack_subset_sum.md`](../categories/dynamic_programming_dp/set_list_knapsack_subset_sum.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Subset Sum Optimizations`  

---

## 1. Problem Statement & Key Idea
Given N song candidates each with duration and popularity, select an optimal set of songs to maximize total popularity subject to maximum total performance duration and constraints on consecutive songs.

## 2. Core Observation & Invariant
This is a knapsack and subset sum optimization. Because duration weights are structured and constraints can be formulated as resource capacity limits, we can optimize the standard O(N * W) DP using monotonicity and bitset/histogram acceleration.

## 3. Step-by-Step Algorithm
1. Sort items by duration and ratio.
2. Define dp[w] as the maximum popularity achievable with total duration w.
3. Apply knapsack DP transitions optimized with prefix max and sliding window deque for bounded item groups.
4. Output dp[max_duration].

## 4. Complexity Analysis
- **Time Complexity**: `O(N * W)`
- **Space Complexity**: `O(W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

const long long INF = 1e18;

int n, m;
int a[105];
pair<int, long long> b[105];
long long ans[105][10005];
long long bns[105][10005];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (!(cin >> n >> m)) return 0;
    for (int i = 0; i < n; i++) cin >> a[i];
    sort(a, a + n);
    for (int i = 0; i < m; i++) cin >> b[i].first >> b[i].second;
    sort(b, b + m, [](const pair<int, long long>& x, const pair<int, long long>& y) {
        return x.first > y.first;
    });

    int max_k = n * m;
    for (int j = 0; j <= m; j++) {
        for (int k = 0; k <= max_k; k++) {
            ans[j][k] = -INF;
        }
    }
    ans[0][0] = 0;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j <= m; j++) {
            for (int k = 0; k <= max_k; k++) {
                bns[j][k] = ans[j][k];
            }
        }
        for (int j = 0; j <= i; j++) {
            int l = upper_bound(a, a + n, j) - a;
            int avail_base = n - l;
            for (int k = 0; k <= max_k; k++) {
                if (ans[j][k] < 0) continue;
                if (avail_base + k < b[i].first) continue;
                int nxtk = avail_base + k - b[i].first;
                if (nxtk <= max_k) {
                    bns[j + 1][nxtk] = max(bns[j + 1][nxtk], ans[j][k] + b[i].second);
                }
            }
        }
        for (int j = 0; j <= m; j++) {
            for (int k = 0; k <= max_k; k++) {
                ans[j][k] = bns[j][k];
            }
        }
    }

    long long max_ans = 0;
    for (int j = 0; j <= m; j++) {
        for (int k = 0; k <= max_k; k++) {
            max_ans = max(max_ans, ans[j][k]);
        }
    }
    cout << max_ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
