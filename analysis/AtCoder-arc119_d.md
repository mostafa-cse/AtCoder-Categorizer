# Problem Analysis: AtCoder-arc119_d — D - Grid Repainting 3

**Problem ID**: `AtCoder-arc119_d`  
**Contest**: `arc119`  
**Rating / Difficulty**: 2713  
**URL**: https://atcoder.jp/contests/arc119/tasks/arc119_d  
**VJudge Tag**: `[problem:AtCoder-arc119_d]`  
**Category File**: [`../categories/graph_theory/grid_repainting_3_bipartite_matching.md`](../categories/graph_theory/grid_repainting_3_bipartite_matching.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`  

---

## 1. Problem Statement & Key Idea
We are given an H x W grid with 'R' (red) and 'B' (blue) cells. In each step, we can choose a red cell and repaint its entire row white (Operation X), or choose a red cell and repaint its entire column white (Operation Y). Once a cell is white, it can no longer be chosen. We want to maximize the final number of white squares and output an optimal sequence of operations.

## 2. Core Observation & Invariant
Construct a bipartite graph with row vertices 1..H on the left and column vertices 1..W on the right, where each red cell (r, c) represents an edge between row r and column c. For each connected component with V_R row vertices and V_C column vertices, we can find a spanning tree of V_R + V_C - 1 edges. By rooting the spanning tree at either a row vertex or a column vertex and processing edges bottom-up (leaves to root), we can eliminate either V_R - 1 rows and V_C columns (root at row), or V_R rows and V_C - 1 columns (root at column). In both choices, every processed edge connects a leaf to its parent, guaranteeing that the chosen cell is still red at the moment of the operation. Maximizing the total white area corresponds to minimizing (H - U)(W - V), which can be optimized over the number of components rooted at rows vs columns in O(K) time.

## 3. Step-by-Step Algorithm
1. 1. Construct the bipartite graph where row r is connected to col c for each red cell (r, c).
2. 2. Use Disjoint Set Union (DSU) to find a spanning forest of the non-trivial connected components in O(HW) time.
3. 3. For each of the K connected components, calculate its number of row and column vertices.
4. 4. Iterate over k_r in [0, K], representing the number of components rooted at a row vertex, and compute total deleted rows U and columns V. Select k_r that maximizes H*W - (H - U)*(W - V).
5. 5. For each component, set its root (row if among the first k_r components, else col) and perform a post-order tree traversal (leaves first). For each non-root vertex u with parent p, output Operation X at (u, p) if u is a row, or Operation Y at (p, u) if u is a column.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H + W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <numeric>
#include <algorithm>
#include <queue>

using namespace std;

struct DSU {
    int n;
    vector<int> parent;
    DSU(int n) : n(n), parent(n + 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i)
            return i;
        return parent[i] = find(parent[i]);
    }
    bool unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
            return true;
        }
        return false;
    }
};

struct Edge {
    int to;
    int r;
    int c;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<string> grid(H);
    for (int i = 0; i < H; ++i) {
        cin >> grid[i];
    }

    DSU dsu(H + W);
    vector<vector<Edge>> adj(H + W + 1);
    vector<bool> has_red(H + W + 1, false);

    for (int r = 1; r <= H; ++r) {
        for (int c = 1; c <= W; ++c) {
            if (grid[r - 1][c - 1] == 'R') {
                int u = r;
                int v = H + c;
                has_red[u] = true;
                has_red[v] = true;
                if (dsu.unite(u, v)) {
                    adj[u].push_back({v, r, c});
                    adj[v].push_back({u, r, c});
                }
            }
        }
    }

    vector<bool> visited(H + W + 1, false);
    vector<vector<int>> components;

    for (int i = 1; i <= H + W; ++i) {
        if (has_red[i] && !visited[i]) {
            vector<int> comp;
            queue<int> q;
            q.push(i);
            visited[i] = true;
            while (!q.empty()) {
                int u = q.front();
                q.pop();
                comp.push_back(u);
                for (const auto& edge : adj[u]) {
                    if (!visited[edge.to]) {
                        visited[edge.to] = true;
                        q.push(edge.to);
                    }
                }
            }
            components.push_back(comp);
        }
    }

    int K = components.size();
    long long total_R = 0, total_C = 0;
    for (const auto& comp : components) {
        for (int u : comp) {
            if (u <= H) total_R++;
            else total_C++;
        }
    }

    long long best_val = -1;
    int best_kr = 0;
    for (int kr = 0; kr <= K; ++kr) {
        int kc = K - kr;
        long long U = total_R - kr;
        long long V = total_C - kc;
        long long val = 1LL * H * W - (1LL * H - U) * (1LL * W - V);
        if (val > best_val) {
            best_val = val;
            best_kr = kr;
        }
    }

    struct Op {
        char type;
        int r, c;
    };
    vector<Op> ops;

    for (int idx = 0; idx < K; ++idx) {
        const auto& comp = components[idx];
        int root = -1;
        if (idx < best_kr) {
            // Root at a row vertex
            for (int u : comp) {
                if (u <= H) { root = u; break; }
            }
        } else {
            // Root at a col vertex
            for (int u : comp) {
                if (u > H) { root = u; break; }
            }
        }

        // BFS to find parent and ordering
        vector<int> parent(H + W + 1, -1);
        vector<int> parent_edge_r(H + W + 1, 0);
        vector<int> parent_edge_c(H + W + 1, 0);
        vector<int> order;
        queue<int> q;

        q.push(root);
        parent[root] = 0;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            order.push_back(u);
            for (const auto& edge : adj[u]) {
                if (parent[edge.to] == -1) {
                    parent[edge.to] = u;
                    parent_edge_r[edge.to] = edge.r;
                    parent_edge_c[edge.to] = edge.c;
                    q.push(edge.to);
                }
            }
        }

        // Post-order processing (leaves to root)
        for (int i = (int)order.size() - 1; i >= 0; --i) {
            int u = order[i];
            if (u != root) {
                int er = parent_edge_r[u];
                int ec = parent_edge_c[u];
                if (u <= H) {
                    ops.push_back({'X', er, ec});
                } else {
                    ops.push_back({'Y', er, ec});
                }
            }
        }
    }

    cout << ops.size() << "\n";
    for (const auto& op : ops) {
        cout << op.type << " " << op.r << " " << op.c << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
