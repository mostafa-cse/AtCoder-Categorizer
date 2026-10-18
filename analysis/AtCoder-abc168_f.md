# Problem Analysis: AtCoder-abc168_f — F. . Single Dot

**Problem ID**: `AtCoder-abc168_f`  
**Contest**: `abc168`  
**Rating / Difficulty**: 2478  
**URL**: https://atcoder.jp/contests/abc168/tasks/abc168_f  
**VJudge Tag**: `[problem:AtCoder-abc168_f]`  
**Category File**: [`../categories/miscellaneous/single_dot_grid_coordinate_compression_bfs.md`](../categories/miscellaneous/single_dot_grid_coordinate_compression_bfs.md)  

- **Tag (Domain)**: `Miscellaneous`  
- **Subtopic**: `Techniques`  
- **Topic (Skill)**: `Coordinate Compression`  

---

## 1. Problem Statement & Key Idea
Compute the reachable area of a cow starting at $(0, 0)$ bounded by $N$ vertical and $M$ horizontal segments. Perform 2D coordinate compression on all segment endpoints and 0, forming an $O(N + M) \times O(N + M)$ grid of rectangular faces. Mark wall boundaries between adjacent cells and run BFS from $(0, 0)$. If the search escapes the outer bounding box, output 'INF'; otherwise, sum the exact rectangular areas.

## 2. Core Observation & Invariant
Because (0, 0) does not lie on any segment, the cow can enter all 4 adjacent open quadrants around the origin. Adjacent compressed faces share open boundaries unless blocked by a segment spanning that coordinate interval. Unbounded components reach the outer coordinate boundary.

## 3. Step-by-Step Algorithm
1. 1. Collect all $x$-coordinates (endpoints + 0) and $y$-coordinates (endpoints + 0), sort and remove duplicates.
2. 2. Construct 2D grid of cells $(i, j)$ spanning $[X_i, X_{i+1}] \times [Y_j, Y_{j+1}]$.
3. 3. Mark vertical wall segments: for segment at $y = Y_c$ covering $[A, B]$, block crossing between $(r, c-1)$ and $(r, c)$ for $r \in [idx(A), idx(B))$.
4. 4. Mark horizontal wall segments: for segment at $x = X_r$ covering $[E, F]$, block crossing between $(r-1, c)$ and $(r, c)$ for $c \in [idx(E), idx(F))$.
5. 5. Queue the cells surrounding $(0, 0)$ and run BFS flood-fill.
6. 6. If BFS visits any boundary cell $(r=0, r=H-2, c=0, c=W-2)$ attempting to cross outward, output 'INF'.
7. 7. Otherwise, output the sum of $(X_{r+1} - X_r) \times (Y_{c+1} - Y_c)$ over all visited cells.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M)^2)`
- **Space Complexity**: `O((N + M)^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Segment {
    long long a, b, c;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    vector<Segment> ns(N);
    vector<long long> xs = {0}, ys = {0};
    for (int i = 0; i < N; ++i) {
        cin >> ns[i].a >> ns[i].b >> ns[i].c;
        xs.push_back(ns[i].a);
        xs.push_back(ns[i].b);
        ys.push_back(ns[i].c);
    }

    vector<Segment> ew(M);
    for (int j = 0; j < M; ++j) {
        cin >> ew[j].a >> ew[j].b >> ew[j].c; // D, E, F
        xs.push_back(ew[j].a);
        ys.push_back(ew[j].b);
        ys.push_back(ew[j].c);
    }

    sort(xs.begin(), xs.end());
    xs.erase(unique(xs.begin(), xs.end()), xs.end());
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());

    int H = xs.size();
    int W = ys.size();

    auto get_x = [&](long long val) {
        return lower_bound(xs.begin(), xs.end(), val) - xs.begin();
    };
    auto get_y = [&](long long val) {
        return lower_bound(ys.begin(), ys.end(), val) - ys.begin();
    };

    // wall_v[r][c] blocks crossing between (r, c-1) and (r, c) at y = Y[c]
    vector<vector<bool>> wall_v(H - 1, vector<bool>(W, false));
    for (int i = 0; i < N; ++i) {
        int idx_c = get_y(ns[i].c);
        int idx_a = get_x(ns[i].a);
        int idx_b = get_x(ns[i].b);
        for (int r = idx_a; r < idx_b; ++r) {
            wall_v[r][idx_c] = true;
        }
    }

    // wall_h[r][c] blocks crossing between (r-1, c) and (r, c) at x = X[r]
    vector<vector<bool>> wall_h(H, vector<bool>(W - 1, false));
    for (int j = 0; j < M; ++j) {
        int idx_d = get_x(ew[j].a);
        int idx_e = get_y(ew[j].b);
        int idx_f = get_y(ew[j].c);
        for (int c = idx_e; c < idx_f; ++c) {
            wall_h[idx_d][c] = true;
        }
    }

    vector<vector<bool>> visited(H - 1, vector<bool>(W - 1, false));
    queue<pair<int, int>> q;

    int idx0 = get_x(0);
    int idy0 = get_y(0);

    if (idx0 > 0 && idy0 > 0) {
        visited[idx0 - 1][idy0 - 1] = true;
        q.push({idx0 - 1, idy0 - 1});
    }
    if (idx0 > 0 && idy0 < W - 1) {
        visited[idx0 - 1][idy0] = true;
        q.push({idx0 - 1, idy0});
    }
    if (idx0 < H - 1 && idy0 > 0) {
        visited[idx0][idy0 - 1] = true;
        q.push({idx0, idy0 - 1});
    }
    if (idx0 < H - 1 && idy0 < W - 1) {
        visited[idx0][idy0] = true;
        q.push({idx0, idy0});
    }

    bool is_inf = false;
    long long area = 0;

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        area += (xs[r + 1] - xs[r]) * (ys[c + 1] - ys[c]);

        // Move up
        if (r == 0) {
            is_inf = true;
        } else if (!wall_h[r][c] && !visited[r - 1][c]) {
            visited[r - 1][c] = true;
            q.push({r - 1, c});
        }

        // Move down
        if (r == H - 2) {
            is_inf = true;
        } else if (!wall_h[r + 1][c] && !visited[r + 1][c]) {
            visited[r + 1][c] = true;
            q.push({r + 1, c});
        }

        // Move left
        if (c == 0) {
            is_inf = true;
        } else if (!wall_v[r][c] && !visited[r][c - 1]) {
            visited[r][c - 1] = true;
            q.push({r, c - 1});
        }

        // Move right
        if (c == W - 2) {
            is_inf = true;
        } else if (!wall_v[r][c + 1] && !visited[r][c + 1]) {
            visited[r][c + 1] = true;
            q.push({r, c + 1});
        }
    }

    if (is_inf) {
        cout << "INF\n";
    } else {
        cout << area << "\n";
    }
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
