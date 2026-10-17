# Bounded Ray-Shooting Grid BFS with Early Pruning on Directional Steps

**Domain**: `Graph Theory`  
**Subtopic**: `Grid BFS`  

This workbook contains curated, high-quality competitive programming problems teaching **Bounded Ray-Shooting Grid BFS with Early Pruning on Directional Steps**.

---

## Curated Problems

### `[problem:AtCoder-abc170_f]` — Pond Skater
- **Rating / Difficulty**: 1968
- **Contest**: `abc170`
- **Analysis**: [`analysis/AtCoder-abc170_f.md`](../../analysis/AtCoder-abc170_f.md)
- **Key Idea**: Standard BFS explores neighbor cells. Traveling up to K squares introduces up to K steps per direction. To maintain linear complexity O(H * W), when extending in direction (dr, dc) up to K steps: if a cell (nr, nc) has dist[nr][nc] < dist[r][c] + 1, we can pass through it (since future cells along this ray may not have been reached yet), but if dist[nr][nc] <= dist[r][c], an earlier/shorter wave has already explored this ray further, so we can immediately break!
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`
- **Verified C++ Implementation**:
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
