# Problem Analysis: AtCoder-arc159_d — LIS 2

**Problem ID**: `AtCoder-arc159_d`  
**Contest**: `arc159`  
**Rating / Difficulty**: 2056  
**URL**: https://atcoder.jp/contests/arc159/tasks/arc159_d  
**VJudge Tag**: `[problem:AtCoder-arc159_d]`  
**Category File**: [`../categories/dynamic_programming/coordinate_compressed_segtree_interval_lis.md`](../categories/dynamic_programming/coordinate_compressed_segtree_interval_lis.md)  

- **Tag (Domain)**: `Dynamic Programming (DP)`  
- **Subtopic**: `DP Optimizations`  
- **Topic (Skill)**: `Coordinate-Compressed Segment Tree Optimized Interval LIS`  

---

## 1. Problem Statement & Key Idea
Takahashi appends intervals [l_i, r_i] sequentially to an array X. Find the length of the longest strictly increasing subsequence (LIS) of the concatenated sequence X.

**Key Idea**: Each interval [l_i, r_i] contains strictly increasing consecutive integers. When extending an existing LIS ending at value x: if x < l_i, we can append all elements [l_i, r_i], obtaining length dp[x] + (r_i - l_i + 1). If l_i <= x <= r_i, we can append (x+1 .. r_i), obtaining length dp[x] + (r_i - x) = (dp[x] - x) + r_i. Maintaining both dp[x] and (dp[x] - x) in a coordinate-compressed segment tree allows querying both transitions in O(log N) and updating at position r_i.

## 2. Core Observation & Invariant
Extending from x in [l_i, r_i] splits into querying max(dp[x]) for x < l_i and max(dp[x] - x) for l_i <= x <= r_i.

## 3. Step-by-Step Algorithm
1. Collect all l_i and r_i endpoints and coordinate-compress them into an array of size M <= 2N.
2. Initialize a Segment Tree supporting range max queries for two values: dp[x] and dp[x] - x.
3. For each interval [l_i, r_i]:
4.   Query 1: q1 = max_{x < l_i} dp[x]. Gain = q1 + (r_i - l_i + 1).
5.   Query 2: q2 = max_{l_i <= x <= r_i} (dp[x] - x). Gain = q2 + r_i.
6.   Best LIS ending at r_i is cur = max({r_i - l_i + 1, Gain 1, Gain 2}).
7.   Update segment tree at position r_i with dp = cur and diff = cur - r_i.
8. Output the maximum LIS length found.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. Core Algorithmic Skill & Learning Takeaway
Segment tree optimization for piecewise linear interval DP transitions.

**Reusable Pattern**: Interval subsequence transitions split into range query for dp[x] and range query for dp[x] - x.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const long long INF = 2e18;

struct SegTree {
    int n;
    vector<long long> tree_dp;
    vector<long long> tree_diff;

    SegTree(int n) : n(n), tree_dp(4 * n, -INF), tree_diff(4 * n, -INF) {}

    void update(int node, int l, int r, int qx, long long v_dp, long long v_diff) {
        if (l == r) {
            tree_dp[node] = max(tree_dp[node], v_dp);
            tree_diff[node] = max(tree_diff[node], v_diff);
            return;
        }
        int mid = l + (r - l) / 2;
        if (qx <= mid) update(2 * node, l, mid, qx, v_dp, v_diff);
        else update(2 * node + 1, mid + 1, r, qx, v_dp, v_diff);
        tree_dp[node] = max(tree_dp[2 * node], tree_dp[2 * node + 1]);
        tree_diff[node] = max(tree_diff[2 * node], tree_diff[2 * node + 1]);
    }

    long long query_dp(int node, int l, int r, int ql, int qr) {
        if (ql > qr || ql > r || qr < l) return -INF;
        if (ql <= l && r <= qr) return tree_dp[node];
        int mid = l + (r - l) / 2;
        return max(query_dp(2 * node, l, mid, ql, qr), query_dp(2 * node + 1, mid + 1, r, ql, qr));
    }

    long long query_diff(int node, int l, int r, int ql, int qr) {
        if (ql > qr || ql > r || qr < l) return -INF;
        if (ql <= l && r <= qr) return tree_diff[node];
        int mid = l + (r - l) / 2;
        return max(query_diff(2 * node, l, mid, ql, qr), query_diff(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<pair<long long, long long>> intervals(n);
    vector<long long> pts;
    for (int i = 0; i < n; ++i) {
        cin >> intervals[i].first >> intervals[i].second;
        pts.push_back(intervals[i].first);
        pts.push_back(intervals[i].second);
    }

    sort(pts.begin(), pts.end());
    pts.erase(unique(pts.begin(), pts.end()), pts.end());
    int m = pts.size();

    auto get_idx = [&](long long v) {
        return lower_bound(pts.begin(), pts.end(), v) - pts.begin();
    };

    SegTree st(m);
    long long ans = 0;

    for (int i = 0; i < n; ++i) {
        long long l = intervals[i].first;
        long long r = intervals[i].second;
        int il = get_idx(l);
        int ir = get_idx(r);

        long long q1 = st.query_dp(1, 0, m - 1, 0, il - 1);
        long long cur1 = (q1 < 0 ? 0 : q1) + (r - l + 1);

        long long q2 = st.query_diff(1, 0, m - 1, il, ir);
        long long cur2 = (q2 < -INF / 2 ? -INF : q2 + r);

        long long cur = max({cur1, cur2, r - l + 1});
        ans = max(ans, cur);

        st.update(1, 0, m - 1, ir, cur, cur - r);
    }

    cout << ans << "\n";
    return 0;
}
```
