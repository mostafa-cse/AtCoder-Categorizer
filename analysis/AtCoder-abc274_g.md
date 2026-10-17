# Problem Analysis: AtCoder-abc274_g — G. Security Camera 3

**Problem ID**: `AtCoder-abc274_g`  
**Contest**: `abc274`  
**Rating / Difficulty**: 2340  
**URL**: https://atcoder.jp/contests/abc274/tasks/abc274_g  
**VJudge Tag**: `[problem:AtCoder-abc274_g]`  
**Category File**: [`../categories/graph_theory/security_camera_bipartite_matching_konig.md`](../categories/graph_theory/security_camera_bipartite_matching_konig.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Konig's Theorem and Maximum Independent Set in Bipartite Graphs`  

---

## 1. Problem Statement & Key Idea
Find the minimum number of surveillance cameras to monitor all empty cells in a grid with obstacles. Each camera covers a maximal row or column segment, reducing by König's theorem to maximum bipartite matching via Hopcroft-Karp in $O(HW \sqrt{HW})$.

## 2. Core Observation & Invariant
Each surveillance camera covers at most one maximal horizontal or vertical segment of empty cells. Every empty cell $(r, c)$ must be covered by its row segment or its column segment, reducing the problem to Minimum Vertex Cover in a bipartite graph.

## 3. Step-by-Step Algorithm
1. Decompose the empty cells into maximal contiguous horizontal segments (left vertices) and vertical segments (right vertices).
2. Add an edge between horizontal segment $H_{r, c}$ and vertical segment $V_{r, c}$ for every empty cell $(r, c)$.
3. By König's Theorem, the minimum vertex cover equals the maximum bipartite matching, computed via Hopcroft-Karp in $O(E \sqrt{V})$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(HW \sqrt{HW})`
- **Space Complexity**: `O(HW)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

struct HopcroftKarp {
    int n, m;
    vector<vector<int>> adj;
    vector<int> pair_u, pair_v, dist;

    HopcroftKarp(int n, int m) : n(n), m(m), adj(n), pair_u(n, -1), pair_v(m, -1), dist(n) {}

    void add_edge(int u, int v) {
        adj[u].push_back(v);
    }

    bool bfs() {
        queue<int> q;
        for (int u = 0; u < n; ++u) {
            if (pair_u[u] == -1) {
                dist[u] = 0;
                q.push(u);
            } else {
                dist[u] = -1;
            }
        }
        bool found = false;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                int next_u = pair_v[v];
                if (next_u == -1) {
                    found = true;
                } else if (dist[next_u] == -1) {
                    dist[next_u] = dist[u] + 1;
                    q.push(next_u);
                }
            }
        }
        return found;
    }

    bool dfs(int u) {
        for (int v : adj[u]) {
            int next_u = pair_v[v];
            if (next_u == -1 || (dist[next_u] == dist[u] + 1 && dfs(next_u))) {
                pair_u[u] = v;
                pair_v[v] = u;
                return true;
            }
        }
        dist[u] = -1;
        return false;
    }

    int max_matching() {
        int matching = 0;
        while (bfs()) {
            for (int u = 0; u < n; ++u) {
                if (pair_u[u] == -1 && dfs(u)) {
                    matching++;
                }
            }
        }
        return matching;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int h, w;
    if (!(cin >> h >> w)) return 0;

    vector<string> grid(h);
    for (int i = 0; i < h; ++i) {
        cin >> grid[i];
    }

    vector<vector<int>> h_id(h, vector<int>(w, -1));
    int num_h = 0;
    for (int r = 0; r < h; ++r) {
        int c = 0;
        while (c < w) {
            if (grid[r][c] == '.') {
                while (c < w && grid[r][c] == '.') {
                    h_id[r][c] = num_h;
                    c++;
                }
                num_h++;
            } else {
                c++;
            }
        }
    }

    vector<vector<int>> v_id(h, vector<int>(w, -1));
    int num_v = 0;
    for (int c = 0; c < w; ++c) {
        int r = 0;
        while (r < h) {
            if (grid[r][c] == '.') {
                while (r < h && grid[r][c] == '.') {
                    v_id[r][c] = num_v;
                    r++;
                }
                num_v++;
            } else {
                r++;
            }
        }
    }

    HopcroftKarp hk(num_h, num_v);
    for (int r = 0; r < h; ++r) {
        for (int c = 0; c < w; ++c) {
            if (grid[r][c] == '.') {
                hk.add_edge(h_id[r][c], v_id[r][c]);
            }
        }
    }

    cout << hk.max_matching() << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
