# Problem Analysis: AtCoder-abc170_f — Pond Skater

**Problem ID**: `AtCoder-abc170_f`  
**Contest**: `abc170`  
**Rating / Difficulty**: 1968  
**URL**: https://atcoder.jp/contests/abc170/tasks/abc170_f  
**VJudge Tag**: `[problem:AtCoder-abc170_f]`  
**Category File**: [`../categories/graph_theory/bounded_ray_shooting_grid_bfs.md`](../categories/graph_theory/bounded_ray_shooting_grid_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Grid BFS`  
- **Topic (Skill)**: `Bounded Ray-Shooting Grid BFS with Early Pruning on Directional Steps`  

---

## 1. Problem Statement & Key Idea
An H x W grid (H * W <= 10^6). A skater can travel up to K squares in one cardinal direction per move without crossing obstacles. Find minimum moves from (x_1, y_1) to (x_2, y_2), or -1.

Standard BFS explores neighbor cells. Traveling up to K squares introduces up to K steps per direction. To maintain linear complexity O(H * W), when extending in direction (dr, dc) up to K steps: if a cell (nr, nc) has dist[nr][nc] < dist[r][c] + 1, we can pass through it (since future cells along this ray may not have been reached yet), but if dist[nr][nc] <= dist[r][c], an earlier/shorter wave has already explored this ray further, so we can immediately break!

## 2. Core Observation & Invariant
Breaking ray expansion when encountering a cell reached with <= current distance guarantees each cell is visited at most a constant number of times.

## 3. Step-by-Step Algorithm
1. Initialize dist[H][W] with INF.
2. Set dist[x_1][y_1] = 0 and push to queue.
3. While queue is not empty:
4.   pop (r, c).
5.   For each of the 4 cardinal directions:
6.     For step s = 1 to K:
7.       nr = r + dr * s, nc = c + dc * s.
8.       If out of bounds or obstacle, break.
9.       If dist[nr][nc] <= dist[r][c], break.
10.       If dist[nr][nc] == INF: dist[nr][nc] = dist[r][c] + 1, push (nr, nc).
11. Print dist[x_2][y_2] if < INF, else -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

const int INF = 1e9 + 7;
const int dr[] = {-1, 1, 0, 0};
const int dc[] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, k;
    if (!(cin >> h >> w >> k)) return 0;

    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    --x1; --y1; --x2; --y2;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    vector<vector<int>> dist(h, vector<int>(w, INF));
    queue<pair<int, int>> q;

    dist[x1][y1] = 0;
    q.push({x1, y1});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == x2 && c == y2) {
            cout << dist[r][c] << "\n";
            return 0;
        }

        int d = dist[r][c];

        for (int dir = 0; dir < 4; ++dir) {
            for (int s = 1; s <= k; ++s) {
                int nr = r + dr[dir] * s;
                int nc = c + dc[dir] * s;

                if (nr < 0 || nr >= h || nc < 0 || nc >= w || grid[nr][nc] == '@') {
                    break;
                }
                if (dist[nr][nc] <= d) {
                    break;
                }
                if (dist[nr][nc] == INF) {
                    dist[nr][nc] = d + 1;
                    q.push({nr, nc});
                }
            }
        }
    }

    cout << (dist[x2][y2] >= INF ? -1 : dist[x2][y2]) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Optimizing ray-shooting grid BFS via directional early-pruning conditions.
- **Reusable Pattern**: `Ray-Shooting BFS: Break ray expansion when dist[next] <= dist[cur] to guarantee O(V + E) bounds.`
