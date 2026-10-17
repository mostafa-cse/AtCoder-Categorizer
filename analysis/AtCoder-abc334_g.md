# Problem Analysis: AtCoder-abc334_g — Christmas Color Grid 2

**Problem ID**: `AtCoder-abc334_g`  
**Contest**: `abc334`  
**Rating / Difficulty**: 2242  
**URL**: https://atcoder.jp/contests/abc334/tasks/abc334_g  
**VJudge Tag**: `[problem:AtCoder-abc334_g]`  
**Category File**: [`../categories/graph_theory/articulation_points_random_vertex_deletion_components.md`](../categories/graph_theory/articulation_points_random_vertex_deletion_components.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Connectivity`  
- **Topic (Skill)**: `Articulation Points and Block Cut Tree`  

---

## 1. Problem Statement & Key Idea
Compute the expected number of connected components of green cells after turning one green cell chosen uniformly at random into red.

## 2. Core Observation & Invariant
Let C be the initial number of connected components of green cells. Removing a vertex u changes the number of components depending on its articulation status: an isolated vertex reduces components by 1; a non-articulation vertex leaves components unchanged (delta = 0); an articulation vertex splits its component into k >= 2 pieces (delta = k - 1). Using Tarjan's DFS tree, for root r, delta = children - 1; for non-root u, delta = count of DFS children v with low[v] >= tin[u].

## 3. Step-by-Step Algorithm
1. 1. Build adjacency list of green cells on the H x W grid and count total green cells G.
2. 2. Run Tarjan's DFS on all connected components, tracking tin, low, and DFS tree children.
3. 3. Compute delta[u] for each green cell u using the lowlink condition.
4. 4. Sum (C + delta[u]) over all green cells u modulo 998244353.
5. 5. Multiply the total sum by G^(-1) modulo 998244353.

## 4. Complexity Analysis
- **Time Complexity**: `O(H * W)`
- **Space Complexity**: `O(H * W)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int MOD = 998244353;

long long mod_pow(long long base, long long exp) {
    long long res = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp % 2 == 1) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp /= 2;
    }
    return res;
}

long long mod_inv(long long n) {
    return mod_pow(n, MOD - 2);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    if (!(cin >> H >> W)) return 0;

    vector<string> S(H);
    for (int i = 0; i < H; ++i) {
        cin >> S[i];
    }

    int n_cells = H * W;
    vector<vector<int>> adj(n_cells);

    int green_count = 0;
    auto get_id = [&](int r, int c) {
        return r * W + c;
    };

    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            if (S[r][c] == '#') {
                green_count++;
                int u = get_id(r, c);
                for (int d = 0; d < 4; ++d) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < H && nc >= 0 && nc < W && S[nr][nc] == '#') {
                        adj[u].push_back(get_id(nr, nc));
                    }
                }
            }
        }
    }

    if (green_count == 0) {
        cout << 0 << "\n";
        return 0;
    }

    vector<int> tin(n_cells, 0), low(n_cells, 0);
    vector<bool> visited(n_cells, false);
    int timer = 0;
    int total_components = 0;

    // delta[u] = change in total components if green cell u is deleted
    vector<int> delta(n_cells, 0);

    auto dfs = [&](auto& self, int u, int p) -> void {
        visited[u] = true;
        tin[u] = low[u] = ++timer;
        int children = 0;
        int cuts = 0;

        for (int v : adj[u]) {
            if (v == p) continue;
            if (visited[v]) {
                low[u] = min(low[u], tin[v]);
            } else {
                children++;
                self(self, v, u);
                low[u] = min(low[u], low[v]);
                if (low[v] >= tin[u]) {
                    cuts++;
                }
            }
        }

        if (p == -1) {
            // Root of DFS tree
            // If children == 0, removing u leaves 0 components (delta = -1)
            // If children > 0, removing u leaves children components (delta = children - 1)
            delta[u] = children - 1;
        } else {
            // Non-root: cuts subtrees disconnected + 1 parent component
            delta[u] = cuts;
        }
    };

    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            if (S[r][c] == '#') {
                int u = get_id(r, c);
                if (!visited[u]) {
                    total_components++;
                    dfs(dfs, u, -1);
                }
            }
        }
    }

    long long sum_components = 0;
    for (int r = 0; r < H; ++r) {
        for (int c = 0; c < W; ++c) {
            if (S[r][c] == '#') {
                int u = get_id(r, c);
                long long comps = total_components + delta[u];
                sum_components = (sum_components + comps) % MOD;
            }
        }
    }

    long long ans = (sum_components * mod_inv(green_count)) % MOD;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
