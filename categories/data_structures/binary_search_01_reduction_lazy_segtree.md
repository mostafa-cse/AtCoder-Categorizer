# Segment Tree with Lazy Propagation

**Domain**: `Data Structures (DS)`  
**Subtopic**: `Segment Tree`  

This workbook contains curated, high-quality competitive programming problems teaching **Segment Tree with Lazy Propagation**.

---

## Curated Problems

### `[problem:AtCoder-abc237_g]` — Range Sort Query
- **Rating / Difficulty**: 2085
- **Contest**: `abc237`
- **Analysis**: [`analysis/AtCoder-abc237_g.md`](../../analysis/AtCoder-abc237_g.md)
- **Key Idea**: Sorting arbitrary permutations online is difficult, but sorting a 0-1 sequence is trivial using a lazy segment tree (count the number of 1s in [L, R], then overwrite a prefix with 0s and suffix with 1s). Since we only care about the position of a single element X, we can encode elements as: 0 if P_i < X, 1 if P_i == X, and 2 if P_i > X (or binary search the index, or maintain 3-state counts in the lazy segment tree). Maintaining three values {0, 1, 2} in a lazy segment tree allows directly performing range sorts and locating the single position containing 1 at the end.
- **Time Complexity**: `O((N + Q) log N)`
- **Space Complexity**: `O(N)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int c0, c1, c2;
    int lazy; // -1: none, 0, 1, 2
};

int n, q, x_val;
vector<int> p;
vector<Node> tree;

void apply_lazy(int u, int l, int r, int val) {
    tree[u].c0 = tree[u].c1 = tree[u].c2 = 0;
    int len = r - l + 1;
    if (val == 0) tree[u].c0 = len;
    else if (val == 1) tree[u].c1 = len;
    else if (val == 2) tree[u].c2 = len;
    tree[u].lazy = val;
}

void push(int u, int l, int r) {
    if (tree[u].lazy != -1 && l < r) {
        int mid = (l + r) / 2;
        apply_lazy(2 * u, l, mid, tree[u].lazy);
        apply_lazy(2 * u + 1, mid + 1, r, tree[u].lazy);
        tree[u].lazy = -1;
    }
}

void pull(int u) {
    tree[u].c0 = tree[2 * u].c0 + tree[2 * u + 1].c0;
    tree[u].c1 = tree[2 * u].c1 + tree[2 * u + 1].c1;
    tree[u].c2 = tree[2 * u].c2 + tree[2 * u + 1].c2;
}

void build(int u, int l, int r) {
    tree[u].lazy = -1;
    if (l == r) {
        int val = (p[l] < x_val ? 0 : (p[l] == x_val ? 1 : 2));
        tree[u].c0 = (val == 0);
        tree[u].c1 = (val == 1);
        tree[u].c2 = (val == 2);
        return;
    }
    int mid = (l + r) / 2;
    build(2 * u, l, mid);
    build(2 * u + 1, mid + 1, r);
    pull(u);
}

void update_range(int u, int l, int r, int ql, int qr, int val) {
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

Node query_range(int u, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) return tree[u];
    push(u, l, r);
    int mid = (l + r) / 2;
    Node res = {0, 0, 0, -1};
    if (ql <= mid) {
        Node left_res = query_range(2 * u, l, mid, ql, qr);
        res.c0 += left_res.c0;
        res.c1 += left_res.c1;
        res.c2 += left_res.c2;
    }
    if (qr > mid) {
        Node right_res = query_range(2 * u + 1, mid + 1, r, ql, qr);
        res.c0 += right_res.c0;
        res.c1 += right_res.c1;
        res.c2 += right_res.c2;
    }
    return res;
}

int find_target(int u, int l, int r) {
    if (l == r) return l;
    push(u, l, r);
    int mid = (l + r) / 2;
    if (tree[2 * u].c1 > 0) return find_target(2 * u, l, mid);
    return find_target(2 * u + 1, mid + 1, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> n >> q >> x_val)) return 0;

    p.resize(n + 1);
    for (int i = 1; i <= n; ++i) cin >> p[i];

    tree.resize(4 * n + 5);
    build(1, 1, n);

    for (int i = 0; i < q; ++i) {
        int type, l, r;
        cin >> type >> l >> r;
        Node cnt = query_range(1, 1, n, l, r);
        if (type == 1) { // Ascending
            update_range(1, 1, n, l, l + cnt.c0 - 1, 0);
            update_range(1, 1, n, l + cnt.c0, l + cnt.c0 + cnt.c1 - 1, 1);
            update_range(1, 1, n, l + cnt.c0 + cnt.c1, r, 2);
        } else { // Descending
            update_range(1, 1, n, l, l + cnt.c2 - 1, 2);
            update_range(1, 1, n, l + cnt.c2, l + cnt.c2 + cnt.c1 - 1, 1);
            update_range(1, 1, n, l + cnt.c2 + cnt.c1, r, 0);
        }
    }

    cout << find_target(1, 1, n) << "\n";
    return 0;
}
```
