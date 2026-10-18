# Problem Analysis: AtCoder-abc414_f — F. Jump Traveling

**Problem ID**: `AtCoder-abc414_f`  
**Contest**: `abc414`  
**Rating / Difficulty**: 2357  
**URL**: https://atcoder.jp/contests/abc414/tasks/abc414_f  
**VJudge Tag**: `[problem:AtCoder-abc414_f]`  
**Category File**: [`../categories/graph_theory/phase_bounded_tree_bfs.md`](../categories/graph_theory/phase_bounded_tree_bfs.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Breadth First Search (BFS)`  

---

## 1. Problem Statement & Key Idea
Find minimum tree jumps of length $K$ from vertex 1 to all vertices. BFS over $2(N-1)$ directed edges limits visits per vertex to at most 2 per phase $d \bmod K$, yielding optimal paths in $O(NK)$ time.

## 2. Core Observation & Invariant
Jumping distance $K$ in a tree can be modeled as taking $K$ tree steps without immediately traversing back along the entry edge. In BFS, each vertex $v$ at step phase $d \bmod K$ needs to be visited at most twice across different incoming edges; third and subsequent visits to the same vertex at the same phase provide no new unvisited outgoing transitions.

## 3. Step-by-Step Algorithm
1. Represent the tree edges as $2(N-1)$ directed edges.
2. Run BFS with queue states $(d, v, e)$ where $d$ is total steps, $v$ is current vertex, and $e$ is incoming directed edge.
3. Track visit count $cnt[d \bmod K][v] \le 2$ and traversed edges $dp[(d+1) \bmod K][e_2]$. Skip transitions if $cnt == 2$ or if immediate backtracking occurs when $d \bmod K \ne 0$.
4. Record $ans[v] = d / K$ when $d \bmod K == 0$. Runs in $O(NK)$ time.

## 4. Complexity Analysis
- **Time Complexity**: `O(NK)`
- **Space Complexity**: `O(NK)`

## 5. C++ Source Code
```cpp
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, k;
    if (!(cin >> n >> k)) return;
    vector<vector<pair<int, int>>> g(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        u--; v--;
        g[u].push_back({v, 2 * i});
        g[v].push_back({u, 2 * i + 1});
    }

    int num_edges = 2 * n - 2;
    vector<vector<int>> dp(k, vector<int>(num_edges, -1));
    vector<int> ans(n, -1);
    vector<vector<int>> cnt(k, vector<int>(n, 0));
    deque<tuple<int, int, int>> dq;
    dq.push_back({0, 0, -1});

    while (!dq.empty()) {
        auto [d, v, e] = dq.front();
        dq.pop_front();

        if (d % k == 0 && ans[v] == -1) {
            ans[v] = d / k;
        }

        if (cnt[d % k][v] == 2) continue;
        cnt[d % k][v]++;

        for (auto& edge : g[v]) {
            int u = edge.first;
            int e2 = edge.second;
            if (e != -1 && (e ^ e2) == 1 && (d % k != 0)) continue;
            int next_phase = (d + 1) % k;
            if (dp[next_phase][e2] == -1) {
                dp[next_phase][e2] = d + 1;
                dq.push_back({d + 1, u, e2});
            }
        }
    }

    for (int i = 1; i < n; i++) {
        cout << ans[i] << (i == n - 1 ? "" : " ");
    }
    cout << "\n";
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    if (cin >> t) {
        while (t--) solve();
    }
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
