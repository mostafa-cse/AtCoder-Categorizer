# Problem Analysis: AtCoder-arc080_c — E. Young Maids

**Problem ID**: `AtCoder-arc080_c`  
**Contest**: `arc080`  
**Rating / Difficulty**: 2277  
**URL**: https://atcoder.jp/contests/arc080/tasks/arc080_c  
**VJudge Tag**: `[problem:AtCoder-arc080_c]`  
**Category File**: [`../categories/data_structures_ds/segment_tree_lexicographical_permutation_rmq_pair_peeling.md`](../categories/data_structures_ds/segment_tree_lexicographical_permutation_rmq_pair_peeling.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Given a permutation $P$ of length $2N$, repeatedly select an adjacent pair $(P_i, P_{i+1})$ in the current sequence to place at the front of a new sequence, prioritizing lexicographically smallest sequences. Find the resulting permutation.

## 2. Core Observation & Invariant
In any sequence of adjacent pair removals, every removed pair $(x, y)$ originally occupied an even-length interval between them and had alternating parities relative to the subarray boundary. The problem greedily decouples into independent even-length subsegments $[l, pos(x)-1]$, $[pos(x)+1, pos(y)-1]$, and $[pos(y)+1, r]$ managed by a priority queue.

## 3. Step-by-Step Algorithm
1. 1. Prepending pairs to $q$ means the first pair in $q$ was the LAST pair removed from $p$. In reverse, to make $q$ lexicographically smallest, we greedily pick the minimum possible $x$ and corresponding $y$ at each step.\n2. When two elements $x, y$ are removed from an even-length interval $[l, r]$, all elements between them must have been removed in pairs, meaning the number of elements between $x$ and $y$ is even, and the elements before $x$ and after $y$ also have even counts.\n3. Hence, $x$ must share the same parity as $l$, and $y$ must have opposite parity and appear after $x$. To minimize $(x, y)$, choose $x = \arg\min_{i \equiv l \pmod 2, i \in [l, r]} p[i]$ and $y = \arg\min_{j \not\equiv l \pmod 2, j \in [pos(x)+1, r]} p[j]$.\n4. After choosing $(x, y)$, the interval $[l, r]$ splits into up to 3 even-length intervals: $[l, pos(x)-1]$, $[pos(x)+1, pos(y)-1]$, and $[pos(y)+1, r]$.\n5. Maintain all active intervals in a `std::priority_queue` keyed by their minimum $x$ value. Finding $(x, y)$ per interval is performed via RMQ on two Segment Trees (one for even indices, one for odd). Overall time is $O(N \log N)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct SegmentTree {
    int n;
    vector<pair<int, int>> tree;

    void init(int n_) {
        n = n_;
        tree.assign(4 * n + 1, {INF, -1});
    }

    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            tree[node] = {val, idx};
            return;
        }
        int mid = (l + r) / 2;
        if (idx <= mid) update(2 * node, l, mid, idx, val);
        else update(2 * node + 1, mid + 1, r, idx, val);
        tree[node] = min(tree[2 * node], tree[2 * node + 1]);
    }

    pair<int, int> query(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return {INF, -1};
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) / 2;
        return min(query(2 * node, l, mid, ql, qr), query(2 * node + 1, mid + 1, r, ql, qr));
    }
} st[2];

struct Interval {
    int l, r;
    int x_val, x_idx;
    int y_val, y_idx;

    bool operator>(const Interval& other) const {
        return x_val > other.x_val;
    }
};

Interval make_interval(int l, int r, int n) {
    int parity_l = l % 2;
    pair<int, int> qx = st[parity_l].query(1, 0, n - 1, l, r);
    int x_val = qx.first;
    int x_idx = qx.second;

    int parity_r = 1 - parity_l;
    pair<int, int> qy = st[parity_r].query(1, 0, n - 1, x_idx + 1, r);
    int y_val = qy.first;
    int y_idx = qy.second;

    return {l, r, x_val, x_idx, y_val, y_idx};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> p(n);
    st[0].init(n);
    st[1].init(n);

    for (int i = 0; i < n; i++) {
        cin >> p[i];
        st[i % 2].update(1, 0, n - 1, i, p[i]);
    }

    priority_queue<Interval, vector<Interval>, greater<Interval>> pq;
    pq.push(make_interval(0, n - 1, n));

    vector<int> q;
    q.reserve(n);

    while (!pq.empty()) {
        Interval cur = pq.top();
        pq.pop();

        q.push_back(cur.x_val);
        q.push_back(cur.y_val);

        if (cur.l <= cur.x_idx - 1) {
            pq.push(make_interval(cur.l, cur.x_idx - 1, n));
        }
        if (cur.x_idx + 1 <= cur.y_idx - 1) {
            pq.push(make_interval(cur.x_idx + 1, cur.y_idx - 1, n));
        }
        if (cur.y_idx + 1 <= cur.r) {
            pq.push(make_interval(cur.y_idx + 1, cur.r, n));
        }
    }

    for (int i = 0; i < n; i++) {
        cout << q[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
