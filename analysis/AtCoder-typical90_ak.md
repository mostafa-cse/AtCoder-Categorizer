# Problem Analysis: AtCoder-typical90_ak — Don't Leave the Spice

**Problem ID**: `AtCoder-typical90_ak`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 037)  
**Rating / Difficulty**: 1750 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ak  
**VJudge Tag**: `[problem:AtCoder-typical90_ak]`  
**Category File**: [`../categories/dp/segment_tree_dp.md`](../categories/dp/segment_tree_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Segment Tree Accelerated Range Knapsack DP`  

---

## 1. Problem Statement & Key Idea
Dishes require exact weight W (W <= 10000). N spices with weight range [L_i, R_i] and value V_i. Find maximum value to achieve exact weight W, or -1 if impossible.

**Core Idea**: Bounded range Knapsack DP: dp[i][w] = max(dp[i-1][w], max_{l in [L_i, R_i]} (dp[i-1][w - l] + V_i)).

## 2. Core Observation & Invariant
The transition requires the maximum of dp[i-1][w - R_i .. w - L_i]. Maintaining the previous DP layer in a Segment Tree answers each range query in O(log W).

## 3. Step-by-Step Algorithm
1. Build Segment Tree over capacities [0, W] initialized to -1 (with seg[0] = 0).
2. For each spice (L, R, V):
   - For w from W down to 0: query range_max in [max(0, w - R), w - L]. If valid, next_dp[w] = max(dp[w], best + V).
   - Update Segment Tree with next_dp.
3. Output dp[W].

## 4. Complexity Analysis
Time: O(N * W log W), Space: O(W).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = -1;

struct SegTree {
    int n;
    vector<long long> tree;
    SegTree(int n) : n(n), tree(4 * (n + 1), -1) {}

    void update(int node, int start, int end, int idx, long long val) {
        if (start == end) {
            tree[node] = max(tree[node], val);
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    long long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return -1;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return max(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w, n;
    if (!(cin >> w >> n)) return 0;

    SegTree seg(w);
    seg.update(1, 0, w, 0, 0);

    for (int i = 0; i < n; ++i) {
        int l, r;
        long long v;
        cin >> l >> r >> v;

        vector<pair<int, long long>> updates;
        for (int cap = 1; cap <= w; ++cap) {
            int ql = max(0, cap - r);
            int qr = cap - l;
            if (ql <= qr) {
                long long best = seg.query(1, 0, w, ql, qr);
                if (best != -1) {
                    updates.push_back({cap, best + v});
                }
            }
        }
        for (auto [cap, val] : updates) {
            seg.update(1, 0, w, cap, val);
        }
    }

    long long ans = seg.query(1, 0, w, w, w);
    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Segment Tree range-maximum query acceleration on range knapsack transitions.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Accelerating sliding-window / range-interval DP transitions using dynamic range maximum data structures.
- **Reusable Pattern**: `Segment Tree Accelerated Range DP.`

---
Back to [Segment Tree Accelerated Range Knapsack DP](../categories/dp/segment_tree_dp.md) | [Categories Directory](../categories/README.md)