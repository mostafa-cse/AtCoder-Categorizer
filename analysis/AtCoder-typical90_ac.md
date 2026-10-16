# Problem Analysis: AtCoder-typical90_ac — Long Bricks

**Problem ID**: `AtCoder-typical90_ac`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 029)  
**Rating / Difficulty**: 1750 (★5)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_ac  
**VJudge Tag**: `[problem:AtCoder-typical90_ac]`  
**Category File**: [`../categories/data_structures/lazy_segment_tree_coordinate_compression.md`](../categories/data_structures/lazy_segment_tree_coordinate_compression.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree / Fenwick Tree`  
- **Topic (Skill)**: `Dynamic Coordinate Compression + Lazy Segment Tree`  

---

## 1. Problem Statement & Key Idea
W-wide ground (W <= 10^9). N bricks fall in order. Brick i spans [L_i, R_i], lands on top of existing bricks in that range, and levels that range to max_height + 1. Output landing height of each brick.

**Core Idea**: Range maximum query and range assignment update using a Segment Tree with Lazy Propagation.

## 2. Core Observation & Invariant
Since W <= 10^9 is large but N <= 10^5, coordinate compress all 2N interval endpoints {L_i, R_i} into an array of size <= 2 * 10^5.

## 3. Step-by-Step Algorithm
1. Collect and coordinate-compress all L_i and R_i.
2. Build Lazy Segment Tree supporting Range Max Query and Range Assignment Update.
3. For each brick: query max height h in [compressed(L_i), compressed(R_i)].
4. Update range [compressed(L_i), compressed(R_i)] to h + 1.
5. Output h + 1.

## 4. Complexity Analysis
Time: O(N log N), Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct LazySegTree {
    int n;
    vector<int> tree, lazy;
    LazySegTree(int n) : n(n), tree(4 * n, 0), lazy(4 * n, 0) {}

    void push(int node) {
        if (lazy[node] != 0) {
            lazy[2 * node] = max(lazy[2 * node], lazy[node]);
            tree[2 * node] = max(tree[2 * node], lazy[node]);
            lazy[2 * node + 1] = max(lazy[2 * node + 1], lazy[node]);
            tree[2 * node + 1] = max(tree[2 * node + 1], lazy[node]);
            lazy[node] = 0;
        }
    }

    void update(int node, int start, int end, int l, int r, int val) {
        if (r < start || end < l) return;
        if (l <= start && end <= r) {
            tree[node] = max(tree[node], val);
            lazy[node] = max(lazy[node], val);
            return;
        }
        push(node);
        int mid = (start + end) / 2;
        update(2 * node, start, mid, l, r, val);
        update(2 * node + 1, mid + 1, end, l, r, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node];
        push(node);
        int mid = (start + end) / 2;
        return max(query(2 * node, start, mid, l, r),
                   query(2 * node + 1, mid + 1, end, l, r));
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int w, n;
    if (!(cin >> w >> n)) return 0;

    vector<pair<int, int>> queries(n);
    vector<int> coords;
    coords.reserve(2 * n);

    for (int i = 0; i < n; ++i) {
        cin >> queries[i].first >> queries[i].second;
        coords.push_back(queries[i].first);
        coords.push_back(queries[i].second);
    }

    sort(coords.begin(), coords.end());
    coords.erase(unique(coords.begin(), coords.end()), coords.end());

    auto get_id = [&](int x) {
        return (int)(lower_bound(coords.begin(), coords.end(), x) - coords.begin()) + 1;
    };

    int m = coords.size();
    LazySegTree seg(m);

    for (int i = 0; i < n; ++i) {
        int l = get_id(queries[i].first);
        int r = get_id(queries[i].second);
        int cur_max = seg.query(1, 1, m, l, r);
        int new_h = cur_max + 1;
        seg.update(1, 1, m, l, r, new_h);
        cout << new_h << "\n";
    }
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Coordinate compression and lazy range update on Segment Tree.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Handling massive coordinate ranges up to 10^9 via compression and maintaining interval heights with lazy segment tree.
- **Reusable Pattern**: `Coordinate Compression + Lazy Segment Tree Range Max.`

---
Back to [Dynamic Coordinate Compression + Lazy Segment Tree](../categories/data_structures/lazy_segment_tree_coordinate_compression.md) | [Categories Directory](../categories/README.md)