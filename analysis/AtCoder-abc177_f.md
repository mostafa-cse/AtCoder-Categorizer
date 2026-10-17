# Problem Analysis: AtCoder-abc177_f — F. I hate Shortest Path Problem

**Problem ID**: `AtCoder-abc177_f`  
**Contest**: `abc177`  
**Rating / Difficulty**: 2291  
**URL**: https://atcoder.jp/contests/abc177/tasks/abc177_f  
**VJudge Tag**: `[problem:AtCoder-abc177_f]`  
**Category File**: [`../categories/data_structures/lazy_segment_tree_grid_path_chmin.md`](../categories/data_structures/lazy_segment_tree_grid_path_chmin.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Segment Tree with Lazy Propagation`  

---

## 1. Problem Statement & Key Idea
In an $(H+1) \times W$ grid where each row $i$ has an impassable block $[A_i, B_i]$, find the minimum path length from row 1 to row $i+1$ moving only down or right for each $i = 1, \dots, H$.

## 2. Core Observation & Invariant
In an $(H+1) \times W$ grid, moving downwards increases moves by 1 everywhere. Blocking interval $[A_i, B_i]$ forces paths ending in $[A_i, B_i]$ to detour rightwards to $B_i + 1$, transforming reaching costs in $[A_i, B_i]$ into a single minimum detour candidate placed at $B_i + 1$. Maintaining values with lazy segment tree and a multiset provides running global minima in $O(\log W)$ per row.

## 3. Step-by-Step Algorithm
1. 1. Let $dp[c]$ be the minimum number of horizontal moves to reach column $c$ at the current row.
2. 2. In row $i$, every vertical step adds $1$ to all reachable columns (accumulated into a global offset $+i$).
3. 3. An obstacle blocks columns $[A_i, B_i]$. Any path arriving inside $[A_i, B_i]$ cannot move straight down. It must walk to $B_i + 1$. The cost to reach $B_i + 1$ from any $c \in [A_i, B_i]$ is $dp[c] + (B_i + 1 - c)$.
4. 4. Thus, we query the range minimum of $dp[c] - c$ for $c \in [A_i, B_i]$. Let this be $M_{best}$. Then $dp[B_i + 1]$ becomes $\min(dp[B_i + 1], M_{best} + B_i + 1)$.
5. 5. All entries $dp[c]$ for $c \in [A_i, B_i]$ become unreachable (set to $\infty$).
6. 6. We maintain $dp[c]$ and $dp[c] - c$ in a Segment Tree supporting range assignment, point updates, and maintain all active values in a `multiset` or segment tree root to query the global minimum in $O(\log W)$ per row.

## 4. Complexity Analysis
- **Time Complexity**: `O(H + W \log W)`
- **Space Complexity**: `O(W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

const int INF = 1e9;

struct SegTree {
    int n;
    vector<int> min_val;
    vector<int> min_diff; // min of (val - pos)
    vector<int> lazy_val;

    SegTree(int n) : n(n) {
        min_val.assign(4 * n + 5, INF);
        min_diff.assign(4 * n + 5, INF);
        lazy_val.assign(4 * n + 5, -1);
        build(1, 1, n);
    }

    void build(int node, int l, int r) {
        if (l == r) {
            min_val[node] = 0;
            min_diff[node] = -l;
            return;
        }
        int mid = (l + r) / 2;
        build(2 * node, l, mid);
        build(2 * node + 1, mid + 1, r);
        min_val[node] = min(min_val[2 * node], min_val[2 * node + 1]);
        min_diff[node] = min(min_diff[2 * node], min_diff[2 * node + 1]);
    }

    void push(int node, int l, int r) {
        if (lazy_val[node] != -1) {
            int v = lazy_val[node];
            int mid = (l + r) / 2;
            
            // Left child
            min_val[2 * node] = v;
            min_diff[2 * node] = (v >= INF ? INF : v - mid); // upper bound diff
            lazy_val[2 * node] = v;

            // Right child
            min_val[2 * node + 1] = v;
            min_diff[2 * node + 1] = (v >= INF ? INF : v - r);
            lazy_val[2 * node + 1] = v;

            lazy_val[node] = -1;
        }
    }

    void update_set_inf(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return;
        if (ql <= l && r <= qr) {
            min_val[node] = INF;
            min_diff[node] = INF;
            lazy_val[node] = INF;
            return;
        }
        push(node, l, r);
        int mid = (l + r) / 2;
        update_set_inf(2 * node, l, mid, ql, qr);
        update_set_inf(2 * node + 1, mid + 1, r, ql, qr);
        min_val[node] = min(min_val[2 * node], min_val[2 * node + 1]);
        min_diff[node] = min(min_diff[2 * node], min_diff[2 * node + 1]);
    }

    void update_point(int node, int l, int r, int idx, int val) {
        if (l == r) {
            min_val[node] = min(min_val[node], val);
            min_diff[node] = min_val[node] - l;
            lazy_val[node] = -1;
            return;
        }
        push(node, l, r);
        int mid = (l + r) / 2;
        if (idx <= mid) update_point(2 * node, l, mid, idx, val);
        else update_point(2 * node + 1, mid + 1, r, idx, val);
        min_val[node] = min(min_val[2 * node], min_val[2 * node + 1]);
        min_diff[node] = min(min_diff[2 * node], min_diff[2 * node + 1]);
    }

    int query_min_diff(int node, int l, int r, int ql, int qr) {
        if (ql > r || qr < l) return INF;
        if (ql <= l && r <= qr) return min_diff[node];
        push(node, l, r);
        int mid = (l + r) / 2;
        return min(query_min_diff(2 * node, l, mid, ql, qr),
                   query_min_diff(2 * node + 1, mid + 1, r, ql, qr));
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    // We store (val, col) in a std::set to maintain active values accurately
    // For each col, we have its current val
    set<pair<int, int>> active_by_col; // (col, val)
    multiset<int> all_vals;

    for (int c = 1; c <= W; ++c) {
        active_by_col.insert({c, 0});
        all_vals.insert(0);
    }

    for (int row = 1; row <= H; ++row) {
        int A, B;
        cin >> A >> B;

        // Find all columns in [A, B]
        auto it = active_by_col.lower_bound({A, -1});
        int best_diff = INF;
        vector<pair<int, int>> to_remove;
        while (it != active_by_col.end() && it->first <= B) {
            best_diff = min(best_diff, it->second - it->first);
            all_vals.erase(all_vals.find(it->second));
            to_remove.push_back(*it);
            it++;
        }
        for (auto& p : to_remove) {
            active_by_col.erase(p);
        }

        if (best_diff < INF && B + 1 <= W) {
            int new_val = best_diff + (B + 1);
            // Check if B + 1 already has an entry
            auto next_it = active_by_col.lower_bound({B + 1, -1});
            if (next_it != active_by_col.end() && next_it->first == B + 1) {
                if (new_val < next_it->second) {
                    all_vals.erase(all_vals.find(next_it->second));
                    active_by_col.erase(next_it);
                    active_by_col.insert({B + 1, new_val});
                    all_vals.insert(new_val);
                }
            } else {
                active_by_col.insert({B + 1, new_val});
                all_vals.insert(new_val);
            }
        }

        if (all_vals.empty()) {
            cout << -1 << "\n";
        } else {
            cout << *all_vals.begin() + row << "\n";
        }
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
