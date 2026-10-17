# Problem Analysis: AtCoder-abc218_g — Game on Tree 2

**Problem ID**: `AtCoder-abc218_g`  
**Contest**: `abc218`  
**Rating / Difficulty**: 2217  
**URL**: https://atcoder.jp/contests/abc218/tasks/abc218_g  
**VJudge Tag**: `[problem:AtCoder-abc218_g]`  
**Category File**: [`../categories/game_theory/game_on_tree_2_minimax_bit_median.md`](../categories/game_theory/game_on_tree_2_minimax_bit_median.md)  

- **Tag (Domain)**: `Game Theory`  
- **Subtopic**: `Graph Games`  
- **Topic (Skill)**: `Games on Arbitrary Graphs`  

---

## 1. Problem Statement & Key Idea
Two players play a game on a tree moving a piece downwards from root 1 to a leaf. Taro maximizes the median of node values visited, Jiro minimizes it. Find the final median score under optimal play.

## 2. Core Observation & Invariant
The game is a finite full-information extensive-form game on a tree, solvable by Minimax DFS. Since path length increases by 1 at each step, running order statistics (median) along the path from root to leaf can be maintained dynamically in O(log N) using a Fenwick tree with binary lifting over coordinate-compressed values.

## 3. Step-by-Step Algorithm
1. 1. Coordinate compress node values A_i.
2. 2. Traverse tree via DFS, maintaining frequency of path nodes in a Fenwick tree.
3. 3. At leaf nodes, query the (k+1)/2-th element (if odd length) or average of k/2 and k/2+1 elements (if even length) via binary lifting on Fenwick tree.
4. 4. At internal nodes, take maximum over children on Taro's turns (even depth) and minimum over children on Jiro's turns (odd depth).
5. 5. Backtrack node insertion in Fenwick tree upon returning from DFS.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

// Coordinate compression + Fenwick Tree for order statistics
struct Fenwick {
    int n;
    vector<int> tree;
    Fenwick(int n) : n(n), tree(n + 1, 0) {}

    void add(int i, int delta) {
        for (; i <= n; i += i & -i) tree[i] += delta;
    }

    // find smallest index with prefix sum >= k (1-indexed k)
    int find_kth(int k) {
        int idx = 0;
        for (int p = 1 << 18; p > 0; p >>= 1) {
            if (idx + p <= n && tree[idx + p] < k) {
                idx += p;
                k -= tree[idx];
            }
        }
        return idx + 1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    vector<int> vals;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        vals.push_back(a[i]);
    }

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    int sz = vals.size();
    Fenwick bit(sz);

    vector<vector<int>> adj(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto get_median = [&](int path_len) {
        if (path_len % 2 == 1) {
            int k = (path_len + 1) / 2;
            int idx = bit.find_kth(k);
            return vals[idx - 1];
        } else {
            int k1 = path_len / 2;
            int k2 = k1 + 1;
            int idx1 = bit.find_kth(k1);
            int idx2 = bit.find_kth(k2);
            return (vals[idx1 - 1] + vals[idx2 - 1]) / 2;
        }
    };

    // DFS Minimax
    function<int(int, int, int)> dfs = [&](int u, int p, int depth) {
        int rk = lower_bound(vals.begin(), vals.end(), a[u]) - vals.begin() + 1;
        bit.add(rk, 1);

        vector<int> child_vals;
        for (int v : adj[u]) {
            if (v == p) continue;
            child_vals.push_back(dfs(v, u, depth + 1));
        }

        int res;
        if (child_vals.empty()) {
            // Leaf
            res = get_median(depth + 1);
        } else {
            if (depth % 2 == 0) {
                // Taro's turn: maximize
                res = 0;
                for (int val : child_vals) res = max(res, val);
            } else {
                // Jiro's turn: minimize
                res = 2e9;
                for (int val : child_vals) res = min(res, val);
            }
        }

        bit.add(rk, -1);
        return res;
    };

    int ans = dfs(0, -1, 0);
    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
