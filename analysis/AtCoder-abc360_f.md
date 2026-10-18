# Problem Analysis: AtCoder-abc360_f — F - InterSections

**Problem ID**: `AtCoder-abc360_f`  
**Contest**: `abc360`  
**Rating / Difficulty**: 2563  
**URL**: https://atcoder.jp/contests/abc360/tasks/abc360_f  
**VJudge Tag**: `[problem:AtCoder-abc360_f]`  
**Category File**: [`../categories/geometry/intersections_sweep_line_lazy_segtree.md`](../categories/geometry/intersections_sweep_line_lazy_segtree.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Sweep Line`  
- **Topic (Skill)**: `Sweep Line Algorithm and Radial Sweep`  

---

## 1. Problem Statement & Key Idea
Find an open interval $(L, R)$ that intersects the maximum number of given intervals $(l_i, r_i)$.

## 2. Core Observation & Invariant
Two intervals $(L, R)$ and $(l_i, r_i)$ intersect (with non-empty intersection and neither containing the other) iff either $L < l_i < R < r_i$ or $l_i < L < r_i < R$. In the $(L, R)$ plane, each given interval $(l_i, r_i)$ defines a union of 2D axis-aligned rectangles of valid $(L, R)$ pairs. The problem reduces to finding a point $(L, R)$ covered by the maximum number of rectangles, solved via a Sweep Line with a Lazy Segment Tree.

## 3. Step-by-Step Algorithm
1. 1. For each given interval $(l_i, r_i)$, generate rectangle addition events on the $(L, R)$ plane.
2. 2. Discretize and coordinate-compress all $x$ and $y$ event coordinates.
3. 3. Sort sweep-line events along the $L$-axis.
4. 4. Maintain coverage counts on the $R$-axis using a Lazy Segment Tree supporting range addition and range maximum query.
5. 5. Track the global maximum and reconstruct the optimal integer pair $(L, R)$.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Event {
    int type; // +1 or -1
    int y1, y2;
};

struct Node {
    int max_val;
    int max_idx;
};

struct LazySegTree {
    int n;
    vector<Node> tree;
    vector<int> lazy;

    LazySegTree(int n) : n(n) {
        tree.resize(4 * n);
        lazy.assign(4 * n, 0);
        build(1, 0, n - 1);
    }

    void build(int v, int tl, int tr) {
        tree[v].max_val = 0;
        tree[v].max_idx = tl;
        if (tl < tr) {
            int tm = (tl + tr) / 2;
            build(2 * v, tl, tm);
            build(2 * v + 1, tm + 1, tr);
        }
    }

    void apply(int v, int val) {
        tree[v].max_val += val;
        lazy[v] += val;
    }

    void push(int v) {
        if (lazy[v] != 0) {
            apply(2 * v, lazy[v]);
            apply(2 * v + 1, lazy[v]);
            lazy[v] = 0;
        }
    }

    void update(int v, int tl, int tr, int l, int r, int val) {
        if (l > r) return;
        if (l == tl && r == tr) {
            apply(v, val);
            return;
        }
        push(v);
        int tm = (tl + tr) / 2;
        update(2 * v, tl, tm, l, min(r, tm), val);
        update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, val);
        if (tree[2 * v].max_val >= tree[2 * v + 1].max_val) {
            tree[v] = tree[2 * v];
        } else {
            tree[v] = tree[2 * v + 1];
        }
    }

    Node query(int v, int tl, int tr, int l, int r) {
        if (l > r) return {-1, -1};
        if (l == tl && r == tr) return tree[v];
        push(v);
        int tm = (tl + tr) / 2;
        Node left_node = query(2 * v, tl, tm, l, min(r, tm));
        Node right_node = query(2 * v + 1, tm + 1, tr, max(l, tm + 1), r);
        if (left_node.max_val >= right_node.max_val) return left_node;
        return right_node;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<pair<int, int>> intervals(N);
    vector<int> all_x, all_y;
    all_x.push_back(0);
    all_y.push_back(1);

    struct Rect {
        int x1, x2, y1, y2;
    };
    vector<Rect> rects;

    for (int i = 0; i < N; ++i) {
        cin >> intervals[i].first >> intervals[i].second;
        int l = intervals[i].first;
        int r = intervals[i].second;

        // Rect 1
        if (0 <= l - 1 && l + 1 <= r - 1) {
            rects.push_back({0, l - 1, l + 1, r - 1});
            all_x.push_back(0);
            all_x.push_back(l);
            all_y.push_back(l + 1);
            all_y.push_back(r - 1);
        }
        // Rect 2
        if (l + 1 <= r - 1 && r + 1 <= 1000000000) {
            rects.push_back({l + 1, r - 1, r + 1, 1000000000});
            all_x.push_back(l + 1);
            all_x.push_back(r);
            all_y.push_back(r + 1);
            all_y.push_back(1000000000);
        }
    }

    sort(all_x.begin(), all_x.end());
    all_x.erase(unique(all_x.begin(), all_x.end()), all_x.end());

    sort(all_y.begin(), all_y.end());
    all_y.erase(unique(all_y.begin(), all_y.end()), all_y.end());

    vector<vector<pair<int, pair<int, int>>>> events(all_x.size());
    for (const auto& rect : rects) {
        int x1_idx = lower_bound(all_x.begin(), all_x.end(), rect.x1) - all_x.begin();
        int x2_idx = lower_bound(all_x.begin(), all_x.end(), rect.x2 + 1) - all_x.begin();
        int y1_idx = lower_bound(all_y.begin(), all_y.end(), rect.y1) - all_y.begin();
        int y2_idx = lower_bound(all_y.begin(), all_y.end(), rect.y2) - all_y.begin();

        events[x1_idx].push_back({1, {y1_idx, y2_idx}});
        if (x2_idx < all_x.size()) {
            events[x2_idx].push_back({-1, {y1_idx, y2_idx}});
        }
    }

    LazySegTree seg(all_y.size());
    int best_val = 0;
    int best_l = 0;
    int best_r = 1;

    for (int i = 0; i < all_x.size(); ++i) {
        for (const auto& ev : events[i]) {
            seg.update(1, 0, all_y.size() - 1, ev.second.first, ev.second.second, ev.first);
        }

        int x_val = all_x[i];
        int y_start_idx = upper_bound(all_y.begin(), all_y.end(), x_val) - all_y.begin();
        if (y_start_idx < all_y.size()) {
            Node res = seg.query(1, 0, all_y.size() - 1, y_start_idx, all_y.size() - 1);
            if (res.max_val > best_val) {
                best_val = res.max_val;
                best_l = x_val;
                best_r = all_y[res.max_idx];
            }
        }
    }

    cout << best_l << " " << best_r << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
