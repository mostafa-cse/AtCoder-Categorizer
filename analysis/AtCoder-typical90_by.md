# Problem Analysis: AtCoder-typical90_by — Planes on a 2D Plane

**Problem ID**: `AtCoder-typical90_by`  
**Contest**: `typical90` (Kyopro Typical 90, Problem 077)  
**Rating / Difficulty**: 2600 (★7)  
**URL**: https://atcoder.jp/contests/typical90/tasks/typical90_by  
**VJudge Tag**: `[problem:AtCoder-typical90_by]`  
**Category File**: [`../categories/graph_theory/bipartite_matching_geometry.md`](../categories/graph_theory/bipartite_matching_geometry.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Bipartite Matching & Network Flow`  
- **Topic (Skill)**: `Bipartite Matching on Geometric Directional Lattice via Dinic / Hopcroft-Karp`  

---

## 1. Problem Statement & Key Idea
N points A_i, N destination points B_j. Each point A_i must move to a unique destination B_j along one of 8 compass directions by exact distance T. Determine if valid bijection exists, and output direction for each point.

**Core Idea**: Bipartite Matching problem between N starting points and N destination points.

## 2. Core Observation & Invariant
For each point A_i, check its 8 compass destinations. Use a hash map on B coordinates to identify target indices in O(1). Add directed edges and run Dinic's Max-Flow algorithm.

## 3. Step-by-Step Algorithm
1. Hash map B points: map<pair<int, int>, int> id_B.
2. For each A_i: test 8 compass offsets by T. If destination in id_B, add flow edge i -> j.
3. Run Dinic's Algorithm. If max_flow == N, reconstruct direction for each A_i; else 'No'.

## 4. Complexity Analysis
Time: O(N sqrt(N)) with Dinic on unit network, Space: O(N).

## 5. Complete C++ Solution
```cpp
#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to, cap, rev, dir;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, int dir) {
        adj[from].push_back({to, 1, (int)adj[to].size(), dir});
        adj[to].push_back({from, 0, (int)adj[from].size() - 1, -1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (auto& e : adj[u]) {
                if (e.cap > 0 && level[e.to] == -1) {
                    level[e.to] = level[u] + 1;
                    q.push(e.to);
                }
            }
        }
        return level[t] != -1;
    }

    int dfs(int u, int t, int pushed) {
        if (pushed == 0 || u == t) return pushed;
        for (int& cid = ptr[u]; cid < (int)adj[u].size(); ++cid) {
            auto& e = adj[u][cid];
            if (level[u] + 1 != level[e.to] || e.cap == 0) continue;
            int tr = dfs(e.to, t, min(pushed, e.cap));
            if (tr == 0) continue;
            e.cap -= tr;
            adj[e.to][e.rev].cap += tr;
            return tr;
        }
        return 0;
    }

    int max_flow(int s, int t) {
        int flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (int pushed = dfs(s, t, 1e9)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int dx[] = {1, 1, 0, -1, -1, -1, 0, 1};
int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    long long t;
    if (!(cin >> n >> t)) return 0;

    vector<pair<long long, long long>> A(n + 1);
    for (int i = 1; i <= n; ++i) cin >> A[i].first >> A[i].second;

    map<pair<long long, long long>, int> id_B;
    for (int j = 1; j <= n; ++j) {
        long long bx, by;
        cin >> bx >> by;
        id_B[{bx, by}] = j;
    }

    int src = 0, sink = 2 * n + 1;
    Dinic dinic(sink + 1);

    for (int i = 1; i <= n; ++i) {
        dinic.add_edge(src, i, -1);
        dinic.add_edge(n + i, sink, -1);

        for (int d = 0; d < 8; ++d) {
            long long nx = A[i].first + dx[d] * t;
            long long ny = A[i].second + dy[d] * t;
            auto it = id_B.find({nx, ny});
            if (it != id_B.end()) {
                int j = it->second;
                dinic.add_edge(i, n + j, d + 1);
            }
        }
    }

    int flow = dinic.max_flow(src, sink);
    if (flow != n) {
        cout << "No\n";
        return 0;
    }

    cout << "Yes\n";
    vector<int> ans(n + 1);
    for (int i = 1; i <= n; ++i) {
        for (const auto& e : dinic.adj[i]) {
            if (e.to > n && e.to <= 2 * n && e.cap == 0) {
                ans[i] = e.dir;
                break;
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        cout << ans[i] << (i == n ? "" : " ");
    }
    cout << "\n";
    return 0;
}
```

## 6. Editorial Comparison & Alignment
Bipartite matching reduction on 8-direction geometric grid.

## 7. What This Problem Teaches & Reusable Pattern
- **Core Skill**: Bipartite matching with coordinate hash table lookup and path direction reconstruction.
- **Reusable Pattern**: `Geometric Bipartite Matching via Max-Flow.`

---
Back to [Bipartite Matching on Geometric Directional Lattice via Dinic / Hopcroft-Karp](../categories/graph_theory/bipartite_matching_geometry.md) | [Categories Directory](../categories/README.md)