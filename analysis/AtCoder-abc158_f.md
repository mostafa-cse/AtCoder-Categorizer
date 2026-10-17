# Problem Analysis: AtCoder-abc158_f — Removing Robots

**Problem ID**: `AtCoder-abc158_f`  
**Contest**: `abc158`  
**Rating / Difficulty**: 2067  
**URL**: https://atcoder.jp/contests/abc158/tasks/abc158_f  
**VJudge Tag**: `[problem:AtCoder-abc158_f]`  
**Category File**: [`../categories/dynamic_programming/chain_reaction_interval_reachability_dp.md`](../categories/dynamic_programming/chain_reaction_interval_reachability_dp.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `Classic DP`  
- **Topic (Skill)**: `Chain Reaction Interval Reachability via Segment Tree and Linear DP`  

---

## 1. Problem Statement & Key Idea
N robots on a number line at coordinates X_i move D_i to the right when activated, triggering any robot in [X_i, X_i + D_i) recursively. How many distinct sets of remaining robots can result from activating robots some number of times modulo 998244353?

**Key Idea**: Sort robots by X_i. Activating robot i triggers a contiguous range of robots [i, R_i]. We compute R_i from right to left using a Segment Tree: R_i = max(k, query_max(i+1, k)), where k is the rightmost robot with X_k < X_i + D_i. Once each robot removes [i, R_i], for robot i we have two disjoint choices: (1) robot i is never activated, leaving robot i and moving to i+1 (dp[i+1] ways); or (2) robot i is activated, removing [i, R_i] and moving to R_i+1 (dp[R_i+1] ways). Thus dp[i] = dp[i+1] + dp[R_i+1].

## 2. Core Observation & Invariant
Recursive activation forms contiguous intervals [i, R_i], turning set counting into a clean 2-choice linear DP: keep robot i (dp[i+1]) vs activate robot i (dp[R_i+1]).

## 3. Step-by-Step Algorithm
1. Sort robots by X_i.
2. Initialize a Segment Tree supporting point update and range maximum query.
3. For i from N-1 down to 0:
4.   Find k = upper_bound(X) - 1 for X_i + D_i.
5.   If k > i: R_i = max(k, query(i+1, k)); else R_i = i.
6.   Update segment tree at position i with R_i.
7. Initialize dp array of size N+2 with dp[N] = 1, dp[N+1] = 1.
8. For i from N-1 down to 0: dp[i] = (dp[i+1] + dp[R_i+1]) % 998244353.
9. Output dp[0].

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Combining range maximum segment tree for domino reachability with linear DP.

**Reusable Pattern**: Cascading range trigger DP: compute range closure [i, R_i] with segment tree, then transition dp[i] = dp[i+1] + dp[R_i+1].

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MOD = 998244353;

struct Robot {
    long long x, d;
    int id;
};

struct SegTree {
    int n;
    vector<int> tree;
    SegTree(int n) : n(n), tree(4 * n, 0) {}

    void update(int node, int l, int r, int qx, int val) {
        if (l == r) {
            tree[node] = val;
            return;
        }
        int mid = l + (r - l) / 2;
        if (qx <= mid) update(2 * node, l, mid, qx, val);
        else update(2 * node + 1, mid + 1, r, qx, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int l, int r, int ql, int qr) {
        if (ql > qr || ql > r || qr < l) return 0;
        if (ql <= l && r <= qr) return tree[node];
        int mid = l + (r - l) / 2;
        return max(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<Robot> robots(n);
    for (int i = 0; i < n; ++i) {
        cin >> robots[i].x >> robots[i].d;
        robots[i].id = i;
    }

    sort(robots.begin(), robots.end(), [](const Robot& a, const Robot& b) {
        return a.x < b.x;
    });

    vector<long long> X(n);
    for (int i = 0; i < n; ++i) X[i] = robots[i].x;

    SegTree st(n);
    vector<int> R(n);

    for (int i = n - 1; i >= 0; --i) {
        long long reach_x = robots[i].x + robots[i].d;
        int k = lower_bound(X.begin(), X.end(), reach_x) - X.begin() - 1;
        if (k > i) {
            R[i] = max(k, st.query(1, 0, n - 1, i + 1, k));
        } else {
            R[i] = i;
        }
        st.update(1, 0, n - 1, i, R[i]);
    }

    vector<long long> dp(n + 2, 0);
    dp[n] = 1;
    dp[n + 1] = 1;

    for (int i = n - 1; i >= 0; --i) {
        dp[i] = (dp[i + 1] + dp[R[i] + 1]) % MOD;
    }

    cout << dp[0] << "\n";
    return 0;
}
```
