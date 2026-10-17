# Min-Cut / Max-Flow Model on Network Disconnection

**Domain**: `Graph Theory`  
**Subtopic**: `Network Flow`  

This workbook contains curated, high-quality competitive programming problems teaching **Min-Cut / Max-Flow Model on Network Disconnection**.

---

## Curated Problems

### `[problem:AtCoder-abc010_4]` — 浮気予防
- **Rating / Difficulty**: 1777
- **Contest**: `abc010`
- **Analysis**: [`analysis/AtCoder-abc010_4.md`](../../analysis/AtCoder-abc010_4.md)
- **Key Idea**: Standard Min-Cut problem. Source is Takahashi (0). Create a supersink T. For each of the G girls, add an edge to T with capacity 1. For each original friendship edge (u, v), add bidirectional capacity 1. By the Max-Flow Min-Cut Theorem, min cut equals max flow from 0 to T.
- **Time Complexity**: `O(V^2 * E)`
- **Space Complexity**: `O(V + E)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to, rev;
    int cap, flow;
};

struct Dinic {
    int n, s, t;
    vector<vector<Edge>> adj;
    vector<int> level, ptr;

    Dinic(int n, int s, int t) : n(n), s(s), t(t), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, int cap) {
        adj[from].push_back({to, (int)adj[to].size(), cap, 0});
        adj[to].push_back({from, (int)adj[from].size() - 1, 0, 0});
    }

    bool bfs() {
        fill(level.begin(), level.end(), -1);
        level[s] = 0;
        queue<int> q;
        q.push(s);

        while (!q.empty()) {
            int v = q.front(); q.pop();
            for (auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    int dfs(int v, int pushed) {
        if (pushed == 0 || v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
            int tr_pushed = dfs(tr, min(pushed, edge.cap - edge.flow));
            if (tr_pushed == 0) continue;
            edge.flow += tr_pushed;
            adj[tr][edge.rev].flow -= tr_pushed;
            return tr_pushed;
        }
        return 0;
    }

    int max_flow() {
        int flow = 0;
        while (bfs()) {
            fill(ptr.begin(), ptr.end(), 0);
            while (int pushed = dfs(s, 1e9)) {
                flow += pushed;
            }
        }
        return flow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, g, m;
    if (!(cin >> n >> g >> m)) return 0;

    int sink = n;
    Dinic dinic(n + 1, 0, sink);

    for (int i = 0; i < g; ++i) {
        int girl;
        cin >> girl;
        dinic.add_edge(girl, sink, 1);
    }

    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        dinic.add_edge(u, v, 1);
        dinic.add_edge(v, u, 1);
    }

    cout << dinic.max_flow() << "\n";
    return 0;
}
```
