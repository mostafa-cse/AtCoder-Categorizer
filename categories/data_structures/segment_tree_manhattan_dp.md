# Segment Tree Optimization for 1D Manhattan Distance DP

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Segment Tree DP`  

This workbook contains curated, high-quality competitive programming problems teaching **Segment Tree Optimization for 1D Manhattan Distance DP**.

---

## Curated Problems

### `[problem:AtCoder-abc353_g]` — Merchant Takahashi
- **Rating / Difficulty**: 1765
- **Contest**: `abc353`
- **Analysis**: [`analysis/AtCoder-abc353_g.md`](../../analysis/AtCoder-abc353_g.md)
- **Key Idea**: When transitioning from town j to town T, the net change is dp[j] - C * |T - j| + P. Split into two cases: for j <= T, cost is dp[j] + C * j + P - C * T; for j >= T, cost is dp[j] - C * j + P + C * T. Maintain two segment trees storing (dp[j] + C * j) and (dp[j] - C * j).
- **Time Complexity**: `O(M log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
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
