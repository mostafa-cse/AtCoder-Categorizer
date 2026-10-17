# Segment Tree with Lazy Propagation

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Segment Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Segment Tree with Lazy Propagation**.

---

## Curated Problems

### `[problem:AtCoder-abc371_f]` — Takahashi in Narrow Road
- **Rating / Difficulty**: 2109
- **Contest**: `abc371`
- **Analysis**: [`analysis/AtCoder-abc371_f.md`](../../analysis/AtCoder-abc371_f.md)
- **Key Idea**: The spacing constraint X_{j+1} - X_j >= 1 becomes non-decreasing coordinates Y_j = X_j - j, where Y_1 <= Y_2 <= ... <= Y_N. Moving person T to target G means setting Y_T to G - T. If target > Y_T, we push all adjacent people to the right with Y_j < target up to target. If target < Y_T, we push all adjacent people to the left with Y_j > target down to target. Since Y is non-decreasing, the set of pushed people forms a contiguous interval! Using a Lazy Segment Tree supporting range assignment and range sum queries, we binary search the boundary of the pushed range and execute the range assignment in O(log N).
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    long long sum;
    long long min_val, max_val;
    long long lazy;
};

int n;
vector<long long> y;
vector<Node> tree;

const long long INF = 2e18;

void apply_lazy(int u, int l, int r, long long val) {
    tree[u].lazy = val;
    tree[u].min_val = val;
    tree[u].max_val = val;
    tree[u].sum = 1LL * (r - l + 1) * val;
}

void push(int u, int l, int r) {
    if (tree[u].lazy != -INF) {
        int mid = (l + r) / 2;
        apply_lazy(2 * u, l, mid, tree[u].lazy);
        apply_lazy(2 * u + 1, mid + 1, r, tree[u].lazy);
        tree[u].lazy = -INF;
    }
}

void pull(int u) {
    tree[u].sum = tree[2 * u].sum + tree[2 * u + 1].sum;
    tree[u].min_val = min(tree[2 * u].min_val, tree[2 * u + 1].min_val);
    tree[u].max_val = max(tree[2 * u].max_val, tree[2 * u + 1].max_val);
}

void build(int u, int l, int r) {
    tree[u].lazy = -INF;
    if (l == r) {
        tree[u].sum = y[l];
        tree[u].min_val = y[l];
        tree[u].max_val = y[l];
        return;
    }
    int mid = (l + r) / 2;
    build(2 * u, l, mid);
    build(2 * u + 1, mid + 1, r);
    pull(u);
}

long long query_point(int u, int l, int r, int p) {
    if (l == r) return tree[u].sum;
    push(u, l, r);
    int mid = (l + r) / 2;
    if (p <= mid) return query_point(2 * u, l, mid, p);
    return query_point(2 * u + 1, mid + 1, r, p);
}

long long query_sum(int u, int l, int r, int ql, int qr) {
    if (ql > qr) return 0;
    if (ql <= l && r <= qr) return tree[u].sum;
    push(u, l, r);
    int mid = (l + r) / 2;
    long long res = 0;
    if (ql <= mid) res += query_sum(2 * u, l, mid, ql, qr);
    if (qr > mid) res += query_sum(2 * u + 1, mid + 1, r, ql, qr);
    return res;
}

void update_range(int u, int l, int r, int ql, int qr, long long val) {
    if (ql > qr) return;
    if (ql <= l && r <= qr) {
        apply_lazy(u, l, r, val);
        return;
    }
    push(u, l, r);
    int mid = (l + r) / 2;
    if (ql <= mid) update_range(2 * u, l, mid, ql, qr, val);
    if (qr > mid) update_range(2 * u + 1, mid + 1, r, ql, qr, val);
    pull(u);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    y.resize(n + 1);
    for (int i = 1; i <= n; ++i) {
        long long x;
        cin >> x;
        y[i] = x - i;
    }

    tree.resize(4 * n + 5);
    build(1, 1, n);

    int q;
    if (!(cin >> q)) return 0;

    long long total_dist = 0;

    while (q--) {
        int t;
        long long g;
        cin >> t >> g;
        long long target = g - t;
        long long cur = query_point(1, 1, n, t);

        if (target > cur) {
            int low = t, high = n, R = t;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (query_point(1, 1, n, mid) < target) {
                    R = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            long long prev_sum = query_sum(1, 1, n, t, R);
            long long new_sum = 1LL * (R - t + 1) * target;
            total_dist += (new_sum - prev_sum);
            update_range(1, 1, n, t, R, target);
        } else if (target < cur) {
            int low = 1, high = t, L = t;
            while (low <= high) {
                int mid = (low + high) / 2;
                if (query_point(1, 1, n, mid) > target) {
                    L = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            long long prev_sum = query_sum(1, 1, n, L, t);
            long long new_sum = 1LL * (t - L + 1) * target;
            total_dist += (prev_sum - new_sum);
            update_range(1, 1, n, L, t, target);
        }
    }

    cout << total_dist << "\n";
    return 0;
}
```
