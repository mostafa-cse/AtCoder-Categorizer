# Problem Analysis: AtCoder-arc049_c — C. ぬりまーす

**Problem ID**: `AtCoder-arc049_c`  
**Contest**: `arc049`  
**Rating / Difficulty**: 2308  
**URL**: https://atcoder.jp/contests/arc049/tasks/arc049_c  
**VJudge Tag**: `[problem:AtCoder-arc049_c]`  
**Category File**: [`../categories/graph_theory/branching_2sat_conflict_topological_cycle.md`](../categories/graph_theory/branching_2sat_conflict_topological_cycle.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Topological Sorting`  

---

## 1. Problem Statement & Key Idea
Given directed dependency constraints of Type 1 ($y$ must be painted before $x$) and Type 2 ($v$ must not be painted when painting $u$), find the maximum number of paintable vertices.

## 2. Core Observation & Invariant
Each Type 2 constraint $(u, v)$ requires either $u$ is painted before $v$ (adding directed edge $u \to v$) or $u$ is never painted (marking $u$ as forbidden).

## 3. Step-by-Step Algorithm
1. Since $B \le 10$, branch over all $2^B \le 1024$ assignments of Type 2 constraints.
2. For each assignment, construct the dependency graph with Type 1 edges $y \to x$ and Type 2 Choice 1 edges $u \to v$.
3. Propagate forbidden status to all reachable descendants, then run Kahn's topological sort on remaining vertices to detect and eliminate cycles, maximizing the number of painted vertices.

## 4. Complexity Analysis
- **Time Complexity**: `O(2^B (N + A + B))`
- **Space Complexity**: `O(N + A + B)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

struct Edge {
    int u, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, A;
    if (!(cin >> N >> A)) return 0;
    vector<Edge> type1(A);
    for (int i = 0; i < A; ++i) {
        cin >> type1[i].u >> type1[i].v;
    }

    int B;
    cin >> B;
    vector<Edge> type2(B);
    for (int i = 0; i < B; ++i) {
        cin >> type2[i].u >> type2[i].v;
    }

    int ans = 0;

    for (int mask = 0; mask < (1 << B); ++mask) {
        vector<vector<int>> adj(N + 1);
        vector<int> in_degree(N + 1, 0);
        vector<bool> forbidden(N + 1, false);

        for (const auto& e : type1) {
            adj[e.v].push_back(e.u);
        }

        for (int i = 0; i < B; ++i) {
            if (mask & (1 << i)) {
                adj[type2[i].u].push_back(type2[i].v);
            } else {
                forbidden[type2[i].u] = true;
            }
        }

        queue<int> q;
        for (int i = 1; i <= N; ++i) {
            if (forbidden[i]) q.push(i);
        }
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (!forbidden[v]) {
                    forbidden[v] = true;
                    q.push(v);
                }
            }
        }

        vector<int> deg(N + 1, 0);
        for (int u = 1; u <= N; ++u) {
            if (forbidden[u]) continue;
            for (int v : adj[u]) {
                if (!forbidden[v]) {
                    deg[v]++;
                }
            }
        }

        queue<int> topo_q;
        int painted = 0;
        for (int i = 1; i <= N; ++i) {
            if (!forbidden[i] && deg[i] == 0) {
                topo_q.push(i);
            }
        }

        while (!topo_q.empty()) {
            int u = topo_q.front();
            topo_q.pop();
            painted++;
            for (int v : adj[u]) {
                if (!forbidden[v]) {
                    deg[v]--;
                    if (deg[v] == 0) {
                        topo_q.push(v);
                    }
                }
            }
        }

        ans = max(ans, painted);
    }

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
