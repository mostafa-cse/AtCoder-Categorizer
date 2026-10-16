# Problem Analysis: AtCoder-typical90_aq — Maze Challenge with Lack of Sleep

**Problem ID**: `AtCoder-typical90_aq`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 043)  
**Rating / Difficulty**: 1350 (★4)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_aq  
**VJudge Tag**: `[problem:AtCoder-typical90_aq]`  
**Category File**: [`../categories/graph_theory/shortest_paths_01_bfs.md`](../categories/graph_theory/shortest_paths_01_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `0-1 BFS with State Direction / Minimum Turn Path`  

---

## 1. Problem Statement & Key Idea
H x W grid with walls. Start at (r_s, c_s), goal at (r_t, c_t). Moving in the same direction costs 0 turns; changing direction costs 1 turn. Find minimum turns to reach goal.

**Core Idea**: Maintain state (r, c, dir). Edge weights are 0 (continue same dir) and 1 (change dir). Solve using 0-1 BFS with a deque.

## 2. Core Observation & Invariant
Because edge weights are strictly {0, 1}, pushing weight-0 edges to the front and weight-1 edges to the back of a deque guarantees monotonic distance processing in O(HW) linear time.

## 3. Step-by-Step Algorithm
1. dist[H][W][4] initialized to INF.
2. Push initial 4 directions from start into deque with dist = 0.
3. While deque not empty: pop (r, c, dir):
   - Straight step: (nr, nc) in same dir has cost 0 -> push_front.
   - Turn in place: other directions have cost 1 -> push_back.
4. Output min over all 4 directions at goal.

## 4. Complexity Analysis
Time: O(H * W), Space: O(H * W).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <deque>
#include <algorithm>

using namespace std;

const int INF = 1e9 + 7;

struct State {
    int r, c, dir;
};

int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0, -1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    int rs, cs, rt, ct;
    cin >> rs >> cs >> rt >> ct;
    --rs; --cs; --rt; --ct;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) cin >> grid[i];

    vector<vector<vector<int>>> dist(h, vector<vector<int>>(w, vector<int>(4, INF)));
    deque<State> dq;

    for (int d = 0; d < 4; ++d) {
        dist[rs][cs][d] = 0;
        dq.push_back({rs, cs, d});
    }

    while (!dq.empty()) {
        auto [r, c, d] = dq.front();
        dq.pop_front();

        // Move forward in same direction (cost 0)
        int nr = r + dr[d], nc = c + dc[d];
        if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] == '.') {
            if (dist[r][c][d] < dist[nr][nc][d]) {
                dist[nr][nc][d] = dist[r][c][d];
                dq.push_front({nr, nc, d});
            }
        }

        // Change direction (cost 1)
        for (int nd = 0; nd < 4; ++nd) {
            if (nd != d && dist[r][c][d] + 1 < dist[r][c][nd]) {
                dist[r][c][nd] = dist[r][c][d] + 1;
                dq.push_back({r, c, nd});
            }
        }
    }

    int ans = INF;
    for (int d = 0; d < 4; ++d) {
        ans = min(ans, dist[rt][ct][d]);
    }

    cout << ans << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
0-1 BFS state graph with directional orientation.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: 0-1 BFS with std::deque, directional orientation in grid states, and linear time turn minimization.
- **Reusable Pattern**: `0-1 BFS on State Grid.`

---
Back to [0-1 BFS with State Direction / Minimum Turn Path](../categories/graph_theory/shortest_paths_01_bfs.md) | [Categories Directory](../categories/README.md)