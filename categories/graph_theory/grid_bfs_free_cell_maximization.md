# Grid BFS Shortest Path / Free Cell Maximization

**Domain**: `Graph Theory`  
**Subtopic**: `Grid BFS`  

This workbook contains curated, high-quality competitive programming problems teaching **Grid BFS Shortest Path / Free Cell Maximization**.

---

## Curated Problems

### [problem:AtCoder-abc088_d] — Grid Repainting
- **Contest**: `abc088`
- **Rating / Difficulty**: 999
- **Specific Skill**: Grid BFS Shortest Path / Free Cell Maximization
- **Individual Analysis**: [`../../analysis/AtCoder-abc088_d.md`](../../analysis/AtCoder-abc088_d.md)
- **Problem Statement Summary**: An H x W grid consists of white ('.') and black ('#') cells. You start at (1, 1) and want to reach (H, W) moving 4-directionally through white cells. You can repaint some white cells to black, provided a valid path still exists. Maximize the number of cells repainted.
- **Core Insight**: Let total_white be the total count of '.' cells. Let dist be the minimum steps in shortest path from (1, 1) to (H, W) (1-indexed length, so dist + 1 cells are visited). If goal is unreachable, output -1. Otherwise, answer is total_white - (dist + 1).
- **Complexity**: Time: `O(H * W)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    int white_count = 0;
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
        for (char c : grid[i]) {
            if (c == '.') white_count++;
        }
    }

    vector<vector<int>> dist(h, vector<int>(w, -1));
    queue<pair<int, int>> q;

    dist[0][0] = 0;
    q.push({0, 0});

    int dr[] = {1, -1, 0, 0};
    int dc[] = {0, 0, 1, -1};

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        for (int d = 0; d < 4; ++d) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] == '.' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }
    }

    if (dist[h - 1][w - 1] == -1) {
        cout << -1 << "\n";
    } else {
        cout << white_count - (dist[h - 1][w - 1] + 1) << "\n";
    }

    return 0;
}
```
