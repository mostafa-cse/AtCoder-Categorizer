# Problem Analysis: AtCoder-abc317_g — Rearranging

**Problem ID**: `AtCoder-abc317_g`  
**Contest**: `abc317`  
**Rating / Difficulty**: 2649  
**URL**: https://atcoder.jp/contests/abc317/tasks/abc317_g  
**VJudge Tag**: `[problem:AtCoder-abc317_g]`  
**Category File**: [`../categories/graph_theory/matrix_rearranging_max_flow.md`](../categories/graph_theory/matrix_rearranging_max_flow.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Flow and Min Cut`  
- **Topic (Skill)**: `Maximum Flow / Minimum Cut`  

---

## 1. Problem Statement & Key Idea
By Hall's Marriage Theorem and the Birkhoff-von Neumann theorem, an N x M matrix where every integer 1..N appears exactly M times can be rearranged column-by-column into a Latin rectangle (where every column is a permutation of 1..N) by finding M successive perfect matchings in a regular bipartite graph.

## 2. Core Observation & Invariant
Construct a bipartite graph with N rows on the left and N values on the right. Each cell in row r with value v creates an edge (r, v). Since each row contains M values and each value appears M times across the grid, the bipartite multigraph is M-regular. By Hall's condition, every regular bipartite graph contains a 1-factor (perfect matching). Extracting this matching determines column j and leaves an (M-1)-regular bipartite graph. Repeating this M times completely factors the matrix.

## 3. Step-by-Step Algorithm
1. 1. Build bipartite flow network between N rows (source -> row r with capacity 1) and N values (value v -> sink with capacity 1).
2. 2. Add directed edges from row r to value v with capacity equal to the multiplicity of value v in row r.
3. 3. Run Dinic's max flow algorithm to find a perfect matching of size N.
4. 4. Assign matched values to the current column j, and decrement the edge multiplicities.
5. 5. Repeat for each column j = 1..M.
6. 6. Output 'Yes' and print the resulting N x M grid.

## 4. Complexity Analysis
- **Time Complexity**: `O(M * N^2.5)`
- **Space Complexity**: `O(N * M)`

## 5. C++ Source Code
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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    if (!(cin >> N >> M)) return 0;

    // row_counts[i][v] = count of number v remaining in row i (1-indexed)
    vector<vector<int>> row_counts(N + 1, vector<int>(N + 1, 0));
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= M; ++j) {
            int a;
            cin >> a;
            row_counts[i][a]++;
        }
    }

    vector<vector<int>> B(N + 1, vector<int>(M + 1, 0));

    // For each column col = 1 to M, find a perfect matching of size N
    for (int col = 1; col <= M; ++col) {
        int source = 0;
        int sink = 2 * N + 1;
        Dinic dinic(sink + 1);

        // Left side: row 1 to N
        for (int i = 1; i <= N; ++i) {
            dinic.add_edge(source, i, 1);
        }
        // Right side: number 1 to N (mapped to N + 1 to 2N)
        for (int v = 1; v <= N; ++v) {
            dinic.add_edge(N + v, sink, 1);
        }
        // Bipartite edges
        for (int i = 1; i <= N; ++i) {
            for (int v = 1; v <= N; ++v) {
                if (row_counts[i][v] > 0) {
                    dinic.add_edge(i, N + v, 1);
                }
            }
        }

        int flow = dinic.max_flow(source, sink);
        if (flow < N) {
            cout << "No\n";
            return 0;
        }

        // Extract matching
        for (int i = 1; i <= N; ++i) {
            for (auto& edge : dinic.adj[i]) {
                if (edge.to > N && edge.to <= 2 * N && edge.flow == 1) {
                    int val = edge.to - N;
                    B[i][col] = val;
                    row_counts[i][val]--;
                    break;
                }
            }
        }
    }

    cout << "Yes\n";
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= M; ++j) {
            cout << B[i][j] << (j == M ? "" : " ");
        }
        cout << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
