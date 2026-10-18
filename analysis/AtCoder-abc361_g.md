# Problem Analysis: AtCoder-abc361_g — G - Go Terrirory

**Problem ID**: `AtCoder-abc361_g`  
**Contest**: `abc361`  
**Rating / Difficulty**: 2613  
**URL**: https://atcoder.jp/contests/abc361/tasks/abc361_g  
**VJudge Tag**: `[problem:AtCoder-abc361_g]`  
**Category File**: [`../categories/graph_theory/go_territory_bfs.md`](../categories/graph_theory/go_territory_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Breadth First Search (BFS)`  

---

## 1. Problem Statement & Key Idea
On an unbounded 2D grid with N obstacle points with coordinates up to 200000, find the number of non-negative integer grid points that cannot reach infinity without crossing obstacles.

## 2. Core Observation & Invariant
Since coordinates are bounded by M = 200000, we can represent free cells on each row x in [0, M] as maximal disjoint open intervals between obstacles. Two intervals on adjacent rows x and x+1 are connected iff they overlap. The total number of intervals is at most N + M. Running a BFS from the boundary / infinity marks all unclosed cells. Any cell belonging to an unmarked interval is completely enclosed by obstacles.

## 3. Step-by-Step Algorithm
1. For each row x in [0, M], collect obstacle y-coordinates and form disjoint free intervals.
2. Connect overlapping intervals between adjacent rows x and x+1 using a two-pointer sweep.
3. Queue all intervals that touch the boundary (x > M or y > M or y = 0 outside obstacles) into a BFS.
4. Mark all reachable intervals.
5. Sum the lengths of all unvisited intervals to obtain the total enclosed points.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    int max_coord = 0;
    vector<pair<int, int>> stones(N);
    for (int i = 0; i < N; ++i) {
        cin >> stones[i].first >> stones[i].second;
        max_coord = max(max_coord, max(stones[i].first, stones[i].second));
    }

    int max_c = max_coord + 2;
    vector<vector<int>> row_stones(max_c + 1);
    for (int i = 0; i < N; ++i) {
        if (stones[i].first <= max_c) {
            row_stones[stones[i].first].push_back(stones[i].second);
        }
    }

    vector<vector<pair<int, int>>> row_intervals(max_c + 1);
    for (int x = 0; x <= max_c; ++x) {
        sort(row_stones[x].begin(), row_stones[x].end());
        int cur = 0;
        for (int y : row_stones[x]) {
            if (y > cur) {
                row_intervals[x].push_back({cur, y - 1});
            }
            cur = y + 1;
        }
        if (cur <= max_c) {
            row_intervals[x].push_back({cur, max_c});
        }
    }

    vector<vector<int>> int_id(max_c + 1);
    vector<pair<int, pair<int, int>>> id_to_int;
    for (int x = 0; x <= max_c; ++x) {
        int_id[x].resize(row_intervals[x].size());
        for (size_t idx = 0; idx < row_intervals[x].size(); ++idx) {
            int_id[x][idx] = (int)id_to_int.size();
            id_to_int.push_back({x, row_intervals[x][idx]});
        }
    }

    int num_nodes = (int)id_to_int.size();
    vector<vector<int>> adj(num_nodes);

    for (int x = 0; x < max_c; ++x) {
        const auto& I = row_intervals[x];
        const auto& J = row_intervals[x + 1];
        size_t p2 = 0;
        for (size_t p1 = 0; p1 < I.size(); ++p1) {
            int L1 = I[p1].first;
            int R1 = I[p1].second;
            while (p2 < J.size() && J[p2].second < L1) {
                p2++;
            }
            size_t cur_p2 = p2;
            while (cur_p2 < J.size() && J[cur_p2].first <= R1) {
                int u = int_id[x][p1];
                int v = int_id[x + 1][cur_p2];
                adj[u].push_back(v);
                adj[v].push_back(u);
                cur_p2++;
            }
        }
    }

    queue<int> q;
    vector<bool> visited(num_nodes, false);
    for (int u = 0; u < num_nodes; ++u) {
        int x = id_to_int[u].first;
        int L = id_to_int[u].second.first;
        int R = id_to_int[u].second.second;
        if (x == 0 || x == max_c || L == 0 || R == max_c) {
            visited[u] = true;
            q.push(u);
        }
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }

    long long ans = 0;
    for (int u = 0; u < num_nodes; ++u) {
        if (!visited[u]) {
            int L = id_to_int[u].second.first;
            int R = id_to_int[u].second.second;
            ans += (long long)(R - L + 1);
        }
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
