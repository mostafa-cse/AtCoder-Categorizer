# Persistent Segment Tree for Online Range Value-Bounded Sum

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Persistent Segment Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Persistent Segment Tree for Online Range Value-Bounded Sum**.

---

## Curated Problems

### `[problem:AtCoder-abc339_g]` — Smaller Sum
- **Rating / Difficulty**: 1792
- **Contest**: `abc339`
- **Analysis**: [`analysis/AtCoder-abc339_g.md`](../../analysis/AtCoder-abc339_g.md)
- **Key Idea**: Coordinate-compress array values. Build a Persistent Segment Tree where version i contains all elements of prefix A[1..i]. A range query [L, R] evaluates query(root[R], <= X) - query(root[L - 1], <= X) in O(log N).
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N log N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    int left_child, right_child;
    long long sum;
};

const int MAX_NODES = 200005 * 40;
Node tree[MAX_NODES];
int node_count = 0;

int insert(int prev, int l, int r, int pos, long long val) {
    int cur = ++node_count;
    tree[cur] = tree[prev];
    tree[cur].sum += val;

    if (l == r) return cur;

    int mid = l + (r - l) / 2;
    if (pos <= mid) {
        tree[cur].left_child = insert(tree[prev].left_child, l, mid, pos, val);
    } else {
        tree[cur].right_child = insert(tree[prev].right_child, mid + 1, r, pos, val);
    }
    return cur;
}

long long query(int node, int l, int r, int ql, int qr) {
    if (!node || l > qr || r < ql) return 0;
    if (ql <= l && r <= qr) return tree[node].sum;

    int mid = l + (r - l) / 2;
    return query(tree[node].left_child, l, mid, ql, qr) +
           query(tree[node].right_child, mid + 1, r, ql, qr);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    vector<long long> vals;
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
        vals.push_back(a[i]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());
    int m = vals.size();

    vector<int> roots(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        int pos = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin() + 1;
        roots[i] = insert(roots[i - 1], 1, m, pos, a[i]);
    }

    int q;
    cin >> q;

    long long last_ans = 0;
    while (q--) {
        long long alpha, beta, gamma;
        cin >> alpha >> beta >> gamma;

        long long l = alpha ^ last_ans;
        long long r = beta ^ last_ans;
        long long x = gamma ^ last_ans;

        if (l > r) swap(l, r);

        auto it = upper_bound(vals.begin(), vals.end(), x);
        int max_pos = it - vals.begin();

        if (max_pos == 0) {
            last_ans = 0;
        } else {
            long long right_sum = query(roots[r], 1, m, 1, max_pos);
            long long left_sum = query(roots[l - 1], 1, m, 1, max_pos);
            last_ans = right_sum - left_sum;
        }

        cout << last_ans << "\n";
    }

    return 0;
}
```
