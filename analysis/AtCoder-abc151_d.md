# Problem Analysis: AtCoder-abc151_d — Maze Master

**Problem ID**: `AtCoder-abc151_d`  
**Contest**: `abc151`  
**Rating / Difficulty**: 959  
**URL**: https://atcoder.jp/contests/abc151/tasks/abc151_d  
**VJudge Tag**: `[problem:AtCoder-abc151_d]`  
**Category File**: [`../categories/graph_theory/all_pairs_grid_bfs_diameter.md`](../categories/graph_theory/all_pairs_grid_bfs_diameter.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Grid BFS`  
- **Topic (Skill)**: `All-Pairs Grid BFS / Grid Maze Diameter`  

---

## 1. Problem Statement & Key Idea
Given an H x W maze of '.' and '#' (H, W <= 20). Pick start cell S and goal cell G (both '.') to maximize the shortest path distance between them. Find this maximum shortest path distance.

**Key Idea**: The problem asks for the diameter of the unweighted grid graph.

## 2. Core Observation & Invariant
Since H, W <= 20, the number of road cells V <= 400. Running a BFS from every road cell takes O(V * (V + E)) = O((H*W)^2) <= 1.6 * 10^5 operations, easily running within milliseconds.

## 3. Step-by-Step Algorithm
1. For every cell (r, c) with grid[r][c] == '.':
2. Run 2D BFS: compute dist array initialized to -1, push (r, c) to queue with dist[r][c] = 0.
3. Explore 4 neighbors: if within bounds, '.' and unvisited, update dist and push to queue.
4. Track the maximum distance reached across all BFS executions.
5. Print the global maximum.

## 4. Complexity Analysis
- **Time Complexity**: `O((H * W)^2)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    int max_dist = 0;
    int dr[] = {1, -1, 0, 0};
    int dc[] = {0, 0, 1, -1};

    for (int sr = 0; sr < h; ++sr) {
        for (int sc = 0; sc < w; ++sc) {
            if (grid[sr][sc] == '#') continue;

            vector<vector<int>> dist(h, vector<int>(w, -1));
            queue<pair<int, int>> q;

            dist[sr][sc] = 0;
            q.push({sr, sc});

            while (!q.empty()) {
                auto [r, c] = q.front();
                q.pop();

                max_dist = max(max_dist, dist[r][c]);

                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] == '.' && dist[nr][nc] == -1) {
                        dist[nr][nc] = dist[r][c] + 1;
                        q.push({nr, nc});
                    }
                }
            }
        }
    }

    cout << max_dist << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: All-pairs shortest path diameter on small grids via repeated BFS.
- **Reusable Pattern**: `Run BFS from every '.' node to find maximum shortest path.`
