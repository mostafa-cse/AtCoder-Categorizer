# Problem Analysis: AtCoder-arc010_4 — D - 情報伝播

**Problem ID**: `AtCoder-arc010_4`  
**Contest**: `arc010`  
**Rating / Difficulty**: 2481  
**URL**: https://atcoder.jp/contests/arc010/tasks/arc010_4  
**VJudge Tag**: `[problem:AtCoder-arc010_4]`  
**Category File**: [`../categories/graph_theory/information_propagation_scc_indegree_zero.md`](../categories/graph_theory/information_propagation_scc_indegree_zero.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Connectivity`  
- **Topic (Skill)**: `Strongly Connected Components (SCC)`  

---

## 1. Problem Statement & Key Idea
Find the minimum number of ally nodes to directly inform such that all $N$ allies receive the message without being intercepted by any of the $M$ spies.

## 2. Core Observation & Invariant
Ally $u$ can transmit a message to ally $v$ safely if and only if $\text{dist}^2(u, v) < R_u^2$, where $R_u^2 = \min_{k} \text{dist}^2(u, \text{spy}_k)$ is the squared distance from $u$ to the nearest spy. This defines a directed transmission graph. Within any strongly connected component (SCC), informing any one node informs all nodes in the component. Contracting the graph into its DAG of SCCs, the minimum number of nodes to inform equals the number of SCCs with in-degree zero.

## 3. Step-by-Step Algorithm
1. 1. For each ally $i$, compute $R_i^2 = \min_{j} \text{dist}^2(i, \text{spy}_j)$.
2. 2. Construct the directed graph with edge $i \to j$ if $\text{dist}^2(i, j) < R_i^2$.
3. 3. Decompose the directed graph into Strongly Connected Components (SCC) using Kosaraju's or Tarjan's algorithm.
4. 4. Build the condensed DAG and count the number of SCCs that have zero incoming edges from other SCCs.
5. 5. Output this count.

## 4. Complexity Analysis
- **Time Complexity**: `O(N M + N^2)`
- **Space Complexity**: `O(N^2)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;
vector<pair<long long, long long>> allies;
vector<pair<long long, long long>> spies;
vector<vector<int>> adj, radj;
vector<bool> visited;
vector<int> order;
vector<int> scc_id;

void dfs1(int u) {
    visited[u] = true;
    for (int v : adj[u]) {
        if (!visited[v]) dfs1(v);
    }
    order.push_back(u);
}

void dfs2(int u, int cid) {
    scc_id[u] = cid;
    for (int v : radj[u]) {
        if (scc_id[v] == -1) dfs2(v, cid);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> N)) return 0;
    allies.resize(N);
    for (int i = 0; i < N; ++i) cin >> allies[i].first >> allies[i].second;

    cin >> M;
    spies.resize(M);
    for (int i = 0; i < M; ++i) cin >> spies[i].first >> spies[i].second;

    const long long INF = 4e18;
    vector<long long> R2(N, INF);
    for (int i = 0; i < N; ++i) {
        long long ax = allies[i].first, ay = allies[i].second;
        for (int j = 0; j < M; ++j) {
            long long sx = spies[j].first, sy = spies[j].second;
            long long d2 = (ax - sx) * (ax - sx) + (ay - sy) * (ay - sy);
            if (d2 < R2[i]) R2[i] = d2;
        }
    }

    adj.resize(N);
    radj.resize(N);
    for (int i = 0; i < N; ++i) {
        long long ax = allies[i].first, ay = allies[i].second;
        for (int j = 0; j < N; ++j) {
            if (i == j) continue;
            long long bx = allies[j].first, by = allies[j].second;
            long long d2 = (ax - bx) * (ax - bx) + (ay - by) * (ay - by);
            if (d2 < R2[i]) {
                adj[i].push_back(j);
                radj[j].push_back(i);
            }
        }
    }

    visited.assign(N, false);
    for (int i = 0; i < N; ++i) {
        if (!visited[i]) dfs1(i);
    }

    scc_id.assign(N, -1);
    int num_scc = 0;
    for (int i = N - 1; i >= 0; --i) {
        int u = order[i];
        if (scc_id[u] == -1) {
            dfs2(u, num_scc++);
        }
    }

    vector<int> in_deg(num_scc, 0);
    for (int u = 0; u < N; ++u) {
        for (int v : adj[u]) {
            if (scc_id[u] != scc_id[v]) {
                in_deg[scc_id[v]]++;
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < num_scc; ++i) {
        if (in_deg[i] == 0) ans++;
    }

    cout << ans << "\n";
    return 0;
}
```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
