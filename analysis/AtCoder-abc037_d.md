# Problem Analysis: AtCoder-abc037_d — Paths

**Problem ID**: `AtCoder-abc037_d`  
**Contest**: `abc037`  
**Rating / Difficulty**: 1377  
**URL**: https://atcoder.jp/contests/abc037/tasks/abc037_d  
**VJudge Tag**: `[problem:AtCoder-abc037_d]`  
**Category File**: [`../categories/dp/grid_strictly_increasing_paths_dag.md`](../categories/dp/grid_strictly_increasing_paths_dag.md)  

- **Tag (Domain)**: `Dynamic Programming`  
- **Subtopic**: `DAG DP`  
- **Topic (Skill)**: `2D Grid Strictly Increasing Paths Memoized DFS / DAG DP`  

---

## 1. Problem Statement & Key Idea
An H x W grid with integers a_{i, j}. Count all paths of length >= 1 that move 4-directionally to strictly greater adjacent cells, modulo 10^9 + 7.

**Key Idea**: Because each step moves to a strictly greater value, there are no cycles! The grid forms a Directed Acyclic Graph (DAG).

## 2. Core Observation & Invariant
Let dp[r][c] be the number of strictly increasing paths starting at cell (r, c). Base path of length 1 contributes 1. For each 4-directional neighbor (nr, nc) with a[nr][nc] > a[r][c]: dp[r][c] += dp[nr][nc]. Memoized DFS computes each cell exactly once in O(H * W).

## 3. Step-by-Step Algorithm
1. Initialize memo table of size H x W to -1.
2. Write DFS(r, c): if memo[r][c] != -1 return memo; ways = 1; for 4 neighbors: if a[nr][nc] > a[r][c]: ways = (ways + DFS(nr, nc)) % MOD; return memo[r][c] = ways.
3. Total answer is sum_{r, c} DFS(r, c) modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. Complete C++ Solution
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

## 6. Editorial Comparison & Alignment
Matches official editorial.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Memoized depth-first search on implicitly acyclic topological grids.
- **Reusable Pattern**: `Strictly increasing grid paths: dp[u] = 1 + sum_{(u, v): val[v] > val[u]} dp[v].`
