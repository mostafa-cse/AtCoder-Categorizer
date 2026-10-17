# Problem Analysis: AtCoder-abc032_d — ナップサック問題

**Problem ID**: `AtCoder-abc032_d`  
**Contest**: `abc032`  
**Rating / Difficulty**: 1731  
**URL**: https://atcoder.jp/contests/abc032/tasks/abc032_d  
**VJudge Tag**: `[problem:AtCoder-abc032_d]`  
**Category File**: [`../categories/dp/constraint_adaptive_knapsack_master.md`](../categories/dp/constraint_adaptive_knapsack_master.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `Knapsack Multi-Constraint`  
- **Topic (Skill)**: `Constraint-Adaptive Knapsack (Meet-in-the-Middle vs Weight DP vs Dual Value DP)`  

---

## 1. Problem Statement & Key Idea
Given N items with values v_i and weights w_i, and knapsack capacity W. Find max value under one of three constraint conditions: (1) N <= 30, (2) max w_i <= 1000, or (3) max v_i <= 1000.

**Key Insight**: The ultimate knapsack master problem. Adapt algorithm based on constraints: (1) N <= 30 -> Meet-in-the-Middle O(2^{N/2}), (2) max w_i <= 1000 -> Weight DP O(N * sum w_i), (3) max v_i <= 1000 -> Dual Value DP O(N * sum v_i).

## 2. Core Observation & Invariant
Meet-in-the-middle splits items into two halves of size <= 15, sorts by weight with prefix max value, and binary searches.

## 3. Step-by-Step Algorithm
1. Check which constraint holds:
2. Case 1 (N <= 30): Generate subsets of first half and second half. Filter second half for Pareto optimality. For each in first half, binary search upper bound in second half.
3. Case 2 (max w_i <= 1000): Standard 1D DP array of size min(W, N * 1000).
4. Case 3 (max v_i <= 1000): Dual DP array where dp[v] = min weight to achieve value v. Ans = max v such that dp[v] <= W.

## 4. Complexity Analysis
- **Time Complexity**: `Case 1: O(2^{N/2} log 2^{N/2}), Case 2: O(N * sum W), Case 3: O(N * sum V)`
- **Space Complexity**: `Case 1: O(2^{N/2}), Case 2: O(sum W), Case 3: O(sum V)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Item {
    long long v, w;
};

void solve_small_n(int n, long long W, const vector<Item>& items) {
    int n1 = n / 2;
    int n2 = n - n1;

    vector<pair<long long, long long>> part1;
    for (int mask = 0; mask < (1 << n1); ++mask) {
        long long cur_w = 0, cur_v = 0;
        for (int i = 0; i < n1; ++i) {
            if ((mask >> i) & 1) {
                cur_w += items[i].w;
                cur_v += items[i].v;
            }
        }
        if (cur_w <= W) part1.push_back({cur_w, cur_v});
    }

    vector<pair<long long, long long>> part2;
    for (int mask = 0; mask < (1 << n2); ++mask) {
        long long cur_w = 0, cur_v = 0;
        for (int i = 0; i < n2; ++i) {
            if ((mask >> i) & 1) {
                cur_w += items[n1 + i].w;
                cur_v += items[n1 + i].v;
            }
        }
        if (cur_w <= W) part2.push_back({cur_w, cur_v});
    }

    sort(part2.begin(), part2.end());
    vector<pair<long long, long long>> p2_opt;
    long long max_v = -1;
    for (auto& p : part2) {
        if (p.second > max_v) {
            max_v = p.second;
            p2_opt.push_back(p);
        }
    }

    long long ans = 0;
    for (auto& p : part1) {
        long long rem_w = W - p.first;
        auto it = upper_bound(p2_opt.begin(), p2_opt.end(), make_pair(rem_w, (long long)4e18));
        if (it != p2_opt.begin()) {
            --it;
            ans = max(ans, p.second + it->second);
        }
    }
    cout << ans << "\n";
}

void solve_small_w(int n, long long W, const vector<Item>& items) {
    int max_w = min((long long)n * 1000, W);
    vector<long long> dp(max_w + 1, 0);

    for (int i = 0; i < n; ++i) {
        for (int w = max_w; w >= items[i].w; --w) {
            dp[w] = max(dp[w], dp[w - items[i].w] + items[i].v);
        }
    }

    long long ans = 0;
    for (int w = 0; w <= max_w; ++w) ans = max(ans, dp[w]);
    cout << ans << "\n";
}

void solve_small_v(int n, long long W, const vector<Item>& items) {
    int max_v = n * 1000;
    vector<long long> dp(max_v + 1, INF);
    dp[0] = 0;

    for (int i = 0; i < n; ++i) {
        for (int v = max_v; v >= items[i].v; --v) {
            if (dp[v - items[i].v] != INF) {
                dp[v] = min(dp[v], dp[v - items[i].v] + items[i].w);
            }
        }
    }

    long long ans = 0;
    for (int v = 0; v <= max_v; ++v) {
        if (dp[v] <= W) ans = v;
    }
    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long W;
    if (!(cin >> n >> W)) return 0;

    vector<Item> items(n);
    long long max_item_w = 0, max_item_v = 0;
    for (int i = 0; i < n; ++i) {
        cin >> items[i].v >> items[i].w;
        max_item_w = max(max_item_w, items[i].w);
        max_item_v = max(max_item_v, items[i].v);
    }

    if (n <= 30) {
        solve_small_n(n, W, items);
    } else if (max_item_w <= 1000) {
        solve_small_w(n, W, items);
    } else {
        solve_small_v(n, W, items);
    }

    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Selecting optimal knapsack algorithmic paradigm based on constraints.
- **Reusable Pattern**: `Constraint-Adaptive Knapsack: Branch between Meet-in-the-Middle, Weight-DP, and Value-Dual-DP.`
