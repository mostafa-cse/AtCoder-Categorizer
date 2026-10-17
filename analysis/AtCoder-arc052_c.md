# Problem Analysis: AtCoder-arc052_c — C. 高橋くんと不思議な道

**Problem ID**: `AtCoder-arc052_c`  
**Contest**: `arc052`  
**Rating / Difficulty**: 2277  
**URL**: https://atcoder.jp/contests/arc052/tasks/arc052_c  
**VJudge Tag**: `[problem:AtCoder-arc052_c]`  
**Category File**: [`../categories/graph_theory/dijkstra_quadratic_b_edge_state_pruning.md`](../categories/graph_theory/dijkstra_quadratic_b_edge_state_pruning.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra's Algorithm`  

---

## 1. Problem Statement & Key Idea
In a graph with Type A edges (cost 1) and Type B edges (the $k$-th traversed Type B edge costs $k$), find the minimum cost path from vertex 0 to all other vertices.

## 2. Core Observation & Invariant
Using $k$ Type B edges incurs quadratic cost $k(k+1)/2$. Since any simple Type A path costs $< N$, taking more than $\sqrt{2N} \approx 141$ Type B edges cannot compensate for Type A savings. For $k < B$, we maintain exact Type A cost $dist[u][k]$; for $k \ge B$, only the minimum $k$ is needed.

## 3. Step-by-Step Algorithm
1. 1. Type A edges cost 1 each, while the $k$-th Type B edge costs $k$, so traversing $k$ Type B edges adds $\sum_{j=1}^k j = \frac{k(k+1)}{2}$.\n2. The total cost of reaching vertex $u$ with $a$ Type A edges and $k$ Type B edges is $a + \frac{k(k+1)}{2}$.\n3. For $k \le B = 150$, maintain $dist[u][k]$, the minimum Type A count to reach $u$ with exactly $k$ Type B edges. State transitions in Dijkstra prioritize total cost $a + k(k+1)/2$.\n4. For $k \ge B$, each additional Type B edge costs $\ge 150 > N$. Two paths with $k_1 < k_2$ can never be overtaken by $k_2$ because saving at most $N$ Type A edges cannot offset the quadratic penalty. Thus for $k \ge B$, we only maintain $\min(k)$ at each vertex.\n5. Run Dijkstra on states $(u, k, a)$ with this two-regime pruning. Total state count is $O(N \sqrt{N} + M)$, which solves the problem in $O(N \sqrt{N} \log(N \sqrt{N}))$.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \log(N B)) where B = \min(N, 150)`
- **Space Complexity**: `O(N B + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

struct Edge {
    int to;
    int type;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<Edge>> adj(n);
    for (int i = 0; i < m; i++) {
        int c, u, v;
        cin >> c >> u >> v;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    const int B = 150;
    vector<vector<int>> dist(n, vector<int>(B, 1e9));
    vector<pair<int, int>> min_b(n, {1e9, 1e9});

    typedef tuple<long long, int, int, int> State;
    priority_queue<State, vector<State>, greater<State>> pq;

    dist[0][0] = 0;
    pq.push({0, 0, 0, 0});

    vector<long long> ans(n, INF);

    while (!pq.empty()) {
        auto [cost, u, k, a] = pq.top();
        pq.pop();

        ans[u] = min(ans[u], cost);

        if (k < B) {
            if (a > dist[u][k]) continue;
        } else {
            if (make_pair(k, a) > min_b[u]) continue;
        }

        for (const auto& e : adj[u]) {
            int v = e.to;
            int nk = k + e.type;
            int na = a + (1 - e.type);
            long long ncost = na + 1LL * nk * (nk + 1) / 2;

            if (nk < B) {
                if (na < dist[v][nk]) {
                    dist[v][nk] = na;
                    pq.push({ncost, v, nk, na});
                }
            } else {
                pair<int, int> p = {nk, na};
                if (p < min_b[v]) {
                    min_b[v] = p;
                    pq.push({ncost, v, nk, na});
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << ans[i] << "\n";
    }

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
