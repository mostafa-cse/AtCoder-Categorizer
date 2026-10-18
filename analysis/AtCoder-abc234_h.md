# Problem Analysis: AtCoder-abc234_h — Ex. Enumerate Pairs

**Problem ID**: `AtCoder-abc234_h`  
**Contest**: `abc234`  
**Rating / Difficulty**: 2505  
**URL**: https://atcoder.jp/contests/abc234/tasks/abc234_h  
**VJudge Tag**: `[problem:AtCoder-abc234_h]`  
**Category File**: [`../categories/geometry/enumerate_pairs_grid_hashing_2d.md`](../categories/geometry/enumerate_pairs_grid_hashing_2d.md)  

- **Tag (Domain)**: `Geometry`  
- **Subtopic**: `Geometry 2D`  
- **Topic (Skill)**: `Points, Vectors, Transformations, Dot Products, Cross Products, Precision Issues and Polar Sort(2D)`  

---

## 1. Problem Statement & Key Idea
Enumerate all pairs of points $(i, j)$ with $i < j$ whose Euclidean distance is $\le K$. The number of such pairs is guaranteed to be $\le 4 \times 10^5$.

## 2. Core Observation & Invariant
Fixed-radius near neighbors problem in 2D. Partition the plane into square grid cells of side length $K$. Any two points within distance $K$ must reside in the same cell or in adjacent cells. Checking pairs within each cell and against 4 canonical neighboring cells checks every candidate pair exactly once without false misses.

## 3. Step-by-Step Algorithm
1. 1. Map each point $(X_i, Y_i)$ to cell coordinates $(\lfloor X_i / K \rfloor, \lfloor Y_i / K \rfloor)$ using floor division.
2. 2. Group point indices into a hash table / map keyed by cell coordinates.
3. 3. For each cell, check point pairs within the cell and against neighbor cells $(cx+1, cy)$, $(cx-1, cy+1)$, $(cx, cy+1)$, $(cx+1, cy+1)$.
4. 4. For candidates with $(X_u - X_v)^2 + (Y_u - Y_v)^2 \le K^2$, record $(u, v)$.
5. 5. Sort pairs lexicographically and output pair count followed by all pairs.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N + M \log M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    long long x, y;
    int id;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    long long k;
    if (!(cin >> n >> k)) return 0;
    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) {
        cin >> pts[i].x >> pts[i].y;
        pts[i].id = i + 1;
    }

    auto floor_div = [&](long long a, long long b) -> long long {
        long long res = a / b;
        long long rem = a % b;
        if (rem != 0 && ((a < 0) ^ (b < 0))) res--;
        return res;
    };

    map<pair<long long, long long>, vector<int>> grid;
    for (int i = 0; i < n; ++i) {
        long long cx = floor_div(pts[i].x, k);
        long long cy = floor_div(pts[i].y, k);
        grid[{cx, cy}].push_back(i);
    }

    vector<pair<int, int>> ans;
    long long k2 = k * k;

    int dx[] = {0, 1, -1, 0, 1};
    int dy[] = {0, 0, 1, 1, 1};

    for (auto &cell : grid) {
        long long cx = cell.first.first;
        long long cy = cell.first.second;
        const auto &vec1 = cell.second;

        // pairs inside same cell
        int sz = vec1.size();
        for (int i = 0; i < sz; ++i) {
            for (int j = i + 1; j < sz; ++j) {
                int u = vec1[i];
                int v = vec1[j];
                long long d = (pts[u].x - pts[v].x) * (pts[u].x - pts[v].x) + 
                              (pts[u].y - pts[v].y) * (pts[u].y - pts[v].y);
                if (d <= k2) {
                    ans.push_back({min(pts[u].id, pts[v].id), max(pts[u].id, pts[v].id)});
                }
            }
        }

        // pairs with 4 neighboring cells
        for (int dir = 1; dir < 5; ++dir) {
            pair<long long, long long> neighbor = {cx + dx[dir], cy + dy[dir]};
            auto it = grid.find(neighbor);
            if (it != grid.end()) {
                const auto &vec2 = it->second;
                for (int u : vec1) {
                    for (int v : vec2) {
                        long long d = (pts[u].x - pts[v].x) * (pts[u].x - pts[v].x) + 
                                      (pts[u].y - pts[v].y) * (pts[u].y - pts[v].y);
                        if (d <= k2) {
                            ans.push_back({min(pts[u].id, pts[v].id), max(pts[u].id, pts[v].id)});
                        }
                    }
                }
            }
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.size() << "\n";
    for (auto &p : ans) {
        cout << p.first << " " << p.second << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
