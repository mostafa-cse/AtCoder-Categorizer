# Problem Analysis: AtCoder-arc099_c — Independence

**Problem ID**: `AtCoder-arc099_c`  
**Contest**: `arc099`  
**Rating / Difficulty**: 2160  
**URL**: https://atcoder.jp/contests/arc099/tasks/arc099_c  
**VJudge Tag**: `[problem:AtCoder-arc099_c]`  
**Category File**: [`../categories/graph_theory/clique_partition_complement_bipartite_knapsack.md`](../categories/graph_theory/clique_partition_complement_bipartite_knapsack.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Cliques and Independent Sets`  
- **Topic (Skill)**: `Maximum Clique`  

---

## 1. Problem Statement & Key Idea
Partition a graph into two cliques minimizing edges with endpoints in the same state. A clique partition in G corresponds to a 2-coloring (bipartite coloring) in the complement graph G_bar. Knapsack balances the component color classes.

## 2. Core Observation & Invariant
Two vertices belong to the same clique in G iff there is NO edge between them in the complement graph G_bar. Thus, the complement graph must be bipartite; otherwise no valid partition exists (output -1). For each bipartite connected component with partition sizes (s_i, t_i), choose one side for state A using knapsack DP, minimizing same-state edges C(a, 2) + C(b, 2).

## 3. Step-by-Step Algorithm
1. Construct the complement graph G_bar of size N <= 700.
2. Check if G_bar is bipartite via BFS/DFS 2-coloring. If an odd cycle is detected, output -1.
3. Collect component partition sizes (s_i, t_i).
4. Use a bitset knapsack to compute all reachable sizes a of state A: dp = (dp << s_i) | (dp << t_i).
5. Find achievable a minimizing a*(a-1)/2 + (N-a)*(N-a-1)/2.

## 4. Complexity Analysis
- **Time Complexity**: `O(N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code (Verified & Clean)
```cpp
#include <iostream>
#include <vector>
#include <bitset>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<bool>> adj(n + 1, vector<bool>(n + 1, false));
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u][v] = adj[v][u] = true;
    }

    vector<vector<int>> comp_adj(n + 1);
    for (int i = 1; i <= n; ++i) {
        for (int j = i + 1; j <= n; ++j) {
            if (!adj[i][j]) {
                comp_adj[i].push_back(j);
                comp_adj[j].push_back(i);
            }
        }
    }

    vector<int> color(n + 1, 0);
    vector<pair<int, int>> comps;

    for (int i = 1; i <= n; ++i) {
        if (color[i] != 0) continue;

        int cnt1 = 0, cnt2 = 0;
        vector<int> q = {i};
        color[i] = 1;
        cnt1++;

        bool ok = true;
        for (size_t head = 0; head < q.size(); ++head) {
            int u = q[head];
            for (int v : comp_adj[u]) {
                if (color[v] == 0) {
                    color[v] = -color[u];
                    if (color[v] == 1) cnt1++; else cnt2++;
                    q.push_back(v);
                } else if (color[v] == color[u]) {
                    ok = false;
                }
            }
        }

        if (!ok) {
            cout << -1 << "\n";
            return 0;
        }

        comps.push_back({cnt1, cnt2});
    }

    bitset<705> dp;
    dp[0] = 1;

    for (const auto& c : comps) {
        dp = (dp << c.first) | (dp << c.second);
    }

    long long min_same_state = 1e18;
    for (int a = 0; a <= n; ++a) {
        if (dp[a]) {
            int b = n - a;
            long long inside = 1LL * a * (a - 1) / 2 + 1LL * b * (b - 1) / 2;
            min_same_state = min(min_same_state, inside);
        }
    }

    if (min_same_state > 1e17) {
        cout << -1 << "\n";
    } else {
        cout << min_same_state << "\n";
    }

    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
