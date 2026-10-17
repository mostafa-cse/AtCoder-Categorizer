# Problem Analysis: AtCoder-abc353_f — Tile Distance

**Problem ID**: `AtCoder-abc353_f`  
**Contest**: `abc353`  
**Rating / Difficulty**: 2201  
**URL**: https://atcoder.jp/contests/abc353/tasks/abc353_f  
**VJudge Tag**: `[problem:AtCoder-abc353_f]`  
**Category File**: [`../categories/miscellaneous/tile_distance_chebyshev_step_metric.md`](../categories/miscellaneous/tile_distance_chebyshev_step_metric.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Manhattan <> Chebyshev`  

---

## 1. Problem Statement & Key Idea
Multi-scale grid distance reduction between 1x1 small tiles and KxK large tiles via Chebyshev diagonal metric with axis-aligned step cost.

## 2. Core Observation & Invariant
A grid point (x, y) belongs to a KxK block ((x/K), (y/K)). Blocks with odd coordinate sum are large tiles, and those with even coordinate sum are sets of K^2 1x1 tiles. Inside large tiles, motion is free along any direction. When stepping between adjacent large tiles (which meet at small tile borders), diagonal steps cost 2 and axis-aligned steps of 2 blocks cost min(4, K+1).

## 3. Step-by-Step Algorithm
1. 1. If K == 1, answer is Manhattan distance |sx - tx| + |sy - ty|.
2. 2. If start/target is in a small tile block, generate at most 4 boundary entry/exit points to adjacent large tile blocks with their Manhattan entry costs.
3. 3. For each pair of (start, target) large tile blocks (bx1, by1) and (bx2, by2), their coordinate differences dx = |bx1 - bx2| and dy = |by1 - by2| satisfy dx + dy is even. Decompose into min(dx, dy) diagonal moves (cost 2 each) and remaining |dx - dy| / 2 axis moves (cost min(4, K+1) each).
4. 4. Take the minimum over all candidate pairs and the direct Manhattan path.

## 4. Complexity Analysis
- **Time Complexity**: `O(1)`
- **Space Complexity**: `O(1)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// abc353_f: Tile Distance
// Grid has 1x1 tiles and KxK large tiles.
// An entry/exit to a large tile (X, Y) is at (X*K, Y*K), etc.
// For K = 1, simple Manhattan distance |sx - tx| + |sy - ty|.
// For K = 2, cost to step between large tiles vs walking on 1x1.

bool is_large(ll x, ll y, ll K) {
    ll bx = x / K, by = y / K;
    return (bx + by) % 2 != 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll K;
    if (!(cin >> K)) return 0;
    ll sx, sy, tx, ty;
    cin >> sx >> sy >> tx >> ty;

    ll ans = llabs(sx - tx) + llabs(sy - ty);
    if (K == 1) {
        cout << ans << "\n";
        return 0;
    }

    // Candidates for start: if in small tile, step to adjacent large tiles.
    // There are at most 4 adjacent large tile boundaries.
    struct Point {
        ll bx, by; // block coords of large tile
        ll cost;   // cost to reach this large tile block
    };

    auto get_candidates = [&](ll x, ll y) -> vector<Point> {
        vector<Point> res;
        ll bx = x / K, by = y / K;
        if ((bx + by) % 2 != 0) {
            // Already in a large tile!
            res.push_back({bx, by, 0});
        } else {
            // In a small tile block (bx, by).
            // Cost to reach the 4 adjacent large tile blocks:
            // Left: x reaches bx*K - 1, which is in (bx - 1, by)
            ll d_left = x - bx * K + 1;
            res.push_back({bx - 1, by, d_left});
            // Right: x reaches (bx + 1)*K, which is in (bx + 1, by)
            ll d_right = (bx + 1) * K - x;
            res.push_back({bx + 1, by, d_right});
            // Down: y reaches by*K - 1
            ll d_down = y - by * K + 1;
            res.push_back({bx, by - 1, d_down});
            // Up: y reaches (by + 1)*K
            ll d_up = (by + 1) * K - y;
            res.push_back({bx, by + 1, d_up});
        }
        return res;
    };

    auto starts = get_candidates(sx, sy);
    auto targets = get_candidates(tx, ty);

    // Distance between large tile (bx1, by1) and (bx2, by2):
    // In Chebyshev / diagonal moves:
    // Moving diagonally between adjacent large tiles takes 2 steps (through a corner or 1x1 tile).
    // Moving along axis takes 2 steps to next large tile (1 step inside small, 1 step into large).
    // Wait, between large tiles, each step costs 2.
    // If K >= 2: moving diagonally takes 2 cost.
    // Moving straight (diff of 2 in bx, 0 in by) takes min(2*K, 4) or (K+1)?
    // Between (bx1, by1) and (bx2, by2) where both are large tiles (odd sum):
    // |bx1 - bx2| + |by1 - by2| is even!
    // Let dx = |bx1 - bx2|, dy = |by1 - by2|.
    // We can decompose into min(dx, dy) diagonal moves (each dx-1, dy-1, cost 2),
    // and remaining |dx - dy| steps along an axis.
    // Along an axis, a move of 2 blocks costs min(2 * (K + 1) / 2?, min(4, K + 1))?
    // In large tile, can traverse inside for free! Crossing the small tile of length 1 costs 1,
    // plus entering the next large tile costs 1. So crossing one small tile costs 2.
    // If K == 2: crossing small tile costs 2, crossing inside small tile costs K. min(4, K+1) = min(4, 3) for K=2 is 3?
    // Wait: for K, cost of move of 2 in one direction:
    // Either walk across small tile in 1D: cost K+1 (entering and walking across 1x1).
    // Or zig-zag diagonally: (1, 1) and (1, -1) costs 2 + 2 = 4!
    // So cost is min(4LL, K + 1) for each difference of 2!
    for (auto& s : starts) {
        for (auto& t : targets) {
            ll dx = llabs(s.bx - t.bx);
            ll dy = llabs(s.by - t.by);
            // dx + dy is even
            ll diag = min(dx, dy);
            ll rem = (max(dx, dy) - diag) / 2;
            ll large_dist = diag * 2 + rem * min(4LL, K + 1);
            ans = min(ans, s.cost + t.cost + large_dist);
        }
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
