# Problem Analysis: AtCoder-abc184_e — Third Avenue

**Problem ID**: `AtCoder-abc184_e`  
**Contest**: `abc184`  
**Rating / Difficulty**: 1418  
**URL**: https://atcoder.jp/contests/abc184/tasks/abc184_e  
**VJudge Tag**: `[problem:AtCoder-abc184_e]`  
**Category File**: [`../categories/graph_theory/grid_bfs_teleporter_equivalence.md`](../categories/graph_theory/grid_bfs_teleporter_equivalence.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Breadth-First Search (BFS)`  
- **Topic (Skill)**: `Grid BFS with Teleporter Equivalence Class Clearance`  

---

## 1. Problem Statement & Key Idea
An H x W grid contains '.', '#', start 'S', goal 'G', and teleporters labeled 'a' through 'z'. Stepping to an adjacent cell takes 1 second. Stepping from a teleporter cell 'c' to any other teleporter cell of the same letter 'c' takes 1 second. Find the minimum time to reach 'G' from 'S', or -1 if unreachable.

**Key Insight**: Standard BFS on the grid. To prevent quadratic TLE from teleporter edges, when teleporters of type 'c' are used for the first time, enqueue all cells of type 'c' and CLEAR the list for 'c'.

## 2. Core Observation & Invariant
Without clearing, a grid with many teleporters of the same letter could trigger O(T^2) transitions. Clearing the list for letter 'c' once it is explored guarantees each teleporter node is inspected O(1) times, keeping the BFS linear O(H * W).

## 3. Step-by-Step Algorithm
1. Store teleporter cell coordinates grouped by letter 'a'..'z'.
2. Maintain dist[H][W] initialized to -1, and used_teleport[26] = false.
3. Queue start 'S' with dist = 0.
4. While queue is not empty, pop (r, c):
5.   If (r, c) == 'G', return dist[r][c].
6.   For each of 4 cardinal neighbors (nr, nc):
7.     If valid, not '#', and dist[nr][nc] == -1: set dist = dist[r][c] + 1 and enqueue.
8.   If grid[r][c] is 'a'..'z' and !used_teleport[char - 'a']:
9.     used_teleport[char - 'a'] = true.
10.     For each teleporter (tr, tc) of that letter:
11.       If dist[tr][tc] == -1: set dist = dist[r][c] + 1 and enqueue.
12.     Clear teleporter list for that letter.
13. If 'G' is not reached, return -1.

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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: BFS state expansion with equivalence-class clearing to avoid dense multi-edge overhead.
- **Reusable Pattern**: `Teleporter/Hyperedge BFS: once any hyperedge member is visited, expand all and clear hyperedge.`
