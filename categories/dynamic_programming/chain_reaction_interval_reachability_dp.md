# Chain Reaction Interval Reachability via Segment Tree and Linear DP

**Domain**: `Dynamic Programming (DP)`  
**Subtopic**: `Classic DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Chain Reaction Interval Reachability via Segment Tree and Linear DP**.

---

## Curated Problems

### `[problem:AtCoder-abc158_f]` — Removing Robots
- **Rating / Difficulty**: 2067
- **Contest**: `abc158`
- **Analysis**: [`analysis/AtCoder-abc158_f.md`](../../analysis/AtCoder-abc158_f.md)
- **Key Idea**: Sort robots by X_i. Activating robot i triggers a contiguous range of robots [i, R_i]. We compute R_i from right to left using a Segment Tree: R_i = max(k, query_max(i+1, k)), where k is the rightmost robot with X_k < X_i + D_i. Once each robot removes [i, R_i], for robot i we have two disjoint choices: (1) robot i is never activated, leaving robot i and moving to i+1 (dp[i+1] ways); or (2) robot i is activated, removing [i, R_i] and moving to R_i+1 (dp[R_i+1] ways). Thus dp[i] = dp[i+1] + dp[R_i+1].
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
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
