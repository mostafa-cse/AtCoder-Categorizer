# Problem Analysis: AtCoder-abc472_g — Cascading Grid

**Problem ID**: `AtCoder-abc472_g`  
**Contest**: `abc472`  
**Rating / Difficulty**: 2018  
**URL**: https://atcoder.jp/contests/abc472/tasks/abc472_g  
**VJudge Tag**: `[problem:AtCoder-abc472_g]`  
**Category File**: [`../categories/graph_theory/maximum_weight_closure_min_cut_grid.md`](../categories/graph_theory/maximum_weight_closure_min_cut_grid.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Network Flow`  
- **Topic (Skill)**: `Maximum Weight Closure via Min-Cut on Grid Directed Reachability`  

---

## 1. Problem Statement & Key Idea
An H x W grid has cells with '+', '-', or '#'. Operation: pick a non-# cell and turn to '#' all cells reachable by moving Left, Right, or Down without passing through '#'. Find the maximum possible value of (count of '+' minus count of '-') remaining in the grid.

**Key Idea**: Eliminating a cell triggers the elimination of all cells reachable by moving Left, Right, or Down. Thus, the set of eliminated cells must form a closed set in a directed reachability graph. If we eliminate a '-' cell, we gain profit +1; if we eliminate a '+' cell, we incur cost 1 (weight -1). Maximizing the score improvement is exactly the Maximum Weight Closure Problem (Project Selection Problem) on a directed graph, solvable via Min-Cut / Dinic's Algorithm.

## 2. Core Observation & Invariant
Downward reachability constraints define a transitive closure where removing penalties is dual to minimum cut project selection.

## 3. Step-by-Step Algorithm
1. Calculate base score = count(+) - count(-).
2. Build directed graph on non-# cells: directed edge from u to v if v is adjacent to u by Left, Right, or Down.
3. Weight of eliminating cell u: if '-', w(u) = +1; if '+', w(u) = -1.
4. Construct network flow graph: Source S, Sink T.
5.   For each node u with w(u) > 0: add edge S -> u with capacity w(u).
6.   For each node u with w(u) < 0: add edge u -> T with capacity -w(u).
7.   For each dependency u -> v: add edge u -> v with capacity INF.
8. Compute max flow using Dinic's algorithm.
9. Max profit gained by eliminating cells = sum_{w > 0} w - min_cut.
10. Max total score = base_score + max_profit.

## 4. Complexity Analysis
- **Time Complexity**: `O(V^2 * E) with Dinic on V <= 900`
- **Space Complexity**: `O(V + E)`

## 5. Core Algorithmic Skill & Learning Takeaway
Project selection / Maximum weight closure reduction to Dinic Min-Cut.

**Reusable Pattern**: Grid Closure Min-Cut: Transforming directional cascading domino eliminations into Max Weight Closure.

## 6. Comparison with Alternative Approaches
Matches official editorial.

## 7. Verified Clean C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    long long cap;
    long long flow;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, long long cap) {
        adj[from].push_back({to, cap, 0, (int)adj[to].size()});
        adj[to].push_back({from, 0, 0, (int)adj[from].size() - 1});
    }

    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);

        while (!q.empty()) {
            int v = q.front();
            q.pop();

            for (const auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    long long dfs(int v, int t, long long pushed) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;

        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int trg = edge.to;
            if (level[v] + 1 != level[trg] || edge.cap - edge.flow == 0) continue;

            long long tr = dfs(trg, t, min(pushed, edge.cap - edge.flow));
            if (tr == 0) continue;

            edge.flow += tr;
            adj[trg][edge.rev].flow -= tr;
            return tr;
        }
        return 0;
    }

    long long max_flow(int s, int t) {
        long long flow = 0;
        while (bfs(s, t)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, t, INF)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    long long base_score = 0;
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
        for (char c : grid[i]) {
            if (c == '+') base_score++;
            else if (c == '-') base_score--;
        }
    }

    auto id = [&](int r, int c) {
        return r * w + c;
    };

    int total_nodes = h * w;
    int S = total_nodes, T = total_nodes + 1;
    Dinic dinic(total_nodes + 2);

    long long positive_profit = 0;

    // Movement: Left (0, -1), Right (0, 1), Down (1, 0)
    const int dr[3] = {0, 0, 1};
    const int dc[3] = {-1, 1, 0};

    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '#') continue;

            int u = id(r, c);
            long long weight = (grid[r][c] == '-' ? 1 : -1);

            if (weight > 0) {
                dinic.add_edge(S, u, weight);
                positive_profit += weight;
            } else if (weight < 0) {
                dinic.add_edge(u, T, -weight);
            }

            for (int d = 0; d < 3; ++d) {
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (nr >= 0 && nr < h && nc >= 0 && nc < w && grid[nr][nc] != '#') {
                    dinic.add_edge(u, id(nr, nc), INF);
                }
            }
        }
    }

    long long min_cut = dinic.max_flow(S, T);
    long long max_gain = positive_profit - min_cut;

    cout << base_score + max_gain << "\n";
    return 0;
}
```
