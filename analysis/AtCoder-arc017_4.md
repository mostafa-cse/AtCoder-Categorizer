# Problem Analysis: AtCoder-arc017_4 — ARCたんクッキー

**Problem ID**: `AtCoder-arc017_4`  
**Contest**: `arc017`  
**Rating / Difficulty**: 2244  
**URL**: https://atcoder.jp/contests/arc017/tasks/arc017_4  
**VJudge Tag**: `[problem:AtCoder-arc017_4]`  
**Category File**: [`../categories/data_structures/segment_tree_range_add_range_gcd_difference_array.md`](../categories/data_structures/segment_tree_range_add_range_gcd_difference_array.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree (Point Update Range Query)`  

---

## 1. Problem Statement & Key Idea
Maintain an array under range additions [l, r] += t and range greatest common divisor queries gcd(a_l, ..., a_r).

## 2. Core Observation & Invariant
By the Euclidean algorithm property gcd(x, y) = gcd(x, y - x), the GCD of a range satisfies gcd(a_l, a_{l+1}, ..., a_r) = gcd(a_l, gcd_{i=l+1}^r |a_i - a_{i-1}|). Under the difference array D_i = a_i - a_{i-1}, a range addition [l, r] += t modifies only two elements: D_l += t and D_{r+1} -= t. Thus, range additions become point updates on D, and range GCD queries become gcd(prefix_sum(l), range_gcd(D, l+1, r)).

## 3. Step-by-Step Algorithm
1. 1. Maintain the difference array D in a Segment Tree supporting point updates and range GCD queries.
2. 2. Maintain prefix sums of D in a Fenwick Tree to query any single value a_l in O(log N).
3. 3. For range addition (t != 0, l, r): update D_l += t and D_{r+1} -= t in both Fenwick and Segment Tree.
4. 4. For range GCD (t == 0, l, r): query a_l from Fenwick tree, query gcd of D on [l+1, r] from Segment Tree, and output their GCD.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) log N log(max_val))`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <cmath>

using namespace std;

long long gcd_ll(long long a, long long b) {
    a = std::abs(a);
    b = std::abs(b);
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

// Fenwick Tree for point update, prefix sum
struct Fenwick {
    int n;
    vector<long long> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}
    void add(int i, long long delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

// Segment tree for point update, range GCD
struct SegTree {
    int n;
    vector<long long> tree;
    SegTree(int n) : n(n), tree(4 * n + 1, 0) {}

    void update(int node, int start, int end, int idx, long long val) {
        if (start == end) {
            tree[node] = abs(val);
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = gcd_ll(tree[2 * node], tree[2 * node + 1]);
    }

    long long query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node];
        int mid = start + (end - start) / 2;
        long long left_gcd = query(2 * node, start, mid, l, r);
        long long right_gcd = query(2 * node + 1, mid + 1, end, l, r);
        return gcd_ll(left_gcd, right_gcd);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n)) return 0;

    vector<long long> a(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> a[i];
    }

    vector<long long> D(n + 1);
    for (int i = 1; i <= n; ++i) {
        D[i] = a[i] - a[i - 1];
    }

    Fenwick bit(n);
    SegTree seg(n);

    for (int i = 1; i <= n; ++i) {
        bit.add(i, D[i]);
        seg.update(1, 1, n, i, D[i]);
    }

    int m;
    if (!(cin >> m)) return 0;

    while (m--) {
        long long t;
        int l, r;
        cin >> t >> l >> r;
        if (t != 0) {
            // Range addition [l, r] += t
            D[l] += t;
            bit.add(l, t);
            seg.update(1, 1, n, l, D[l]);

            if (r + 1 <= n) {
                D[r + 1] -= t;
                bit.add(r + 1, -t);
                seg.update(1, 1, n, r + 1, D[r + 1]);
            }
        } else {
            // Range GCD on [l, r]
            long long a_l = bit.query(l);
            long long diff_gcd = 0;
            if (l + 1 <= r) {
                diff_gcd = seg.query(1, 1, n, l + 1, r);
            }
            long long ans = gcd_ll(a_l, diff_gcd);
            cout << ans << "\n";
        }
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
