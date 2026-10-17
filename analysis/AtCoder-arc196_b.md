# Problem Analysis: AtCoder-arc196_b — B. Torus Loop

**Problem ID**: `AtCoder-arc196_b`  
**Contest**: `arc196`  
**Rating / Difficulty**: 2188  
**URL**: https://atcoder.jp/contests/arc196/tasks/arc196_b  
**VJudge Tag**: `[problem:AtCoder-arc196_b]`  
**Category File**: [`../categories/data_structures/bipartite_potential_dsu_torus_edge_loops.md`](../categories/data_structures/bipartite_potential_dsu_torus_edge_loops.md)  

- **Tag (Domain)**: `Data Structures (DS)`  
- **Subtopic**: `Disjoint Set Union (DSU)`  
- **Topic (Skill)**: `Augmented DSU / Weighted DSU`  

---

## 1. Problem Statement & Key Idea
Determine the number of tile rotations of Type A (connecting adjacent edges) and Type B (connecting opposite edges) on an H x W torus grid such that line segments form closed loops without dead ends modulo 998244353.

## 2. Core Observation & Invariant
Each edge presence on the grid is boolean. For each row, horizontal edge presences propagate by toggling on Type A tiles, requiring an even number of Type A tiles per row (and per column) to close around the torus. Type B tiles impose XOR relations between row and column edge variables, forming a bipartite graph of constraints. If any cycle is contradictory (odd parity), answer is 0; otherwise 2^{components}.

## 3. Step-by-Step Algorithm
1. For each row i: compute prefix XORs of A occurrences. If total A count is odd, output 0.
2. For each column j: compute prefix XORs of A occurrences. If total A count is odd, output 0.
3. Construct a bipartite graph with H row vertices and W column vertices.
4. For each cell (i, j) with S_{i, j} == 'B': add edge between row i and col H+j with required difference 1 ^ pref_row[i][j-1] ^ pref_col[i-1][j].
5. Find connected components and verify 2-colorability using BFS. If any conflict occurs, output 0.
6. If consistent, output 2^{components} mod 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(HW)`
- **Space Complexity**: `O(HW)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

void solve() {
    int H, W;
    if (!(cin >> H >> W)) return;

    vector<string> S(H);
    for (int i = 0; i < H; ++i) {
        cin >> S[i];
    }

    vector<vector<int>> pref_row(H, vector<int>(W, 0));
    for (int i = 0; i < H; ++i) {
        int cnt = 0;
        for (int j = 0; j < W; ++j) {
            cnt ^= (S[i][j] == 'A' ? 1 : 0);
            pref_row[i][j] = cnt;
        }
        if (cnt != 0) {
            cout << 0 << "\n";
            return;
        }
    }

    vector<vector<int>> pref_col(H, vector<int>(W, 0));
    for (int j = 0; j < W; ++j) {
        int cnt = 0;
        for (int i = 0; i < H; ++i) {
            cnt ^= (S[i][j] == 'A' ? 1 : 0);
            pref_col[i][j] = cnt;
        }
        if (cnt != 0) {
            cout << 0 << "\n";
            return;
        }
    }

    // Graph with H + W vertices
    // 0 .. H-1: rows (x_i)
    // H .. H+W-1: cols (y_j)
    int V = H + W;
    vector<vector<pair<int, int>>> adj(V);

    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (S[i][j] == 'B') {
                int left_offset = (j == 0 ? 0 : pref_row[i][j - 1]);
                int top_offset = (i == 0 ? 0 : pref_col[i - 1][j]);
                int req_diff = 1 ^ left_offset ^ top_offset;
                adj[i].push_back({H + j, req_diff});
                adj[H + j].push_back({i, req_diff});
            }
        }
    }

    vector<int> color(V, -1);
    int components = 0;

    for (int i = 0; i < V; ++i) {
        if (color[i] == -1) {
            components++;
            vector<int> q;
            color[i] = 0;
            q.push_back(i);
            int head = 0;
            while (head < (int)q.size()) {
                int u = q[head++];
                for (auto const& edge : adj[u]) {
                    int v = edge.first;
                    int diff = edge.second;
                    if (color[v] == -1) {
                        color[v] = color[u] ^ diff;
                        q.push_back(v);
                    } else {
                        if (color[v] != (color[u] ^ diff)) {
                            cout << 0 << "\n";
                            return;
                        }
                    }
                }
            }
        }
    }

    long long ans = 1;
    for (int i = 0; i < components; ++i) {
        ans = (ans * 2) % MOD;
    }

    cout << ans << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    if (cin >> T) {
        while (T--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
