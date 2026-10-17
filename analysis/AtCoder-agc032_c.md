# Problem Analysis: AtCoder-agc032_c — C. Three Circuits

**Problem ID**: `AtCoder-agc032_c`  
**Contest**: `agc032`  
**Rating / Difficulty**: 2284  
**URL**: https://atcoder.jp/contests/agc032/tasks/agc032_c  
**VJudge Tag**: `[problem:AtCoder-agc032_c]`  
**Category File**: [`../categories/graph_theory/eulerian_three_circuit_degree_decomposition.md`](../categories/graph_theory/eulerian_three_circuit_degree_decomposition.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Eulerian Path`  
- **Topic (Skill)**: `Eulerian Path and Cycle`  

---

## 1. Problem Statement & Key Idea
Given a connected undirected graph where every vertex has even degree, determine if the edges can be partitioned into three or more simple cycles.

## 2. Core Observation & Invariant
Partitioning edges into circuits requires every vertex to have an even degree. If $\max \deg \ge 6$ or the count of degree-4 vertices $c_4 \ge 3$, 3 circuits always exist; if $c_4 \le 1$, impossible; if $c_4 = 2$, 3 circuits exist iff the two degree-4 vertices are connected by 2 paths and have independent simple loops, decidable via path tracing.

## 3. Step-by-Step Algorithm
1. 1. Every circuit is an Eulerian subgraph, so all vertex degrees must be even. If any vertex has an odd degree, output `No`.\n2. Since degree-2 vertices only subdivide paths, branching points must have degree $\ge 4$. If any vertex has degree $\ge 6$, edges can be paired into $\ge 3$ intersecting cycles, yielding `Yes`.\n3. If max degree is 4: count vertices with degree 4 ($c_4$). If $c_4 \ge 3$, routing through the 3 branching nodes always permits $\ge 3$ edge-disjoint circuits (`Yes`). If $c_4 \le 1$, the graph is a single cycle or figure-eight, which can only decompose into at most 2 circuits (`No`).\n4. For $c_4 = 2$ with degree-4 vertices $u$ and $v$: if all 4 paths from $u$ terminate at $v$ (4-strand theta graph), any circuit must alternate between $u$ and $v$ and thus consume an even number of paths, allowing at most $\lfloor 4 / 2 \rfloor = 2$ circuits (`No`). However, if at least one path from $u$ returns to $u$ without visiting $v$, the graph decomposes into a loop at $u$, a loop at $v$, and 2 paths between $u$ and $v$, giving exactly 3 circuits (`Yes`).\n5. Path tracing from $u$ along degree-2 paths runs in $O(N + M)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(N + M)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> adj(n + 1);
    vector<int> deg(n + 1, 0);

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
        deg[u]++;
        deg[v]++;
    }

    for (int i = 1; i <= n; i++) {
        if (deg[i] % 2 != 0) {
            cout << "No\n";
            return 0;
        }
    }

    int c4 = 0;
    bool has_ge6 = false;
    vector<int> deg4_nodes;

    for (int i = 1; i <= n; i++) {
        if (deg[i] >= 6) {
            has_ge6 = true;
        } else if (deg[i] == 4) {
            c4++;
            deg4_nodes.push_back(i);
        }
    }

    if (has_ge6 || c4 >= 3) {
        cout << "Yes\n";
        return 0;
    }

    if (c4 <= 1) {
        cout << "No\n";
        return 0;
    }

    int u = deg4_nodes[0];
    int v = deg4_nodes[1];

    bool loop_at_u = false;
    for (int start_nbr : adj[u]) {
        int prev = u;
        int cur = start_nbr;
        while (cur != u && cur != v) {
            int nxt = -1;
            for (int neighbor : adj[cur]) {
                if (neighbor != prev) {
                    nxt = neighbor;
                    break;
                }
            }
            prev = cur;
            cur = nxt;
        }
        if (cur == u) {
            loop_at_u = true;
            break;
        }
    }

    if (loop_at_u) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
