# Problem Analysis: AtCoder-arc013_4 — D. 切り分けできるかな？ (Can it be cut?)

**Problem ID**: `AtCoder-arc013_4`  
**Contest**: `arc013`  
**Rating / Difficulty**: 2535  
**URL**: https://atcoder.jp/contests/arc013/tasks/arc013_4  
**VJudge Tag**: `[problem:AtCoder-arc013_4]`  
**Category File**: [`../categories/graph_theory/can_it_be_cut_hopcroft_karp.md`](../categories/graph_theory/can_it_be_cut_hopcroft_karp.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Matching`  
- **Topic (Skill)**: `Bipartite Matching (HopCroft Karp Algorithm and Kuhn's Algorithm)`  

---

## 1. Problem Statement & Key Idea
Given N rectangular prisms with dimensions (X_i, Y_i, Z_i), we can slice prisms along grid planes parallel to their faces into 1x1x1 unit cubes. Minimize the total number of cutting actions by sharing cuts between overlapping orthogonal dimensions via maximum bipartite matching.

## 2. Core Observation & Invariant
Slicing a block of dimensions X x Y x Z into 1x1x1 cubes requires (X-1) cuts along X, (Y-1) cuts along Y, and (Z-1) cuts along Z. However, cuts along two orthogonal axes can be grouped into independent slice operations: if a cut along dimension A and a cut along dimension B are executed together, they save 1 operation. This models a maximum matching on a bipartite graph where left vertices are cuts on one axis and right vertices are cuts on the orthogonal axis.

## 3. Step-by-Step Algorithm
1. Construct bipartite graph between available orthogonal cutting axes for each prism.
2. For each dimension, create nodes representing the required cuts.
3. Add edges between orthogonal cuts that can share knife strokes without geometric conflicts.
4. Execute Hopcroft-Karp maximum bipartite matching algorithm to find maximum matching M.
5. Total cuts required = total independent cuts minus |M| plus base block slices.

## 4. Complexity Analysis
- **Time Complexity**: `O(V sqrt(E)) via Hopcroft-Karp`
- **Space Complexity**: `O(V + E)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

const int INF = 1e9;

// Hopcroft-Karp algorithm
struct HopcroftKarp {
    int n, m;
    vector<vector<int>> adj;
    vector<int> pair_u, pair_v, dist;

    HopcroftKarp(int n, int m) : n(n), m(m), adj(n + 1), pair_u(n + 1, 0), pair_v(m + 1, 0), dist(n + 1, 0) {}

    void add_edge(int u, int v) {
        adj[u].push_back(v);
    }

    bool bfs() {
        queue<int> q;
        for (int u = 1; u <= n; u++) {
            if (pair_u[u] == 0) {
                dist[u] = 0;
                q.push(u);
            } else {
                dist[u] = INF;
            }
        }
        dist[0] = INF;
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            if (dist[u] < dist[0]) {
                for (int v : adj[u]) {
                    if (dist[pair_v[v]] == INF) {
                        dist[pair_v[v]] = dist[u] + 1;
                        q.push(pair_v[v]);
                    }
                }
            }
        }
        return dist[0] != INF;
    }

    bool dfs(int u) {
        if (u != 0) {
            for (int v : adj[u]) {
                if (dist[pair_v[v]] == dist[u] + 1) {
                    if (dfs(pair_v[v])) {
                        pair_v[v] = u;
                        pair_u[u] = v;
                        return true;
                    }
                }
            }
            dist[u] = INF;
            return false;
        }
        return true;
    }

    int max_matching() {
        int matching = 0;
        while (bfs()) {
            for (int u = 1; u <= n; u++) {
                if (pair_u[u] == 0 && dfs(u)) {
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

    int N;
    if (!(cin >> N)) return 0;

    struct Block {
        int x, y, z;
    };
    vector<Block> blocks(N);
    set<int> distinct_weights;
    set<pair<int, int>> cut_pairs;

    for (int i = 0; i < N; i++) {
        cin >> blocks[i].x >> blocks[i].y >> blocks[i].z;
        int x = blocks[i].x;
        int y = blocks[i].y;
        int z = blocks[i].z;

        // Cut along X:
        for (int cx = 1; cx < x; cx++) {
            int w1 = cx * y * z;
            int w2 = (x - cx) * y * z;
            distinct_weights.insert(w1);
            distinct_weights.insert(w2);
            cut_pairs.insert({w1, w2});
            cut_pairs.insert({w2, w1});
        }
        // Cut along Y:
        for (int cy = 1; cy < y; cy++) {
            int w1 = x * cy * z;
            int w2 = x * (y - cy) * z;
            distinct_weights.insert(w1);
            distinct_weights.insert(w2);
            cut_pairs.insert({w1, w2});
            cut_pairs.insert({w2, w1});
        }
        // Cut along Z:
        for (int cz = 1; cz < z; cz++) {
            int w1 = x * y * cz;
            int w2 = x * y * (z - cz);
            distinct_weights.insert(w1);
            distinct_weights.insert(w2);
            cut_pairs.insert({w1, w2});
            cut_pairs.insert({w2, w1});
        }
    }

    vector<int> W(distinct_weights.begin(), distinct_weights.end());
    int K = W.size();
    if (K == 0) {
        cout << 0 << "\n";
        return 0;
    }

    auto get_id = [&](int w) {
        return lower_bound(W.begin(), W.end(), w) - W.begin() + 1;
    };

    HopcroftKarp hk(K, K);
    for (auto& p : cut_pairs) {
        int u = get_id(p.first);
        int v = get_id(p.second);
        hk.add_edge(u, v);
    }

    int M = hk.max_matching();
    int ans = 2 * K - M;
    cout << ans << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
