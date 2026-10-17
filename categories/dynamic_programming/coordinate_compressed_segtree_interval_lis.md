# Coordinate-Compressed Segment Tree Optimized Interval LIS

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `DP Optimizations`  

This workbook contains curated, high-quality competitive programming problems teaching **Coordinate-Compressed Segment Tree Optimized Interval LIS**.

---

## Curated Problems

### `[problem:AtCoder-arc159_d]` — LIS 2
- **Rating / Difficulty**: 2056
- **Contest**: `arc159`
- **Analysis**: [`analysis/AtCoder-arc159_d.md`](../../analysis/AtCoder-arc159_d.md)
- **Key Idea**: Each interval [l_i, r_i] contains strictly increasing consecutive integers. When extending an existing LIS ending at value x: if x < l_i, we can append all elements [l_i, r_i], obtaining length dp[x] + (r_i - l_i + 1). If l_i <= x <= r_i, we can append (x+1 .. r_i), obtaining length dp[x] + (r_i - x) = (dp[x] - x) + r_i. Maintaining both dp[x] and (dp[x] - x) in a coordinate-compressed segment tree allows querying both transitions in O(log N) and updating at position r_i.
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
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
