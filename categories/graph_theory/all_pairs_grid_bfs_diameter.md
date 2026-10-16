# All-Pairs Grid BFS / Grid Maze Diameter

**Domain**: `Graph Theory`  
**Subtopic**: `Grid BFS`  

This workbook contains curated, high-quality competitive programming problems teaching **All-Pairs Grid BFS / Grid Maze Diameter**.

---

## Curated Problems

### [problem:AtCoder-abc151_d] — Maze Master
- **Contest**: `abc151`
- **Rating / Difficulty**: 959
- **Specific Skill**: All-Pairs Grid BFS / Grid Maze Diameter
- **Individual Analysis**: [`../../analysis/AtCoder-abc151_d.md`](../../analysis/AtCoder-abc151_d.md)
- **Problem Statement Summary**: Given an H x W maze of '.' and '#' (H, W <= 20). Pick start cell S and goal cell G (both '.') to maximize the shortest path distance between them. Find this maximum shortest path distance.
- **Core Insight**: Since H, W <= 20, the number of road cells V <= 400. Running a BFS from every road cell takes O(V * (V + E)) = O((H*W)^2) <= 1.6 * 10^5 operations, easily running within milliseconds.
- **Complexity**: Time: `O((H * W)^2)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
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
