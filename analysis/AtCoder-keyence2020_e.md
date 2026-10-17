# Problem Analysis: AtCoder-keyence2020_e — E. Bichromization

**Problem ID**: `AtCoder-keyence2020_e`  
**Contest**: `keyence2020`  
**Rating / Difficulty**: 2340  
**URL**: https://atcoder.jp/contests/keyence2020/tasks/keyence2020_e  
**VJudge Tag**: `[problem:AtCoder-keyence2020_e]`  
**Category File**: [`../categories/basics/bichromization_distance_greedy_bfs.md`](../categories/basics/bichromization_distance_greedy_bfs.md)  

- **Tag (Domain)**: `Basics`  
- **Subtopic**: `Greedy and Constructive`  
- **Topic (Skill)**: `Basic Constructive Algorithms`  

---

## 1. Problem Statement & Key Idea
Color vertices Black and White and assign edge weights so that the shortest path from each vertex $v$ to an opposite color equals $D_v$. Greedy processing in ascending order of $D_v$ pairs each vertex with a neighbor $u$ having $D_u \le D_v$ in $O(N \log N + M)$.

## 2. Core Observation & Invariant
For any vertex $v$, its nearest opposite-color vertex has distance $D_v$. Therefore, $v$ must have at least one neighbor $u$ with $D_u \le D_v$. When processed in ascending order of $D$, coloring $v$ opposite to an already colored neighbor $u$ with $D_u \le D_v$ and setting edge weight $D_v$ satisfies $v$ without violating $u$.

## 3. Step-by-Step Algorithm
1. Check that every vertex $v$ has at least one neighbor with $D_u \le D_v$; if not, output -1.
2. Sort vertices in ascending order of $D_v$.
3. If $v$ is adjacent to an already colored neighbor $u$ with $D_u \le D_v$, color $v$ opposite to $u$ and set edge weight $D_v$.
4. Otherwise, pair $v$ with an uncolored neighbor $w$ having $D_w = D_v$, coloring them with opposite colors and setting edge weight $D_v$.
5. Assign $10^9$ to all remaining edges in $O(N \log N + M)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N \log N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<long long> d(n);
    for (int i = 0; i < n; ++i) {
        cin >> d[i];
    }

    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        --u; --v;
        adj[u].push_back({v, i});
        adj[v].push_back({u, i});
    }

    for (int v = 0; v < n; ++v) {
        bool ok = false;
        for (auto& edge : adj[v]) {
            int nb = edge.first;
            if (d[nb] <= d[v]) {
                ok = true;
                break;
            }
        }
        if (!ok) {
            cout << -1 << "\n";
            return 0;
        }
    }

    vector<int> order(n);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a, int b) {
        return d[a] < d[b];
    });

    vector<int> color(n, -1); // 0 = B, 1 = W
    vector<long long> edge_weight(m, 1000000000LL);

    for (int v : order) {
        if (color[v] != -1) continue;

        bool found = false;
        for (auto& edge : adj[v]) {
            int nb = edge.first;
            int e_idx = edge.second;
            if (color[nb] != -1 && d[nb] <= d[v]) {
                color[v] = 1 - color[nb];
                edge_weight[e_idx] = d[v];
                found = true;
                break;
            }
        }

        if (!found) {
            for (auto& edge : adj[v]) {
                int nb = edge.first;
                int e_idx = edge.second;
                if (color[nb] == -1 && d[nb] == d[v]) {
                    color[v] = 0; // B
                    color[nb] = 1; // W
                    edge_weight[e_idx] = d[v];
                    found = true;
                    break;
                }
            }
        }

        if (!found) {
            cout << -1 << "\n";
            return 0;
        }
    }

    string s(n, 'B');
    for (int i = 0; i < n; ++i) {
        s[i] = (color[i] == 0 ? 'B' : 'W');
    }

    cout << s << "\n";
    for (int i = 0; i < m; ++i) {
        cout << edge_weight[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
