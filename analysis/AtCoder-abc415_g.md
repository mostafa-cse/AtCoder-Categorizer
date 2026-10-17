# Problem Analysis: AtCoder-abc415_g — G. Get Many Cola

**Problem ID**: `AtCoder-abc415_g`  
**Contest**: `abc415`  
**Rating / Difficulty**: 2180  
**URL**: https://atcoder.jp/contests/abc415/tasks/abc415_g  
**VJudge Tag**: `[problem:AtCoder-abc415_g]`  
**Category File**: [`../categories/dynamic_programming/unbounded_knapsack_pigeonhole_greedy_replacement.md`](../categories/dynamic_programming/unbounded_knapsack_pigeonhole_greedy_replacement.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Intro to DP`  
- **Topic (Skill)**: `Knapsack and Basic Dynamic Programming`  

---

## 1. Problem Statement & Key Idea
Given N <= 10^{15} initial colas, exchange recipes (A_i, B_i) consume D_i = A_i - B_i empty bottles for B_i new colas with A_i, B_i <= 300. Maximize total colas drunk. The unbounded knapsack structure allows pruning non-maximal items and reducing the DP domain via the Pigeonhole Principle.

## 2. Core Observation & Invariant
Let i' be the item maximizing density B_i / D_i. Any collection of non-i' items with total weight >= K(K + 1) has a subset of items whose weight sum is a multiple of D_{i'}, which can be replaced by i' without decreasing the value. Therefore, knapsack DP only needs to be run up to K(K + 1) approx 96,000, and all remaining capacity is filled greedily using item i'.

## 3. Step-by-Step Algorithm
1. For each A in [1, 300], find the maximum B among given recipes. Form items with weight w = A - B and value v = B.
2. Define sz = MAX_A * (MAX_A + 1) + 10. Run unbounded knapsack DP: dp[i + w] = max(dp[i + w], dp[i] + v) for valid i and items.
3. If N < sz, answer is N + dp[N].
4. Otherwise, find item i' with maximum ratio v / w. For each threshold i from MAX_A to sz - 1, calculate candidate dp[i] + ((N - i) / w) * v. Output N + max_candidate.

## 4. Complexity Analysis
- **Time Complexity**: `O(M + K^3)`
- **Space Complexity**: `O(K^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_A = 310;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    int m;
    if (!(cin >> n >> m)) return 0;

    vector<int> mx_b(MAX_A, 0);
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        mx_b[a] = max(mx_b[a], b);
    }

    vector<pair<int, int>> ls;
    for (int i = 0; i < MAX_A; ++i) {
        if (mx_b[i]) {
            ls.emplace_back(i - mx_b[i], mx_b[i]);
        }
    }

    int sz = MAX_A * (MAX_A + 1) + 10;
    vector<int> dp(sz, 0);
    for (int i = 0; i < sz; ++i) {
        for (auto const& [w, v] : ls) {
            if (i < v || i + w >= sz) continue;
            dp[i + w] = max(dp[i + w], dp[i] + v);
        }
    }

    if (n < sz) {
        cout << n + dp[n] << "\n";
        return 0;
    }

    for (size_t i = 1; i < ls.size(); ++i) {
        if (1LL * ls[0].second * ls[i].first < 1LL * ls[0].first * ls[i].second) {
            swap(ls[0], ls[i]);
        }
    }

    auto [w, v] = ls[0];
    long long ans = 0;
    for (int i = MAX_A; i < sz; ++i) {
        long long now = dp[i] + (n - i) / w * 1LL * v;
        ans = max(ans, now);
    }

    cout << n + ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
