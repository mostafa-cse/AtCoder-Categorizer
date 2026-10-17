# Problem Analysis: AtCoder-abc245_g — G. Foreign Friends

**Problem ID**: `AtCoder-abc245_g`  
**Contest**: `abc245`  
**Rating / Difficulty**: 2270  
**URL**: https://atcoder.jp/contests/abc245/tasks/abc245_g  
**VJudge Tag**: `[problem:AtCoder-abc245_g]`  
**Category File**: [`../categories/graph_theory/dijkstra_top2_distinct_origin_countries.md`](../categories/graph_theory/dijkstra_top2_distinct_origin_countries.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Shortest Paths`  
- **Topic (Skill)**: `Dijkstra's Algorithm`  

---

## 1. Problem Statement & Key Idea
In a graph of $N$ people and $M$ weighted edges, each person belongs to a country $A_i \in [1, K]$. There are $L$ popular people. For each person $i$, find the minimum cost path to any popular person belonging to a different country ($A_{popular} \neq A_i$), or -1 if impossible.

## 2. Core Observation & Invariant
Standard multi-source Dijkstra from all popular people would only find the single shortest path, which might originate from the same country $A_i$. Because each person $i$ has only one forbidden country $A_i$, tracking the **top 2 shortest distances to popular people originating from distinct countries** at every vertex guarantees that for any vertex $i$, at least one of the top 2 shortest sources has country $\neq A_i$. Maintaining $(dist_1, country_1)$ and $(dist_2, country_2)$ with $country_1 \neq country_2$ in priority queue relaxation runs in $O((N + M) \log N)$.

## 3. Step-by-Step Algorithm
1. Initialize `dist1[u] = inf, dist2[u] = inf, c1[u] = -1, c2[u] = -1` for all $u$.
2. Push all popular vertices $u \in B$ with $dist=0$ and country $A_u$ into min-priority queue.
3. While priority queue is not empty, pop $(d, u, c)$:
4. Skip if $d > dist1[u]$ (when $c == c1[u]$) or $d > dist2[u]$ (when $c == c2[u]$).
5. For each neighbor $(v, w)$ with new distance $nd = d + w$:
6. If $c == c1[v]$, relax $dist1[v]$.
7. Else if $c == c2[v]$, relax $dist2[v]$.
8. Else if $nd < dist1[v]$, shift 1 to 2 and set 1 to $(nd, c)$, pushing into PQ.
9. Else if $nd < dist2[v]$, set 2 to $(nd, c)$, pushing into PQ.
10. For each vertex $i$, output $dist1[i]$ if $c1[i] \neq A_i$, else $dist2[i]$ if $c2[i] \neq A_i$, else -1.

## 4. Complexity Analysis
- **Time Complexity**: `O((N + M) \log N)`
- **Space Complexity**: `O(N + M)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const long long INF = 1e18;

struct State {
    long long d;
    int u;
    int c;
    bool operator>(const State& other) const {
        return d > other.d;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, k, l;
    if (!(cin >> n >> m >> k >> l)) return 0;

    vector<int> a(n + 1);
    for (int i = 1; i <= n; ++i) cin >> a[i];

    vector<int> b(l);
    for (int i = 0; i < l; ++i) cin >> b[i];

    vector<vector<pair<int, long long>>> adj(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v;
        long long c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }

    vector<long long> dist1(n + 1, INF), dist2(n + 1, INF);
    vector<int> c1(n + 1, -1), c2(n + 1, -1);

    priority_queue<State, vector<State>, greater<State>> pq;

    for (int u : b) {
        dist1[u] = 0;
        c1[u] = a[u];
        pq.push({0, u, a[u]});
    }

    while (!pq.empty()) {
        auto [d, u, c] = pq.top();
        pq.pop();

        if (c == c1[u] && d > dist1[u]) continue;
        if (c == c2[u] && d > dist2[u]) continue;
        if (c != c1[u] && c != c2[u]) continue;

        for (auto [v, w] : adj[u]) {
            long long nd = d + w;
            if (c == c1[v]) {
                if (nd < dist1[v]) {
                    dist1[v] = nd;
                    pq.push({nd, v, c});
                }
            } else if (c == c2[v]) {
                if (nd < dist2[v]) {
                    dist2[v] = nd;
                    pq.push({nd, v, c});
                }
            } else {
                if (nd < dist1[v]) {
                    dist2[v] = dist1[v];
                    c2[v] = c1[v];
                    dist1[v] = nd;
                    c1[v] = c;
                    pq.push({nd, v, c});
                } else if (nd < dist2[v]) {
                    dist2[v] = nd;
                    c2[v] = c;
                    pq.push({nd, v, c});
                }
            }
        }
    }

    for (int i = 1; i <= n; ++i) {
        long long ans = -1;
        if (c1[i] != -1 && c1[i] != a[i]) {
            ans = dist1[i];
        } else if (c2[i] != -1 && c2[i] != a[i]) {
            ans = dist2[i];
        }
        cout << ans << (i == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
