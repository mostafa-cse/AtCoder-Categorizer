# 2D Grid Strictly Increasing Paths Memoized DFS / DAG DP

**Domain**: `Dynamic Programming`  
**Subtopic**: `DAG DP`  

This workbook contains curated, high-quality competitive programming problems teaching **2D Grid Strictly Increasing Paths Memoized DFS / DAG DP**.

---

## Curated Problems

### [problem:AtCoder-abc037_d] — Paths
- **Contest**: `abc037`
- **Rating / Difficulty**: 1377
- **Specific Skill**: 2D Grid Strictly Increasing Paths Memoized DFS / DAG DP
- **Individual Analysis**: [`../../analysis/AtCoder-abc037_d.md`](../../analysis/AtCoder-abc037_d.md)
- **Problem Statement Summary**: An H x W grid with integers a_{i, j}. Count all paths of length >= 1 that move 4-directionally to strictly greater adjacent cells, modulo 10^9 + 7.
- **Core Insight**: Let dp[r][c] be the number of strictly increasing paths starting at cell (r, c). Base path of length 1 contributes 1. For each 4-directional neighbor (nr, nc) with a[nr][nc] > a[r][c]: dp[r][c] += dp[nr][nc]. Memoized DFS computes each cell exactly once in O(H * W).
- **Complexity**: Time: `O(H * W)` | Space: `O(H * W)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>

using namespace std;

const int MOD = 1e9 + 7;
int h, w;
vector<vector<int>> a;
vector<vector<long long>> memo;

int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

long long dfs(int r, int c) {
    if (memo[r][c] != -1) return memo[r][c];

    long long ways = 1;
    for (int d = 0; d < 4; ++d) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if (nr >= 0 && nr < h && nc >= 0 && nc < w && a[nr][nc] > a[r][c]) {
            ways = (ways + dfs(nr, nc)) % MOD;
        }
    }

    return memo[r][c] = ways;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    if (!(cin >> h >> w)) return 0;

    a.assign(h, vector<int>(w));
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            cin >> a[r][c];
        }
    }

    memo.assign(h, vector<long long>(w, -1));

    long long total = 0;
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            total = (total + dfs(r, c)) % MOD;
        }
    }

    cout << total << "\n";
    return 0;
}
```
