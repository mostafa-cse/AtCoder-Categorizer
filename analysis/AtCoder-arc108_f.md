# Problem Analysis: AtCoder-arc108_f — F - Paint Tree

**Problem ID**: `AtCoder-arc108_f`  
**Contest**: `arc108`  
**Rating / Difficulty**: 2646  
**URL**: https://atcoder.jp/contests/arc108/tasks/arc108_f  
**VJudge Tag**: `[problem:AtCoder-arc108_f]`  
**Category File**: [`../categories/graph_theory/paint_tree_diameter_niceness.md`](../categories/graph_theory/paint_tree_diameter_niceness.md)  

- **Tag (Domain)**: `Graph Theory`  
- **Subtopic**: `Graph Traversal`  
- **Topic (Skill)**: `Tree Diameter`  

---

## 1. Problem Statement & Key Idea
Given a tree of N vertices, paint each vertex Black or White. Niceness is the maximum distance between vertices of the same color. Compute the sum of nicenesses over all 2^N colorings modulo 10^9 + 7.

## 2. Core Observation & Invariant
Let u, v be endpoints of a tree diameter of length D. If u and v have the same color, niceness is always D (2^(N-1) colorings). If u and v have different colors (say u White, v Black), for any threshold d, a vertex w can be freely colored if max(d_u(w), d_v(w)) <= d. If min(d_u(w), d_v(w)) > d, 0 colorings exist. Otherwise, its color is forced. Thus, the number of colorings with niceness <= d is 2 * 2^{free(d)} for d >= max_w min(d_u(w), d_v(w)).

## 3. Step-by-Step Algorithm
1. Run 2 BFS passes to find diameter endpoints u, v and length D.
2. Compute distances d_u(w) and d_v(w) for all w in [1, N].
3. Compute min_req = max_w min(d_u(w), d_v(w)).
4. Build frequency array of max(d_u(w), d_v(w)) for all w not in {u, v} and compute prefix sums pref_free[d].
5. For d from min_req to D, compute ways_le[d] = 2 * 2^{pref_free[d]} mod (10^9+7).
6. Accumulate d * (ways_le[d] - ways_le[d-1]) plus D * 2^{N-1}.
7. Output total sum modulo 10^9 + 7.

## 4. Complexity Analysis
- **Time Complexity**: `O(N)`
- **Space Complexity**: `O(N)`

## 5. C++ Source Code
```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const int MOD = 1000000007;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    if (!(cin >> N)) return 0;

    vector<vector<int>> adj(N + 1);
    for (int i = 0; i < N - 1; ++i) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    auto bfs = [&](int start) -> vector<int> {
        vector<int> dist(N + 1, -1);
        queue<int> q;
        dist[start] = 0;
        q.push(start);
        while (!q.empty()) {
            int u = q.front();
            q.pop();
            for (int v : adj[u]) {
                if (dist[v] == -1) {
                    dist[v] = dist[u] + 1;
                    q.push(v);
                }
            }
        }
        return dist;
    };

    // Find diameter endpoints u and v
    vector<int> d1 = bfs(1);
    int u = 1;
    for (int i = 2; i <= N; ++i) {
        if (d1[i] > d1[u]) u = i;
    }

    vector<int> du = bfs(u);
    int v = 1;
    for (int i = 2; i <= N; ++i) {
        if (du[i] > du[v]) v = i;
    }

    vector<int> dv = bfs(v);
    int D = du[v];

    vector<long long> pow2(N + 1, 1);
    for (int i = 1; i <= N; ++i) {
        pow2[i] = (pow2[i - 1] * 2) % MOD;
    }

    int min_req = 0;
    for (int w = 1; w <= N; ++w) {
        min_req = max(min_req, min(du[w], dv[w]));
    }

    vector<int> freq(D + 1, 0);
    for (int w = 1; w <= N; ++w) {
        if (w == u || w == v) continue;
        int m = max(du[w], dv[w]);
        if (m <= D) freq[m]++;
    }

    vector<int> pref_free(D + 1, 0);
    for (int d = 1; d <= D; ++d) {
        pref_free[d] = pref_free[d - 1] + freq[d];
    }

    vector<long long> ways_le(D + 1, 0);
    for (int d = min_req; d <= D; ++d) {
        ways_le[d] = (2 * pow2[pref_free[d]]) % MOD;
    }

    long long ans = 0;
    for (int d = min_req; d <= D; ++d) {
        long long ways_eq = (ways_le[d] - ways_le[d - 1] + MOD) % MOD;
        ans = (ans + (long long)d * ways_eq) % MOD;
    }

    // Contribution when u and v have the same color:
    // 2^(N-1) colorings, each has diameter D
    long long same_color_contrib = ((long long)D * pow2[N - 1]) % MOD;
    ans = (ans + same_color_contrib) % MOD;

    cout << ans << "\n";
    return 0;
}

```

---
*Curated as part of the Zero-Duplicate Premier AtCoder Curriculum.*
