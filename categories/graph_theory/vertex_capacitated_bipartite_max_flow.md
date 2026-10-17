# Maximum Flow / Minimum Cut

**Domain**: `Graph Theory`  
**Subtopic**: `Flow and Min Cut`  

This workbook contains curated, high-quality competitive programming problems teaching **Maximum Flow / Minimum Cut**.

---

## Curated Problems

### `[problem:AtCoder-abc205_f]` — Grid and Tokens
- **Rating / Difficulty**: 2082
- **Contest**: `abc205`
- **Analysis**: [`analysis/AtCoder-abc205_f.md`](../../analysis/AtCoder-abc205_f.md)
- **Key Idea**: Each token can be chosen at most once (capacity 1 on token), can occupy at most one row, and can occupy at most one column. Furthermore, each row can host at most 1 token, and each column can host at most 1 token. We model this as a maximum flow network with node splitting: Source -> Row nodes (capacity 1) -> Token_in nodes (capacity 1) -> Token_out nodes (capacity 1) -> Column nodes (capacity 1) -> Sink.
- **Time Complexity**: `O(V^2 E) with Dinic, practically O(N * (H + W))`
- **Space Complexity**: `O(H + W + N + E)`
- **Verified C++ Implementation**:
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Edge {
    int to;
    int cap;
    int flow;
    int rev;
};

struct Dinic {
    int n;
    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

    Dinic(int n) : n(n), adj(n), level(n), ptr(n) {}

    void add_edge(int from, int to, int cap) {
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
            for (auto& edge : adj[v]) {
                if (edge.cap - edge.flow > 0 && level[edge.to] == -1) {
                    level[edge.to] = level[v] + 1;
                    q.push(edge.to);
                }
            }
        }
        return level[t] != -1;
    }

    int dfs(int v, int t, int pushed) {
        if (pushed == 0) return 0;
        if (v == t) return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); ++cid) {
            auto& edge = adj[v][cid];
            int tr = edge.to;
            if (level[v] + 1 != level[tr] || edge.cap - edge.flow == 0) continue;
            int tr_pushed = dfs(tr, t, min(pushed, edge.cap - edge.flow));
            if (tr_pushed == 0) continue;
            edge.flow += tr_pushed;
            adj[tr][edge.rev].flow -= tr_pushed;
            return tr_pushed;
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w, n;
    if (!(cin >> h >> w >> n)) return 0;

    int S = 0;
    int row_start = 1;
    int token_in_start = row_start + h;
    int token_out_start = token_in_start + n;
    int col_start = token_out_start + n;
    int T = col_start + w;

    Dinic dinic(T + 1);

    for (int r = 1; r <= h; ++r) {
        dinic.add_edge(S, row_start + r - 1, 1);
    }
    for (int c = 1; c <= w; ++c) {
        dinic.add_edge(col_start + c - 1, T, 1);
    }

    for (int i = 0; i < n; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        int t_in = token_in_start + i;
        int t_out = token_out_start + i;
        dinic.add_edge(t_in, t_out, 1);

        for (int r = a; r <= c; ++r) {
            dinic.add_edge(row_start + r - 1, t_in, 1);
        }
        for (int col = b; col <= d; ++col) {
            dinic.add_edge(t_out, col_start + col - 1, 1);
        }
    }

    cout << dinic.max_flow(S, T) << "\n";
    return 0;
}
```
