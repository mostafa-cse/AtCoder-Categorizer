# Problem Analysis: AtCoder-abc176_d — Wizard in Maze

**Problem ID**: `AtCoder-abc176_d`  
**Contest**: `abc176`  
**Rating / Difficulty**: 1248  
**URL**: https://atcoder.jp/contests/abc176/tasks/abc176_d  
**VJudge Tag**: `[problem:AtCoder-abc176_d]`  
**Category File**: [`../categories/graph_theory/zero_one_bfs_warp_moves.md`](../categories/graph_theory/zero_one_bfs_warp_moves.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `0-1 BFS`  
- **Topic (Skill)**: `0-1 BFS on 5x5 Warp Moves`  

---

## 1. Problem Statement & Key Idea
An H x W maze of '.' and '#'. Move A: walk to an adjacent '.' cell (cost 0). Move B: magic warp to any '.' cell within a 5x5 area centered at current cell (cost 1). Find minimum magic warps to reach target.

**Key Idea**: The graph has only edge weights 0 and 1, which is solved optimally via 0-1 BFS using std::deque.

## 2. Core Observation & Invariant
From cell (r, c): 4-directional moves cost 0 (push to front of deque); 5x5 box moves (within dx, dy in [-2, 2]) cost 1 (push to back of deque). Because cost 0 moves are prioritized at the front, dist array maintains optimal distance.

## 3. Step-by-Step Algorithm
1. Initialize dist matrix of size H x W to INF; dist[sr][sc] = 0.
2. Initialize deque<pair<int, int>> dq; dq.push_front({sr, sc}).
3. While dq is not empty: pop (r, c).
4. 4-directional moves: if nr, nc is '.' and dist[r][c] < dist[nr][nc]: dist[nr][nc] = dist[r][c], dq.push_front({nr, nc}).
5. 5x5 warp moves: for dr in [-2, 2], dc in [-2, 2]: if '.' and dist[r][c] + 1 < dist[nr][nc]: dist[nr][nc] = dist[r][c] + 1, dq.push_back({nr, nc}).
6. Print dist[target] (or -1 if unreachable).

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W * 25)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <deque>

using namespace std;

const int INF = 1e9;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, ch, cw, dh, dw;
    if (!(cin >> h >> w >> ch >> cw >> dh >> dw)) return 0;
    ch--; cw--; dh--; dw--; // 0-indexed

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    vector<vector<int>> dist(h, vector<int>(w, INF));
    deque<pair<int, int>> dq;

    dist[ch][cw] = 0;
    dq.push_front({ch, cw});

    int dr4[] = {1, -1, 0, 0};
    int dc4[] = {0, 0, 1, -1};

    while (!dq.empty()) {
        auto [r, c] = dq.front();
        dq.pop_front();

        if (r == dh && c == dw) break;

        // Move A: walk (cost 0)
        for (int d = 0; d < 4; ++d) {
            int nr = r + dr4[d];
            int nc = c + dc4[d];
            if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] == '.') {
                if (dist[r][c] < dist[nr][nc]) {
                    dist[nr][nc] = dist[r][c];
                    dq.push_front({nr, nc});
                }
            }
        }

        // Move B: warp (cost 1)
        for (int dr = -2; dr <= 2; ++dr) {
            for (int dc = -2; dc <= 2; ++dc) {
                int nr = r + dr;
                int nc = c + dc;
                if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] == '.') {
                    if (dist[r][c] + 1 < dist[nr][nc]) {
                        dist[nr][nc] = dist[r][c] + 1;
                        dq.push_back({nr, nc});
                    }
                }
            }
        }
    }

    cout << (dist[dh][dw] == INF ? -1 : dist[dh][dw]) << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 0-1 BFS graph traversal on hybrid local/warp grid move systems.
- **Reusable Pattern**: `0-1 BFS: cost 0 -> push_front, cost 1 -> push_back.`
