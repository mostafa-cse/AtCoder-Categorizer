# Problem Analysis: AtCoder-abc430_g — G. Range Set Modifying Query

**Problem ID**: `AtCoder-abc430_g`  
**Contest**: `abc430`  
**Rating / Difficulty**: 2371  
**URL**: https://atcoder.jp/contests/abc430/tasks/abc430_g  
**VJudge Tag**: `[problem:AtCoder-abc430_g]`  
**Category File**: [`../categories/data_structures/odt_lazy_segtree_cardinality.md`](../categories/data_structures/odt_lazy_segtree_cardinality.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree with Lazy Propagation`  

---

## 1. Problem Statement & Key Idea
Maintain sets $S_1, \dots, S_N$ under range insertions/deletions of $x \in [1, 60]$ and query range max cardinality and count. Maintaining 60 ODT interval sets and mapping additions/removals to a lazy segment tree answers all queries in $O(Q \log N)$.

## 2. Core Observation & Invariant
Since values $x \in [1, 60]$ are bounded, maintain 60 independent interval sets (ODT) for presence of each $x$. Adding $x$ to $[L, R]$ identifies subsegments where $x$ was absent, adding $+1$ to those subsegments and inserting them into the ODT. Deleting $x$ identifies subsegments where $x$ was present, adding $-1$ and removing them. A lazy segment tree maintains range maximum cardinality and frequency count.

## 3. Step-by-Step Algorithm
1. For each $x \in [1, 60]$, maintain disjoint active intervals $[l, r]$ in a `std::set`.
2. Build a Segment Tree with lazy propagation maintaining $(max\_val, count, lazy)$ over array of size $N$.
3. Query 1 / Query 2: find overlapping/missing intervals with $[L, R]$, update the segment tree with $\pm 1$, and update the ODT in $O(\log N)$ amortized.
4. Query 3: range query the segment tree for maximum and count in $O(\log N)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(Q \log N)`
- **Space Complexity**: `O(N + Q)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int max_val;
    int count;
    int lazy;
};

const int MAXN = 300005;
Node tree[4 * MAXN];

void push_up(int u) {
    if (tree[2 * u].max_val > tree[2 * u + 1].max_val) {
        tree[u].max_val = tree[2 * u].max_val;
        tree[u].count = tree[2 * u].count;
    } else if (tree[2 * u].max_val < tree[2 * u + 1].max_val) {
        tree[u].max_val = tree[2 * u + 1].max_val;
        tree[u].count = tree[2 * u + 1].count;
    } else {
        tree[u].max_val = tree[2 * u].max_val;
        tree[u].count = tree[2 * u].count + tree[2 * u + 1].count;
    }
}

void apply_lazy(int u, int val) {
    tree[u].max_val += val;
    tree[u].lazy += val;
}

void push_down(int u) {
    if (tree[u].lazy != 0) {
        apply_lazy(2 * u, tree[u].lazy);
        apply_lazy(2 * u + 1, tree[u].lazy);
        tree[u].lazy = 0;
    }
}

void build(int u, int l, int r) {
    tree[u].lazy = 0;
    if (l == r) {
        tree[u].max_val = 0;
        tree[u].count = 1;
        return;
    }
    int mid = (l + r) / 2;
    build(2 * u, l, mid);
    build(2 * u + 1, mid + 1, r);
    push_up(u);
}

void update_range(int u, int l, int r, int ql, int qr, int val) {
    if (ql <= l && r <= qr) {
        apply_lazy(u, val);
        return;
    }
    push_down(u);
    int mid = (l + r) / 2;
    if (ql <= mid) update_range(2 * u, l, mid, ql, qr, val);
    if (qr > mid) update_range(2 * u + 1, mid + 1, r, ql, qr, val);
    push_up(u);
}

pair<int, int> query_range(int u, int l, int r, int ql, int qr) {
    if (ql <= l && r <= qr) return {tree[u].max_val, tree[u].count};
    push_down(u);
    int mid = (l + r) / 2;
    if (qr <= mid) return query_range(2 * u, l, mid, ql, qr);
    if (ql > mid) return query_range(2 * u + 1, mid + 1, r, ql, qr);
    auto left_res = query_range(2 * u, l, mid, ql, qr);
    auto right_res = query_range(2 * u + 1, mid + 1, r, ql, qr);
    if (left_res.first > right_res.first) return left_res;
    if (left_res.first < right_res.first) return right_res;
    return {left_res.first, left_res.second + right_res.second};
}

// ODT for each value x in [1, 60]
set<pair<int, int>> intervals[65];

void add_val(int l, int r, int x, int n) {
    auto it = intervals[x].upper_bound({l, 2e9});
    if (it != intervals[x].begin()) it--;

    vector<pair<int, int>> overlaps;
    while (it != intervals[x].end() && it->first <= r) {
        if (it->second >= l) overlaps.push_back(*it);
        it++;
    }

    int cur_l = l;
    int merged_l = l, merged_r = r;
    for (auto& seg : overlaps) {
        intervals[x].erase(seg);
        merged_l = min(merged_l, seg.first);
        merged_r = max(merged_r, seg.second);
        if (seg.first > cur_l) {
            update_range(1, 1, n, cur_l, seg.first - 1, 1);
        }
        cur_l = max(cur_l, seg.second + 1);
    }
    if (cur_l <= r) {
        update_range(1, 1, n, cur_l, r, 1);
    }
    intervals[x].insert({merged_l, merged_r});
}

void del_val(int l, int r, int x, int n) {
    auto it = intervals[x].upper_bound({l, 2e9});
    if (it != intervals[x].begin()) it--;

    vector<pair<int, int>> overlaps;
    while (it != intervals[x].end() && it->first <= r) {
        if (it->second >= l) overlaps.push_back(*it);
        it++;
    }

    for (auto& seg : overlaps) {
        intervals[x].erase(seg);
        int ol = max(l, seg.first);
        int or_r = min(r, seg.second);
        update_range(1, 1, n, ol, or_r, -1);
        if (seg.first < ol) intervals[x].insert({seg.first, ol - 1});
        if (seg.second > or_r) intervals[x].insert({or_r + 1, seg.second});
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    build(1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r, x;
            cin >> l >> r >> x;
            add_val(l, r, x, n);
        } else if (type == 2) {
            int l, r, x;
            cin >> l >> r >> x;
            del_val(l, r, x, n);
        } else {
            int l, r;
            cin >> l >> r;
            auto res = query_range(1, 1, n, l, r);
            cout << res.first << " " << res.second << "\n";
        }
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
