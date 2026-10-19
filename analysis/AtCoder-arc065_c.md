# Problem Analysis: AtCoder-arc065_c — E - Manhattan Compass

**Problem ID**: `AtCoder-arc065_c`  
**Contest**: `arc065`  
**Rating / Difficulty**: 2835  
**URL**: https://atcoder.jp/contests/arc065/tasks/arc065_c  
**VJudge Tag**: `[problem:AtCoder-arc065_c]`  
**Category File**: [`../categories/geometry/manhattan_chebyshev_rotation_connected_pairs_bfs.md`](../categories/geometry/manhattan_chebyshev_rotation_connected_pairs_bfs.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Sweep Line`  
- **Topic (Skill)**: `Sweep Line Algorithm and Radial Sweep`  

---

## 1. Problem Statement & Key Idea
N points on the plane. A Manhattan compass points to a pair of points with fixed distance D = d(a, b). Compass can move from (p, q) to (p, r) if d(p, r) == d(p, q) == D. Find the number of reachable pairs.

## 2. Core Observation & Invariant
Rotate coordinates 45 degrees: (X, Y) = (x + y, x - y), so Manhattan distance becomes Chebyshev distance max(|X_1 - X_2|, |Y_1 - Y_2|) = D. Vertices reachable by the compass are exactly the connected component of {a, b} in the distance-D graph. To run BFS in O(N log N) time, store unvisited points in balanced BSTs ordered by X and Y; deleting visited points ensures each vertex is visited once. Counting distance-D pairs in the component uses binary search on 1D slices.

## 3. Step-by-Step Algorithm
1. 1. Rotate points (x, y) -> (x+y, x-y) and compute target distance D = max(|Xa - Xb|, |Ya - Yb|).
2. 2. Insert all points into two std::map<ll, set<pair<ll, int>>> indexed by X and Y.
3. 3. Run BFS from a and b: for point (xu, yu), query lines X = xu +- D for Y in [yu - D, yu + D] and lines Y = yu +- D for X in [xu - D, xu + D], queuing and erasing visited points.
4. 4. Group component points into sorted vectors by X and by Y.
5. 5. For each point in the component, count pairs with X' = X + D and Y' in [Y - D, Y + D], plus pairs with Y' = Y + D and X' in [X - D + 1, X + D - 1] to avoid corner double-counting.
6. 6. Output total pair count.

## 4. Complexity Analysis
- **Time Complexity**: `O(N log N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

typedef long long ll;

struct Point {
    ll x, y;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, a_idx, b_idx;
    if (!(cin >> n >> a_idx >> b_idx)) return 0;
    --a_idx; --b_idx;

    vector<Point> orig(n);
    vector<Point> rot(n);
    for (int i = 0; i < n; ++i) {
        cin >> orig[i].x >> orig[i].y;
        rot[i].x = orig[i].x + orig[i].y;
        rot[i].y = orig[i].x - orig[i].y;
    }

    ll D = max(abs(rot[a_idx].x - rot[b_idx].x), abs(rot[a_idx].y - rot[b_idx].y));

    map<ll, set<pair<ll, int>>> by_X, by_Y;
    for (int i = 0; i < n; ++i) {
        by_X[rot[i].x].insert({rot[i].y, i});
        by_Y[rot[i].y].insert({rot[i].x, i});
    }

    auto remove_pt = [&](int idx) {
        ll x = rot[idx].x;
        ll y = rot[idx].y;
        by_X[x].erase({y, idx});
        by_Y[y].erase({x, idx});
    };

    vector<bool> visited(n, false);
    queue<int> q;

    q.push(a_idx);
    visited[a_idx] = true;
    remove_pt(a_idx);

    q.push(b_idx);
    visited[b_idx] = true;
    remove_pt(b_idx);

    vector<int> component;
    component.push_back(a_idx);
    component.push_back(b_idx);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        ll xu = rot[u].x;
        ll yu = rot[u].y;

        // Check line X = xu + D and X = xu - D
        ll target_X[2] = {xu + D, xu - D};
        for (ll tx : target_X) {
            auto map_it = by_X.find(tx);
            if (map_it == by_X.end()) continue;
            auto& s = map_it->second;
            auto it = s.lower_bound({yu - D, -1});
            vector<int> found;
            while (it != s.end() && it->first <= yu + D) {
                found.push_back(it->second);
                it++;
            }
            for (int idx : found) {
                if (!visited[idx]) {
                    visited[idx] = true;
                    q.push(idx);
                    component.push_back(idx);
                    remove_pt(idx);
                }
            }
        }

        // Check line Y = yu + D and Y = yu - D
        ll target_Y[2] = {yu + D, yu - D};
        for (ll ty : target_Y) {
            auto map_it = by_Y.find(ty);
            if (map_it == by_Y.end()) continue;
            auto& s = map_it->second;
            auto it = s.lower_bound({xu - D, -1});
            vector<int> found;
            while (it != s.end() && it->first <= xu + D) {
                found.push_back(it->second);
                it++;
            }
            for (int idx : found) {
                if (!visited[idx]) {
                    visited[idx] = true;
                    q.push(idx);
                    component.push_back(idx);
                    remove_pt(idx);
                }
            }
        }
    }

    map<ll, vector<ll>> comp_by_X, comp_by_Y;
    for (int u : component) {
        comp_by_X[rot[u].x].push_back(rot[u].y);
        comp_by_Y[rot[u].y].push_back(rot[u].x);
    }
    for (auto& [k, vec] : comp_by_X) sort(vec.begin(), vec.end());
    for (auto& [k, vec] : comp_by_Y) sort(vec.begin(), vec.end());

    ll ans = 0;
    for (int u : component) {
        ll X = rot[u].x;
        ll Y = rot[u].y;

        // On line X + D: Y' in [Y - D, Y + D]
        auto itX = comp_by_X.find(X + D);
        if (itX != comp_by_X.end()) {
            const auto& vec = itX->second;
            auto low = lower_bound(vec.begin(), vec.end(), Y - D);
            auto high = upper_bound(vec.begin(), vec.end(), Y + D);
            ans += (high - low);
        }

        // On line Y + D: X' in [X - D + 1, X + D - 1]
        auto itY = comp_by_Y.find(Y + D);
        if (itY != comp_by_Y.end()) {
            const auto& vec = itY->second;
            auto low = lower_bound(vec.begin(), vec.end(), X - D + 1);
            auto high = upper_bound(vec.begin(), vec.end(), X + D - 1);
            ans += (high - low);
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
