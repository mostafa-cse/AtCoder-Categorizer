# Problem Analysis: AtCoder-arc030_3 — C. 有向グラフ

**Problem ID**: `AtCoder-arc030_3`  
**Contest**: `arc030`  
**Rating / Difficulty**: 2180  
**URL**: https://atcoder.jp/contests/arc030/tasks/arc030_3  
**VJudge Tag**: `[problem:AtCoder-arc030_3]`  
**Category File**: [`../categories/graph_theory/scc_condensation_lexicographical_dag_dp.md`](../categories/graph_theory/scc_condensation_lexicographical_dag_dp.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Connectivity`  
- **Topic (Skill)**: `Strongly Connected Components (SCC)`  

---

## 1. Problem Statement & Key Idea
In a directed graph where each vertex carries a character, visit vertices along a walk to collect exactly k characters such that the resulting string is lexicographically smallest. Contract the graph into an SCC DAG, sort characters within each SCC, and execute string DP on the DAG.

## 2. Core Observation & Invariant
Any walk inside an SCC can visit all its vertices and collect any subset of its characters in sorted order. Once leaving an SCC, you can never return to it. Thus, on the condensed DAG, taking c characters from SCC u takes the c smallest characters of u in non-decreasing order, followed by characters from a successor SCC.

## 3. Step-by-Step Algorithm
1. Find strongly connected components using Kosaraju's or Tarjan's algorithm.
2. For each SCC, collect all vertex characters and sort them in non-decreasing order.
3. Build the condensed DAG of SCCs and compute a topological ordering.
4. Run dynamic programming on the DAG in reverse topological order: dp[u][len] is the lexicographically smallest string of length len starting at SCC u.
5. Transitions: for each count take in [0, min(|C_u|, k)], prefix = scc_chars[u].substr(0, take), and for each successor v in DAG and rem in [0, k - take], update dp[u][take + rem] = min(dp[u][take + rem], prefix + dp[v][rem]).
6. Find the minimum across all dp[u][k] for 0 <= u < scc_cnt. If no path can collect k characters, output -1.

## 4. Complexity Analysis
- **Time Complexity**: `O(N K^2 + M K)`
- **Space Complexity**: `O(N K)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

const string INF = "{"; // larger than any lowercase string

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;

    vector<char> c(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> c[i];
    }

    vector<vector<int>> adj(n + 1), radj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        radj[v].push_back(u);
    }

    // Kosaraju's SCC
    vector<bool> vis(n + 1, false);
    vector<int> order;
    order.reserve(n);

    auto dfs1 = [&](auto& self, int u) -> void {
        vis[u] = true;
        for (int v : adj[u]) {
            if (!vis[v]) self(self, v);
        }
        order.push_back(u);
    };

    for (int i = 1; i <= n; ++i) {
        if (!vis[i]) dfs1(dfs1, i);
    }

    vector<int> scc_id(n + 1, -1);
    int scc_cnt = 0;
    vector<string> scc_chars;

    auto dfs2 = [&](auto& self, int u, int id) -> void {
        scc_id[u] = id;
        scc_chars[id].push_back(c[u]);
        for (int v : radj[u]) {
            if (scc_id[v] == -1) self(self, v, id);
        }
    };

    for (int i = n - 1; i >= 0; --i) {
        int u = order[i];
        if (scc_id[u] == -1) {
            scc_chars.push_back("");
            dfs2(dfs2, u, scc_cnt++);
        }
    }

    // Sort characters in each SCC
    for (int i = 0; i < scc_cnt; ++i) {
        sort(scc_chars[i].begin(), scc_chars[i].end());
    }

    // Build condensed DAG
    vector<vector<int>> dag(scc_cnt);
    vector<int> in_degree(scc_cnt, 0);
    vector<vector<bool>> has_edge(scc_cnt, vector<bool>(scc_cnt, false));

    for (int u = 1; u <= n; ++u) {
        for (int v : adj[u]) {
            int su = scc_id[u], sv = scc_id[v];
            if (su != sv && !has_edge[su][sv]) {
                has_edge[su][sv] = true;
                dag[su].push_back(sv);
                in_degree[sv]++;
            }
        }
    }

    // Topological sort of DAG
    vector<int> q;
    for (int i = 0; i < scc_cnt; ++i) {
        if (in_degree[i] == 0) q.push_back(i);
    }
    vector<int> topo;
    int head = 0;
    while (head < (int)q.size()) {
        int u = q[head++];
        topo.push_back(u);
        for (int v : dag[u]) {
            if (--in_degree[v] == 0) q.push_back(v);
        }
    }

    // DP on DAG in reverse topological order
    // dp[u][len] = lexicographically smallest string of length len starting at u
    vector<vector<string>> dp(scc_cnt, vector<string>(k + 1, INF));

    for (int i = scc_cnt - 1; i >= 0; --i) {
        int u = topo[i];
        dp[u][0] = "";
        int sz = (int)scc_chars[u].size();

        for (int take = 0; take <= min(sz, k); ++take) {
            string pref = scc_chars[u].substr(0, take);
            if (take <= k) {
                if (dp[u][take] == INF || pref < dp[u][take]) {
                    dp[u][take] = pref;
                }
            }
            for (int v : dag[u]) {
                for (int rem = 0; rem <= k - take; ++rem) {
                    if (dp[v][rem] != INF) {
                        string cand = pref + dp[v][rem];
                        if (dp[u][take + rem] == INF || cand < dp[u][take + rem]) {
                            dp[u][take + rem] = cand;
                        }
                    }
                }
            }
        }
    }

    string best = INF;
    for (int i = 0; i < scc_cnt; ++i) {
        if (dp[i][k] != INF && (best == INF || dp[i][k] < best)) {
            best = dp[i][k];
        }
    }

    if (best == INF) {
        cout << -1 << "\n";
    } else {
        cout << best << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
