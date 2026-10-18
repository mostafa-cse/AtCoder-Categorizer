# Problem Analysis: AtCoder-abc256_h — Ex. I like Query Problem

**Problem ID**: `AtCoder-abc256_h`  
**Contest**: `abc256`  
**Rating / Difficulty**: 2531  
**URL**: https://atcoder.jp/contests/abc256/tasks/abc256_h  
**VJudge Tag**: `[problem:AtCoder-abc256_h]`  
**Category File**: [`../categories/data_structures_ds/i_like_query_problem_segment_tree_beats.md`](../categories/data_structures_ds/i_like_query_problem_segment_tree_beats.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree Beats`  

---

## 1. Problem Statement & Key Idea
Maintain an array $A$ of size $N$ supporting three operations:
1. Range floor division: $A_i \leftarrow \lfloor A_i / x \rfloor$ for $i \in [L, R]$.
2. Range assignment: $A_i \leftarrow y$ for $i \in [L, R]$.
3. Range sum query: $\sum_{i=L}^R A_i$.

## 2. Core Observation & Invariant
Floor division is not a linear operation, but when $\lfloor \max / x \rfloor == \lfloor \min / x \rfloor$, the entire range $[L, R]$ collapses to a single value, transforming the operation into a simple range assignment! Segment Tree Beats tracks range minimum, range maximum, and range sum. When $\lfloor \max / x \rfloor == \lfloor \min / x \rfloor$, we apply range assignment tag $\lfloor \max / x \rfloor$. Otherwise, we recurse into children. Since each division by $x \ge 2$ strictly reduces the bit-length of $\max - \min$, the amortized complexity is $O((N + Q) \log N \log(\max A))$.

## 3. Step-by-Step Algorithm
1. 1. Build a Segment Tree where each node maintains `mn`, `mx`, `sum`, and lazy assignment tag `lazy_set`.
2. 2. For range assignment $A_i \leftarrow y$: standard lazy tag update.
3. 3. For range division by $x$:
4.    a. If $x == 1$, return.
5.    b. If $node.mx == 0$, return.
6.    c. If $node.mx / x == node.mn / x$, apply lazy assignment tag $node.mx / x$.
7.    d. Otherwise, push down lazy tags, recurse into left and right children, and pull up values.
8. 4. For range sum: push down lazy tags and accumulate child sums.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + Q) \log N \log(\max A))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 500005;

struct Node {
    long long sum;
    long long mx, mn;
    long long lazy_set;
} tree[MAXN * 4];

void apply_set(int node, int l, int r, long long val) {
    tree[node].sum = (long long)(r - l + 1) * val;
    tree[node].mx = val;
    tree[node].mn = val;
    tree[node].lazy_set = val;
}

void push_down(int node, int l, int r) {
    if (tree[node].lazy_set != -1) {
        int mid = (l + r) / 2;
        apply_set(node * 2, l, mid, tree[node].lazy_set);
        apply_set(node * 2 + 1, mid + 1, r, tree[node].lazy_set);
        tree[node].lazy_set = -1;
    }
}

void push_up(int node) {
    tree[node].sum = tree[node * 2].sum + tree[node * 2 + 1].sum;
    tree[node].mx = max(tree[node * 2].mx, tree[node * 2 + 1].mx);
    tree[node].mn = min(tree[node * 2].mn, tree[node * 2 + 1].mn);
}

void build(int node, int l, int r, const vector<long long>& a) {
    tree[node].lazy_set = -1;
    if (l == r) {
        tree[node].sum = a[l];
        tree[node].mx = a[l];
        tree[node].mn = a[l];
        return;
    }
    int mid = (l + r) / 2;
    build(node * 2, l, mid, a);
    build(node * 2 + 1, mid + 1, r, a);
    push_up(node);
}

void update_set(int node, int l, int r, int ql, int qr, long long val) {
    if (ql <= l && r <= qr) {
        apply_set(node, l, r, val);
        return;
    }
    push_down(node, l, r);
    int mid = (l + r) / 2;
    if (ql <= mid) update_set(node * 2, l, mid, ql, qr, val);
    if (qr > mid) update_set(node * 2 + 1, mid + 1, r, ql, qr, val);
    push_up(node);
}

void update_div(int node, int l, int r, int ql, int qr, long long x) {
    if (ql <= l && r <= qr) {
        if (tree[node].mx / x == tree[node].mn / x) {
            apply_set(node, l, r, tree[node].mx / x);
            return;
        }
    }
    push_down(node, l, r);
    int mid = (l + r) / 2;
    if (ql <= mid) update_div(node * 2, l, mid, ql, qr, x);
    if (qr > mid) update_div(node * 2 + 1, mid + 1, r, ql, qr, x);
    push_up(node);
}

long long query_sum(int node, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) {
        return tree[node].sum;
    }
    push_down(node, l, r);
    int mid = (l + r) / 2;
    long long res = 0;
    if (ql <= mid) res += query_sum(node * 2, l, mid, ql, qr);
    if (qr > mid) res += query_sum(node * 2 + 1, mid + 1, r, ql, qr);
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    build(1, 1, n, a);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            long long x;
            cin >> l >> r >> x;
            update_div(1, 1, n, l, r, x);
        } else if (type == 2) {
            int l, r;
            long long y;
            cin >> l >> r >> y;
            update_set(1, 1, n, l, r, y);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query_sum(1, 1, n, l, r) << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
