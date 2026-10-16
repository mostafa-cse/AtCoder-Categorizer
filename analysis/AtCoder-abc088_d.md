# Problem Analysis: AtCoder-abc088_d — Grid Repainting

**Problem ID**: `AtCoder-abc088_d`  
**Contest**: `abc088`  
**Rating / Difficulty**: 999  
**URL**: https://atcoder.jp/contests/abc088/tasks/abc088_d  
**VJudge Tag**: `[problem:AtCoder-abc088_d]`  
**Category File**: [`../categories/graph_theory/grid_bfs_free_cell_maximization.md`](../categories/graph_theory/grid_bfs_free_cell_maximization.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Grid BFS`  
- **Topic (Skill)**: `Grid BFS Shortest Path / Free Cell Maximization`  

---

## 1. Problem Statement & Key Idea
An H x W grid consists of white ('.') and black ('#') cells. You start at (1, 1) and want to reach (H, W) moving 4-directionally through white cells. You can repaint some white cells to black, provided a valid path still exists. Maximize the number of cells repainted.

**Key Idea**: To maximize repainted white cells, we must keep the minimum number of white cells that still connect (1, 1) to (H, W). This corresponds to the shortest path from start to finish.

## 2. Core Observation & Invariant
Let total_white be the total count of '.' cells. Let dist be the minimum steps in shortest path from (1, 1) to (H, W) (1-indexed length, so dist + 1 cells are visited). If goal is unreachable, output -1. Otherwise, answer is total_white - (dist + 1).

## 3. Step-by-Step Algorithm
1. Count total white cells in the grid.
2. Run 2D BFS from (0, 0) to compute dist[r][c] to all cells.
3. If dist[H-1][W-1] == -1, print -1.
4. Else, print total_white - (dist[H-1][W-1] + 1).

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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Translating resource maximization to shortest path complement.
- **Reusable Pattern**: `Max cells to delete while preserving connectivity = total_cells - shortest_path_length.`
