# Problem Analysis: AtCoder-abc353_g — Merchant Takahashi

**Problem ID**: `AtCoder-abc353_g`  
**Contest**: `abc353`  
**Rating / Difficulty**: 1765  
**URL**: https://atcoder.jp/contests/abc353/tasks/abc353_g  
**VJudge Tag**: `[problem:AtCoder-abc353_g]`  
**Category File**: [`../categories/data_structures/segment_tree_manhattan_dp.md`](../categories/data_structures/segment_tree_manhattan_dp.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree DP`  
- **Topic (Skill)**: `Segment Tree Optimization for 1D Manhattan Distance DP`  

---

## 1. Problem Statement & Key Idea
There are N towns on a line. Traveling between towns i and j costs C * |i - j|. M business events occur sequentially: event i in town T_i gives profit P_i. Choose a subset of events to maximize total profit.

**Key Insight**: When transitioning from town j to town T, the net change is dp[j] - C * |T - j| + P. Split into two cases: for j <= T, cost is dp[j] + C * j + P - C * T; for j >= T, cost is dp[j] - C * j + P + C * T. Maintain two segment trees storing (dp[j] + C * j) and (dp[j] - C * j).

## 2. Core Observation & Invariant
Each event requires two range maximum queries: query [1, T] from Tree 1 and query [T, N] from Tree 2, then update town T in both trees in O(log N).

## 3. Step-by-Step Algorithm
1. Build two Segment Trees of size N:
2.   Tree 1 stores dp[j] + C * j.
3.   Tree 2 stores dp[j] - C * j.
4. Initialize with dp[1] = 0, all other dp[j] = -INF.
5. For each event (T, P):
6.   best_left = Tree1.query(1, T) - C * T.
7.   best_right = Tree2.query(T, N) + C * T.
8.   new_dp = max(best_left, best_right) + P.
9.   Tree1.update(T, new_dp + C * T).
10.   Tree2.update(T, new_dp - C * T).
11. Print max over all dp[j].

## 4. Complexity Analysis
- **Time Complexity**: `O(M log N)`
- **Space Complexity**: `O(N)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

struct SegTree {
    int sz;
    vector<long long> tree;
    SegTree(int n) {
        sz = 1;
        while (sz <= n) sz <<= 1;
        tree.assign(2 * sz, -INF);
    }
    void update(int i, long long val) {
        i += sz;
        tree[i] = max(tree[i], val);
        for (i >>= 1; i > 0; i >>= 1) {
            tree[i] = max(tree[2 * i], tree[2 * i + 1]);
        }
    }
    long long query(int l, int r) {
        long long res = -INF;
        for (l += sz, r += sz + 1; l < r; l >>= 1, r >>= 1) {
            if (l & 1) res = max(res, tree[l++]);
            if (r & 1) res = max(res, tree[--r]);
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long c;
    if (!(cin >> n >> c)) return 0;

    int m;
    cin >> m;

    SegTree tree1(n + 1); // dp[j] + c * j
    SegTree tree2(n + 1); // dp[j] - c * j

    tree1.update(1, 0 + c * 1);
    tree2.update(1, 0 - c * 1);

    long long max_ans = 0;

    while (m--) {
        int t;
        long long p;
        cin >> t >> p;

        long long left_max = tree1.query(1, t) - c * t;
        long long right_max = tree2.query(t, n) + c * t;

        long long best_prev = max(left_max, right_max);
        if (best_prev > -INF / 2) {
            long long new_dp = best_prev + p;
            max_ans = max(max_ans, new_dp);
            tree1.update(t, new_dp + c * t);
            tree2.update(t, new_dp - c * t);
        }
    }

    cout << max_ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Segment tree acceleration of 1D absolute difference / Manhattan transitions.
- **Reusable Pattern**: `Manhattan DP Optimization: Split |T - j| into two segment trees storing dp[j] +/- C*j.`
