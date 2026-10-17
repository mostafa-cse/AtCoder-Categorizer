# Segment Tree (Point Update Range Query)

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Segment Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Segment Tree (Point Update Range Query)**.

---

## Curated Problems

### `[problem:AtCoder-abc342_g]` — Retroactive Range Chmax
- **Rating / Difficulty**: 2107
- **Contest**: `abc342`
- **Analysis**: [`analysis/AtCoder-abc342_g.md`](../../analysis/AtCoder-abc342_g.md)
- **Key Idea**: Instead of pushing updates down to leaves (which makes deletion difficult), we maintain a multiset of active chmax values at each canonical node of a Segment Tree covering [l, r]. Query 1 inserts x into the multisets of the O(log N) canonical nodes covering [l, r]. Query 2 erases x from those exact canonical nodes. Query 3 for position p simply traverses the segment tree from leaf p up to the root, taking the maximum value among all multisets encountered.
- **Time Complexity**: `O(Q log^2 N)`
- **Space Complexity**: `O((N + Q) log N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

struct Query {
    int type;
    int l, r, x;
};

int n, q;
vector<multiset<int>> tree;

void update_insert(int u, int l, int r, int ql, int qr, int x) {
    if (ql <= l && r <= qr) {
        tree[u].insert(x);
        return;
    }
    int mid = (l + r) / 2;
    if (ql <= mid) update_insert(2 * u, l, mid, ql, qr, x);
    if (qr > mid) update_insert(2 * u + 1, mid + 1, r, ql, qr, x);
}

void update_erase(int u, int l, int r, int ql, int qr, int x) {
    if (ql <= l && r <= qr) {
        auto it = tree[u].find(x);
        if (it != tree[u].end()) tree[u].erase(it);
        return;
    }
    int mid = (l + r) / 2;
    if (ql <= mid) update_erase(2 * u, l, mid, ql, qr, x);
    if (qr > mid) update_erase(2 * u + 1, mid + 1, r, ql, qr, x);
}

int query_point(int u, int l, int r, int p) {
    int max_val = 0;
    if (!tree[u].empty()) {
        max_val = *tree[u].rbegin();
    }
    if (l == r) return max_val;
    int mid = (l + r) / 2;
    if (p <= mid) {
        max_val = max(max_val, query_point(2 * u, l, mid, p));
    } else {
        max_val = max(max_val, query_point(2 * u + 1, mid + 1, r, p));
    }
    return max_val;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    cin >> q;
    vector<Query> queries(q + 1);
    tree.resize(4 * n + 5);

    for (int i = 1; i <= n; ++i) {
        update_insert(1, 1, n, i, i, a[i]);
    }

    for (int k = 1; k <= q; ++k) {
        cin >> queries[k].type;
        if (queries[k].type == 1) {
            cin >> queries[k].l >> queries[k].r >> queries[k].x;
            update_insert(1, 1, n, queries[k].l, queries[k].r, queries[k].x);
        } else if (queries[k].type == 2) {
            int id;
            cin >> id;
            update_erase(1, 1, n, queries[id].l, queries[id].r, queries[id].x);
        } else {
            int p;
            cin >> p;
            cout << query_point(1, 1, n, p) << "\n";
        }
    }

    return 0;
}
```
