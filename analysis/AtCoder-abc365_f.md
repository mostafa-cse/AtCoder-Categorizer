# Problem Analysis: AtCoder-abc365_f — F - Takahashi on Grid

**Problem ID**: `AtCoder-abc365_f`  
**Contest**: `abc365`  
**Rating / Difficulty**: 2561  
**URL**: https://atcoder.jp/contests/abc365/tasks/abc365_f  
**VJudge Tag**: `[problem:AtCoder-abc365_f]`  
**Category File**: [`../categories/data_structures_ds/takahashi_on_grid_iterative_segtree.md`](../categories/data_structures_ds/takahashi_on_grid_iterative_segtree.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Segment Tree`  
- **Topic (Skill)**: `Iterative Segment Tree`  

---

## 1. Problem Statement & Key Idea
Answer $Q$ distance queries on a grid where each column $x \in [1, N]$ has walkable vertical interval $[L_x, U_x]$.

## 2. Core Observation & Invariant
When moving from column $x$ to $x+1$, the vertical coordinate $y$ is clamped to $[L_{x+1}, U_{x+1}]$. Clamping functions $f(y) = \text{clamp}(y, f_L, f_U)$ and cost functions $g(y) = C + \max(y, g_L) - \min(y, g_U)$ form a monoid under composition. Thus, transitions across any range of columns can be composed and queried in $O(\log N)$ time using an Iterative Segment Tree.

## 3. Step-by-Step Algorithm
1. 1. Represent each column as a block monoid: $f_L = g_L = L_x$, $f_U = g_U = U_x$, $C = 1$.
2. 2. Define associative merge operation for two blocks: compose clamp intervals and compute composite cost offset $C$.
3. 3. Build an iterative segment tree over all $N$ columns in $O(N)$ time.
4. 4. For each query $(s_x, s_y) \to (t_x, t_y)$ (assume $s_x \le t_x$):
5.    - Query segment tree for range $[s_x, t_x)$ to get composite block.
6.    - Apply block to $s_y$ to obtain final $y$ position and traversal cost.
7.    - Add $|y - t_y|$ to reach destination coordinate.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + Q \log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Block {
    long long fL, fU;
    long long gL, gU;
    long long C;

    pair<long long, long long> apply(long long y) const {
        long long out_y = clamp(y, fL, fU);
        long long cost = C + max(y, gL) - min(y, gU);
        return {out_y, cost};
    }
};

Block make_block(long long L, long long U) {
    return {L, U, L, U, 1};
}

Block unit_block() {
    return {0, 1000000001LL, 0, 1000000001LL, 0};
}

Block merge_blocks(const Block& lhs, const Block& rhs) {
    long long new_fL = clamp(lhs.fL, rhs.fL, rhs.fU);
    long long new_fU = clamp(lhs.fU, rhs.fL, rhs.fU);
    long long new_gL = clamp(rhs.gL, lhs.gL, lhs.gU);
    long long new_gU = clamp(rhs.gU, lhs.gL, lhs.gU);
    auto [out_m, c_m] = lhs.apply(new_gU);
    auto [out_r, c_r] = rhs.apply(out_m);
    long long new_C = lhs.C + c_r;
    return {new_fL, new_fU, new_gL, new_gU, new_C};
}

struct IterativeSegTree {
    int size;
    vector<Block> tree;

    IterativeSegTree(int n, const vector<pair<long long, long long>>& intervals) {
        size = 1;
        while (size < n) size *= 2;
        tree.assign(2 * size, unit_block());
        for (int i = 0; i < n; ++i) {
            tree[size + i] = make_block(intervals[i].first, intervals[i].second);
        }
        for (int i = size - 1; i > 0; --i) {
            tree[i] = merge_blocks(tree[2 * i], tree[2 * i + 1]);
        }
    }

    Block query(int l, int r) const {
        l += size;
        r += size;
        Block sm_l = unit_block();
        Block sm_r = unit_block();
        while (l < r) {
            if (l & 1) sm_l = merge_blocks(sm_l, tree[l++]);
            if (r & 1) sm_r = merge_blocks(tree[--r], sm_r);
            l /= 2;
            r /= 2;
        }
        return merge_blocks(sm_l, sm_r);
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<pair<long long, long long>> intervals(N);
    for (int i = 0; i < N; ++i) {
        cin >> intervals[i].first >> intervals[i].second;
    }

    IterativeSegTree st(N, intervals);

    int Q;
    if (!(cin >> Q)) return 0;

    while (Q--) {
        long long sx, sy, tx, ty;
        cin >> sx >> sy >> tx >> ty;
        if (sx > tx) {
            swap(sx, tx);
            swap(sy, ty);
        }
        Block blk = st.query(sx, tx);
        auto [out, cost] = blk.apply(sy);
        long long ans = llabs(out - ty) + cost;
        cout << ans << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
