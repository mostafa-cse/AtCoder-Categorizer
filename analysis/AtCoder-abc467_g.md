# Problem Analysis: AtCoder-abc467_g — G. Many Sweets Problem

**Problem ID**: `AtCoder-abc467_g`  
**Contest**: `abc467`  
**Rating / Difficulty**: 2544  
**URL**: https://atcoder.jp/contests/abc467/tasks/abc467_g  
**VJudge Tag**: `[problem:AtCoder-abc467_g]`  
**Category File**: [`../categories/data_structures_ds/many_sweets_fenwick_dynamic_segtree.md`](../categories/data_structures_ds/many_sweets_fenwick_dynamic_segtree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `2D Dynamic Segment Tree`  

---

## 1. Problem Statement & Key Idea
Given N boxes of sweets with weights and values, process Q queries where sweets can be bought subject to 2D range restrictions on coordinates and capacity constraints.

## 2. Core Observation & Invariant
The problem requires dynamic 2D point additions and 2D prefix/rectangle aggregations. Because one coordinate has bounded range while the other is large, a Fenwick tree over the first coordinate where each node contains a dynamic segment tree over the second coordinate provides O(log^2 N) point updates and range queries without storing unnecessary empty nodes.

## 3. Step-by-Step Algorithm
1. Implement a dynamic segment tree node with left/right child pointers.
2. Wrap dynamic segment trees inside a 1D Fenwick tree (Fenwick tree of dynamic segment trees).
3. For point updates (x, y, val): update Fenwick tree indices along x, inserting/updating (y, val) in the corresponding dynamic segment tree.
4. For range queries: query O(log N) dynamic segment trees simultaneously, walking down their nodes to aggregate values in O(log^2 N) time.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q log^2 N)`
- **Space Complexity**: `O(Q log^2 N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_VAL = 1000000000;

struct Node {
    int lc, rc;
    int cnt;
    long long sum;
};

const int MAX_NODES = 12000000;
Node tree[MAX_NODES];
int node_cnt = 0;

int new_node() {
    node_cnt++;
    tree[node_cnt].lc = 0;
    tree[node_cnt].rc = 0;
    tree[node_cnt].cnt = 0;
    tree[node_cnt].sum = 0;
    return node_cnt;
}

void update_val(int& node, int l, int r, int val, int delta) {
    if (!node) node = new_node();
    tree[node].cnt += delta;
    tree[node].sum += 1LL * delta * val;
    if (l == r) return;
    int mid = l + (r - l) / 2;
    if (val <= mid) {
        update_val(tree[node].lc, l, mid, val, delta);
    } else {
        update_val(tree[node].rc, mid + 1, r, val, delta);
    }
}

int N, Q;
vector<int> bit_roots;
vector<int> A;

void bit_add(int idx, int val, int delta) {
    for (; idx <= N; idx += idx & -idx) {
        update_val(bit_roots[idx], 1, MAX_VAL, val, delta);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> N >> Q)) return 0;
    A.resize(N + 1);
    bit_roots.assign(N + 1, 0);

    for (int i = 1; i <= N; i++) {
        cin >> A[i];
        bit_add(i, A[i], 1);
    }

    vector<int> pos_roots, neg_roots;
    pos_roots.reserve(25);
    neg_roots.reserve(25);

    while (Q--) {
        int c, x, l, r;
        long long k;
        cin >> c >> x >> l >> r >> k;

        // Point update
        bit_add(c, A[c], -1);
        A[c] = x;
        bit_add(c, A[c], 1);

        // Range query [l, r]
        pos_roots.clear();
        neg_roots.clear();

        for (int idx = r; idx > 0; idx -= idx & -idx) {
            if (bit_roots[idx]) pos_roots.push_back(bit_roots[idx]);
        }
        for (int idx = l - 1; idx > 0; idx -= idx & -idx) {
            if (bit_roots[idx]) neg_roots.push_back(bit_roots[idx]);
        }

        // First check total sum
        long long total_sum = 0;
        for (int rt : pos_roots) total_sum += tree[rt].sum;
        for (int rt : neg_roots) total_sum -= tree[rt].sum;

        if (total_sum < k) {
            cout << -1 << "\n";
            continue;
        }

        int cur_l = 1, cur_r = MAX_VAL;
        int ans_count = 0;

        while (cur_l < cur_r) {
            int mid = cur_l + (cur_r - cur_l) / 2;
            long long right_sum = 0;
            int right_cnt = 0;

            for (int rt : pos_roots) {
                int rc = tree[rt].rc;
                if (rc) {
                    right_sum += tree[rc].sum;
                    right_cnt += tree[rc].cnt;
                }
            }
            for (int rt : neg_roots) {
                int rc = tree[rt].rc;
                if (rc) {
                    right_sum -= tree[rc].sum;
                    right_cnt -= tree[rc].cnt;
                }
            }

            if (right_sum < k) {
                ans_count += right_cnt;
                k -= right_sum;
                // Move all to left child
                for (int i = 0; i < (int)pos_roots.size(); i++) {
                    pos_roots[i] = tree[pos_roots[i]].lc;
                }
                for (int i = 0; i < (int)neg_roots.size(); i++) {
                    neg_roots[i] = tree[neg_roots[i]].lc;
                }
                cur_r = mid;
            } else {
                // Move all to right child
                for (int i = 0; i < (int)pos_roots.size(); i++) {
                    pos_roots[i] = tree[pos_roots[i]].rc;
                }
                for (int i = 0; i < (int)neg_roots.size(); i++) {
                    neg_roots[i] = tree[neg_roots[i]].rc;
                }
                cur_l = mid + 1;
            }
        }

        // At leaf cur_l == cur_r
        long long needed = (k + cur_l - 1) / cur_l;
        ans_count += needed;
        cout << ans_count << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
