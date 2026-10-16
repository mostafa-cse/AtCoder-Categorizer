# Grid BFS with Teleporter Equivalence Class Clearance

**Domain**: `Graph Theory`  
**Subtopic**: `Breadth-First Search (BFS)`  

This workbook contains curated, high-quality competitive programming problems teaching **Grid BFS with Teleporter Equivalence Class Clearance**.

---

## Curated Problems

### `[problem:AtCoder-abc184_e]` — Third Avenue
- **Rating / Difficulty**: 1418
- **Contest**: `abc184`
- **Analysis**: [`analysis/AtCoder-abc184_e.md`](../../analysis/AtCoder-abc184_e.md)
- **Key Idea**: Standard BFS on the grid. To prevent quadratic TLE from teleporter edges, when teleporters of type 'c' are used for the first time, enqueue all cells of type 'c' and CLEAR the list for 'c'.
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

const int dr[4] = {-1, 1, 0, 0};
const int dc[4] = {0, 0, -1, 1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    int sr = -1, sc = -1, gr = -1, gc = -1;
    vector<pair<int, int>> teleporters[26];

    for (int r = 0; r < h; ++r) {
        cin >> grid[r];
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == 'S') {
                sr = r; sc = c;
            } else if (grid[r][c] == 'G') {
                gr = r; gc = c;
            } else if (grid[r][c] >= 'a' && grid[r][c] <= 'z') {
                teleporters[grid[r][c] - 'a'].push_back({r, c});
            }
        }
    }

    vector<vector<int>> dist(h, vector<int>(w, -1));
    vector<bool> tele_used(26, false);
    queue<pair<int, int>> q;

    dist[sr][sc] = 0;
    q.push({sr, sc});

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == gr && c == gc) {
            cout << dist[r][c] << "\n";
            return 0;
        }

        // 4-directional moves
        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] != '#' && dist[nr][nc] == -1) {
                dist[nr][nc] = dist[r][c] + 1;
                q.push({nr, nc});
            }
        }

        // Teleporter warp
        if (grid[r][c] >= 'a' && grid[r][c] <= 'z') {
            int idx = grid[r][c] - 'a';
            if (!tele_used[idx]) {
                tele_used[idx] = true;
                for (const auto& p : teleporters[idx]) {
                    if (dist[p.first][p.second] == -1) {
                        dist[p.first][p.second] = dist[r][c] + 1;
                        q.push(p);
                    }
                }
                teleporters[idx].clear();
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}
```
