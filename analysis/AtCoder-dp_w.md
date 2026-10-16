# Problem Analysis: AtCoder-dp_w — Intervals

**Problem ID**: `AtCoder-dp_w`  
**Contest**: `dp` (Educational DP Contest)  
**Rating / Difficulty**: 2350  
**URL**: https://atcoder.jp/contests/dp/tasks/dp_w  
**VJudge Tag**: `[problem:AtCoder-dp_w]`  
**Category File**: [`../categories/dp/lazy_segment_tree_dp.md`](../categories/dp/lazy_segment_tree_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Lazy Segment Tree Range-Add Point-Query DP`  

---

## 1. Problem Statement & Key Idea
Construct a binary string s of length N. You are given M intervals [l_i, r_i] with score a_i. An interval gives score a_i if at least one '1' falls in [l_i, r_i]. Maximize total score.

**Core Idea**: DP where state is the position of the last '1'. Maintain dp[j] in a Lazy Segment Tree. When scanning i from 1 to N, for each interval ending at i, add its score a to range [l, i].

## 2. Core Observation & Invariant
If the previous '1' is at position j in [l, i], the interval is satisfied. Adding a to range [l, i] updates all valid previous positions in O(log N). dp[i] = max_{0 <= j < i} dp[j].

## 3. Step-by-Step Algorithm
1. Group intervals by their right endpoint r.
2. Maintain Lazy Segment Tree of size N+1.
3. For i from 1 to N: for each interval [l, i] with score a: segtree.range_add(l, i, a). dp[i] = segtree.query_max(0, i-1). segtree.update_point(i, dp[i]).
4. Return segtree.query_max(0, N).

## 4. Complexity Analysis
Time: O((N + M) log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct LazySegTree {
    int n;
    vector<long long> tree, lazy;
    LazySegTree(int n) : n(n), tree(4 * n, 0), lazy(4 * n, 0) {}

    void push(int node) {
        if (lazy[node] != 0) {
            tree[2 * node] += lazy[node];
            lazy[2 * node] += lazy[node];
            tree[2 * node + 1] += lazy[node];
            lazy[2 * node + 1] += lazy[node];
            lazy[node] = 0;
        }
    }

    void update_range(int node, int l, int r, int ql, int qr, long long val) {
        if (ql <= l && r <= qr) {
            tree[node] += val;
            lazy[node] += val;
            return;
        }
        push(node);
        int mid = (l + r) / 2;
        if (ql <= mid) update_range(2 * node, l, mid, ql, qr, val);
        if (qr > mid) update_range(2 * node + 1, mid + 1, r, ql, qr, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    long long query_max(int node, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return tree[node];
        push(node);
        int mid = (l + r) / 2;
        long long res = -INF;
        if (ql <= mid) res = max(res, query_max(2 * node, l, mid, ql, qr));
        if (qr > mid) res = max(res, query_max(2 * node + 1, mid + 1, r, ql, qr));
        return res;
    }

    void update_point(int node, int l, int r, int idx, long long val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        push(node);
        int mid = (l + r) / 2;
        if (idx <= mid) update_point(2 * node, l, mid, idx, val);
        else update_point(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    struct Interval { int l; long long a; };
    vector<vector<Interval>> intervals_at(n + 1);
    for (int i = 0; i < m; ++i) {
        int l, r;
        long long a;
        cin >> l >> r >> a;
        intervals_at[r].push_back({l, a});
    }

    LazySegTree seg(n + 1);

    for (int i = 1; i <= n; ++i) {
        // Carry forward previous optimal state
        long long best_prev = seg.query_max(1, 0, n, 0, i - 1);
        seg.update_point(1, 0, n, i, best_prev);

        // Add intervals ending at i
        for (const auto& inv : intervals_at[i]) {
            seg.update_range(1, 0, n, inv.l, i, inv.a);
        }
    }

    cout << max(0LL, seg.query_max(1, 0, n, 0, n)) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Range-add point-query Lazy Segment Tree dynamic programming.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Using Lazy Segment Tree to dynamically update previous state transitions across ranges of active intervals.
- **Reusable Pattern**: `Lazy Segment Tree accelerated range-event DP.`

---
Back to [Lazy Segment Tree Range-Add Point-Query DP](../categories/dp/lazy_segment_tree_dp.md) | [Categories Directory](../categories/README.md)